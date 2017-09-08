from django.shortcuts import render
from LazarusII.models import UnitFbiData, WeaponTDF, Damage, DownloadTDF, FeatureTDF
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.core import serializers
from chat.models import JawnUser
import json

from rest_framework import renderers
from rest_framework import viewsets, filters
import django_filters
from rest_framework import permissions

from LazarusDatabase.serializers import TotalAnnihilationModSerializer, SelectedAssetUploadRepositorySerializer, \
    LazarusModProjectSerializer, LazarusModAssetSerializer, LazarusModDependencySerializer, HPIUploadSerializer

from LazarusDatabase.models import TotalAnnihilationMod, LazarusModProject, LazarusModAsset, \
    LazarusModDependency, SelectedAssetUploadRepository, HPIUpload

from rest_framework.decorators import detail_route, list_route
from rest_framework import status
from rest_framework import viewsets
import django_filters

from rest_auth.models import LazarusCommanderAccount


class SelectedAssetUploadRepositoryFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(name="name")

    class Meta:
        model = SelectedAssetUploadRepository
        fields = ['name', 'id', 'author']

class SelectedAssetUploadRepositoryViewset(viewsets.ModelViewSet):
    queryset = SelectedAssetUploadRepository.objects.all()
    serializer_class = SelectedAssetUploadRepositorySerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        jawnuser = JawnUser.objects.get(base_user=self.request.user.id)
        return SelectedAssetUploadRepository.objects.filter(author=jawnuser)



class LazarusModProjectViewset(viewsets.ModelViewSet):
    serializer_class = LazarusModProjectSerializer
    queryset = LazarusModProject.objects.all()

class LazarusModAssetViewset(viewsets.ModelViewSet):
    serializer_class = LazarusModAssetSerializer
    queryset = LazarusModAsset.objects.all()

class LazarusModDependencyViewset(viewsets.ModelViewSet):
    serializer_class = LazarusModDependencySerializer
    queryset = LazarusModDependency.objects.all()


from rest_framework.parsers import FileUploadParser

class NewUploadDataTAView(APIView):
    parser_classes = (FileUploadParser,)
    def get(self, request, format=None):
        return HttpResponse('yes...')

class HPIUploadViewset(viewsets.ModelViewSet):
    serializer_class = HPIUploadSerializer
    queryset = HPIUpload.objects.all()



class TotalAnnihilationModViewset(viewsets.ModelViewSet):
    serializer_class = TotalAnnihilationModSerializer
    queryset = TotalAnnihilationMod.objects.all()





class SelectedAssetRepo(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):

        jawnuser = JawnUser.objects.get(base_user=request.user.id)
        queryset = SelectedAssetUploadRepository.objects.filter(author=jawnuser)

        list_response = []
        for item in queryset:
            dictionary = {}
            dictionary['id'] = item.id
            dictionary['name'] = item.name
            dictionary['description'] = item.description
            dictionary['created'] = item.created
            dictionary['author'] = item.author.id
            dictionary['is_selected'] = item.is_selected
            list_response.append(dictionary)

        final = {"results": list_response}
        return Response(final)



class SelectedModProjectsList(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):

        jawnuser = JawnUser.objects.get(base_user=request.user.id)
        queryset = LazarusModProject.objects.filter(created_by=jawnuser)

        list_response = []
        for item in queryset:
            dictionary = {}
            dictionary['id'] = item.id
            dictionary['name'] = item.name
            dictionary['description'] = item.description
            dictionary['created'] = item.created
            dictionary['created_by'] = item.created_by.id
            dictionary['is_selected'] = item.is_selected
            list_response.append(dictionary)

        final = {"results": list_response}
        return Response(final)


class SelectedModProject(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):

        jawnuser = JawnUser.objects.get(base_user=request.user.id)
        queryset = LazarusModProject.objects.filter(created_by=jawnuser)

        list_response = []
        for item in queryset:
            if item.is_selected == True:
                dictionary = {}
                dictionary['id'] = item.id
                dictionary['name'] = item.name
                dictionary['description'] = item.description
                dictionary['created'] = item.created
                dictionary['created_by'] = item.created_by.id
                dictionary['is_selected'] = item.is_selected
                list_response.append(dictionary)

        final = {"results": list_response}
        return Response(final)


class CommanderAccountView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        all_units = LazarusCommanderAccount.objects.all()
        serialized_obj = serializers.serialize("json", all_units)
        json_dict = json.loads(serialized_obj)
        list_response = []
        for item in json_dict:
            betterJson = item['fields']
            list_response.append(betterJson)
        return Response(list_response)

    def post(self, request, *args, **kwargs):
        faction = request.POST['faction']
        new_commander = LazarusCommanderAccount()
        new_commander.user = request.user
        new_commander.about_me = request.user
        new_commander.profile_pic = request.user
        new_commander.faction = faction

        new_commander.save()

        return Response('Welcome commander.')




class UnitFBIFromSQLView(APIView):
    permission_classes = (AllowAny,)
    def get(self, request, format=None):

        selected_mod = LazarusModProject()
        jawnuser = JawnUser.objects.get(base_user=request.user.id)
        queryset = LazarusModProject.objects.filter(created_by=jawnuser)
        for mod in queryset:
            if mod.is_selected == True:
                selected_mod = mod
                break

        list_response = []
        assets = LazarusModAsset.objects.filter(project_id=selected_mod.id)
        for asset in assets:
            asset_dependencies = LazarusModDependency.objects.filter(asset_id=asset.id)
            for dependency in asset_dependencies:
                if dependency.model_schema == 'UnitFbiData':
                    unitFbiSQL = UnitFbiData.objects.filter(id=dependency.model_id)
                    serialized_obj = serializers.serialize("json", unitFbiSQL)
                    json_dict = json.loads(serialized_obj)
                    json_dict[0]['fields']['ID'] = dependency.model_id
                    list_response.append(json_dict[0]['fields'])

        json_response = {
            'list_response': list_response,
            'mod': selected_mod.name,
            'total_units': len(list_response)
        }

        return Response(json_response)

        # all_units = UnitFbiData.objects.all()
        # serialized_obj = serializers.serialize("json", all_units)
        # json_dict = json.loads(serialized_obj)
        # list_response = []
        # for item in json_dict:
        #     betterJson = item['fields']
        #     list_response.append(betterJson)
        # return Response(list_response)


class WeaponTDFFromSQLView(APIView):
    permission_classes = (AllowAny,)
    def get(self, request, format=None):
        all_objs = WeaponTDF.objects.all()
        serialized_obj = serializers.serialize("json", all_objs)
        json_dict = json.loads(serialized_obj)
        list_response = []
        for item in json_dict:
            betterJson = item['fields']
            list_response.append(betterJson)
        return Response(list_response)


class DownloadTDFFromSQLView(APIView):
    permission_classes = (AllowAny,)
    def get(self, request, format=None):
        try:
            all_objs = DownloadTDF.objects.all()
            serialized_obj = serializers.serialize("json", all_objs)
            json_dict = json.loads(serialized_obj)
            list_response = []
            for item in json_dict:
                betterJson = item['fields']
                list_response.append(betterJson)
        except:
            return Response('Failed to find a parent unit for this TDF.')
        return Response(list_response)


class FeatureTDFFromSQLView(APIView):
    permission_classes = (AllowAny,)
    def get(self, request, format=None):
        all_objs = FeatureTDF.objects.all()
        serialized_obj = serializers.serialize("json", all_objs)
        json_dict = json.loads(serialized_obj)
        list_response = []
        for item in json_dict:
            betterJson = item['fields']
            list_response.append(betterJson)
        return Response(list_response)




#
#
# from django.shortcuts import render
# from dynamic_lazarus_page.models import AngularFuseApplication, NgIncludedHtml
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated, AllowAny
# from django.core import serializers
# import json
#
#
# all_apps = AngularFuseApplication.objects.all()
# serialized_obj = serializers.serialize("json", all_apps)
# json_dict = json.loads(serialized_obj)
# list_all_apps = []
#
#
#
#
# for item in all_apps:
#     print(item.name)
#     print('\n\n\n')
#     print(item.js_controller)
#     print('\n\n\n')
#
#
# all_ng_included_html = NgIncludedHtml.objects.all()
# for item in all_ng_included_html:
#     print(item.name)
#     print('\n\n\n')
#     print(item.contents)
#     print('\n\n\n')


