from django.conf.urls import url
from lazarus import views

urlpatterns = [


    # url(r'^listWorkingDirectory/$', views.listWorkingDirectory.as_view(), name='listWorkingDirectory'),
    url(r'^main/$', views.CustomHtmlGenerator.as_view(), name='index'),
    # url(r'^convert_to_png', views.convertPcxToPng.as_view(), name='convertPcxToPng'),


    # url(r'^ram/$', views.getRam.as_view(), name='ram'),
    # url(r'^processes/$', views.getProcesses.as_view(), name='processes'),
    # url(r'^processesDummy/$', views.getProcessesDummy.as_view(), name='processesDummy'),
    # url(r'^storage/$', views.getStorage.as_view(), name='storage'),
    # url(r'^cpuinfo/$', views.getCPUInfo.as_view(), name='cpuinfo'),
    # url(r'^uptime/$', views.getUpTime.as_view(), name='uptime'),
# getProcessesDummy
]
