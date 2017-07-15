from django.db import models
# GeneralWebsiteInfo
from django.contrib.auth.models import User


MAIN_LAYOUT_DEFAULT = '<div layout="row" layout-align="start center">    <div layout="row" layout-align="start center" flex>        <md-button id="navigation-toggle" class="md-icon-button" ng-click="vm.toggleSidenav(\'navigation\')"                   hide-gt-sm aria-label="Toggle navigation" translate                   translate-attr-aria-label="TOOLBAR.TOGGLE_NAVIGATION">            <md-icon md-font-icon="icon-menu" class="icon"></md-icon>        </md-button>        <ms-shortcuts></ms-shortcuts>        <div class="toolbar-separator"></div>    </div>    <div layout="row" layout-align="start center">                <md-progress-circular id="toolbar-progress" ng-disabled="!$root.loadingProgress"  class="md-accent" md-diameter="32">        </md-progress-circular>                <div class="toolbar-separator"></div>        <md-menu-bar id="user-menu">            <md-menu md-position-mode="left bottom">                <md-button class="user-button" ng-click="$mdOpenMenu()"                           aria-label="User settings"                           translate translate-attr-aria-label="TOOLBAR.USER_SETTINGS">                    <div layout="row" layout-align="space-between center">                        <div class="avatar-wrapper">                            <img md-menu-align-target class="avatar" src="/static/assets/images/avatars/profile.jpg">                            <md-icon md-font-icon ng-class="vm.userStatus.icon"                                     ng-style="{\'color\': vm.userStatus.color }"                                     class="icon status s16">                            </md-icon>                        </div>                        <span class="username" hide show-gt-sm>DJANGULAR_USERNAME</span>                        <md-icon md-font-icon="icon-chevron-down"                                 class="icon s16" hide-xs></md-icon>                    </div>                </md-button>                <md-menu-content width="3">                    <md-menu-item class="md-indent" ui-sref="app.pages_profile">                        <md-icon md-font-icon="icon-account" class="icon"></md-icon>                        <md-button>My Profile</md-button>                    </md-menu-item><!--                    <md-menu-item class="md-indent" ui-sref="app.mail">                        <md-icon md-font-icon="icon-email" class="icon"></md-icon>                        <md-button>Inbox</md-button>                    </md-menu-item>                    <md-menu-item class="md-indent">                        <md-icon md-font-icon ng-class="vm.userStatus.icon"                                 ng-style="{\'color\': vm.userStatus.color }" class="icon"></md-icon>                        <md-menu id="user-status-menu">                            <md-button ng-click="$mdOpenMenu()" class="status" ng-class="vm.userStatus.class">                                {{vm.userStatus.title}}                            </md-button>                            <md-menu-content width="2">                                <md-menu-item class="status md-indent"                                              ng-class="{\'selected\': status === vm.userStatus}"                                              ng-repeat="status in vm.userStatusOptions">                                    <md-icon md-font-icon="{{status.icon}}" ng-style="{\'color\': status.color }"                                             class="icon"></md-icon>                                    <md-button ng-click="vm.setUserStatus(status)">                                        {{status.title}}                                    </md-button>                                </md-menu-item>                            </md-menu-content>                        </md-menu>                    </md-menu-item>-->                    <md-menu-divider></md-menu-divider>                    <md-menu-item class="md-indent">                        <md-icon md-font-icon="icon-logout" class="icon"></md-icon>                        <md-button ng-click="vm.logout()">Logout</md-button>                    </md-menu-item>                </md-menu-content>            </md-menu>        </md-menu-bar>                <div class="toolbar-separator"></div>        <!--        <ms-search-bar on-search="vm.search(query)" on-result-click="vm.searchResultClick(item)" debounce="300"></ms-search-bar>        <div class="toolbar-separator"></div>        <md-menu id="language-menu" md-offset="0 72" md-position-mode="target-right target">            <md-button class="language-button" ng-click="$mdOpenMenu()"                       aria-label="Language" md-menu-origin md-menu-align-target>                <div layout="row" layout-align="center center">                    <img class="flag" ng-src="/static/assets/images/flags/{{vm.selectedLanguage.flag}}.png">                    <span class="iso">{{vm.selectedLanguage.code}}</span>                </div>            </md-button>            <md-menu-content width="3" id="language-menu-content">                <md-menu-item ng-repeat="(iso, lang) in vm.languages">                    <md-button ng-click="vm.changeLanguage(lang)" aria-label="{{lang.title}}" translate                               translate-attr-aria-label="{{lang.title}}">                        <span layout="row" layout-align="start center">                            <img class="flag" ng-src="/static/assets/images/flags/{{lang.flag}}.png">                            <span translate="{{lang.translation}}">{{lang.title}}</span>                        </span>                    </md-button>                </md-menu-item>            </md-menu-content>        </md-menu>        <div class="toolbar-separator"></div>        <md-button id="quick-panel-toggle" class="md-icon-button" ng-click="vm.toggleSidenav(\'quick-panel\')"                   aria-label="Toggle quick panel" translate translate-attr-aria-label="TOOLBAR.TOGGLE_QUICK_PANEL">            <md-icon md-font-icon="icon-format-list-bulleted" class="icon"></md-icon>        </md-button>        -->    </div></div>'
DEFAULT_LOADER = '<ms-splash-screen id="splash-screen">\n\t <div class="center">\n\t\t <div class="logo" style="width:250px; font-size: 36px; background-color: darkorange;">\n\t\t <span>Lazarus</span>\n\t\t </div>\n <!-- Material Design Spinner --> \n<div class="spinner-wrapper"> \n<div class="spinner"> \n<div class="inner"> \n<div class="gap"></div> \n<div class="left"> \n<div class="half-circle"></div> </div> \n<div class="right"> \n<div class="half-circle"></div> </div> </div> </div> </div> <!-- / Material Design Spinner --> </div></ms-splash-screen>'

DEFAULT_NAVBAR_LOGO_HTML = ''
DEFAULT_COLOR_THEME_CSS = ''
DEFAULT_BOOT_SCREEN_HTML = ''

BASIC_INFO_TYPE = (
    ('BOOT_SCREEN_HTML', 'Boot Screen Html'),
    ('NAVBAR_TITLE', 'Nav Bar Title'),
    ('NAVBAR_LOGO', 'Nav Bar Logo Html'),
    ('COLOR_THEME', 'Color Palette'),
    ('LAYOUT_STYLE', 'Layout Style'),
    ('LAYOUT_MODE', 'Layout Mode'),
)
class WebsiteColorTheme(models.Model):
    name = models.CharField(max_length=255, default='default', unique=True)
    css_code = models.TextField()
    enabled = models.BooleanField(default=True,
                                  help_text='check to enable this, only one item is allowed to be enabled')


LAYOUT_CHOICES_MAIN = (
    ('BOOT_SCREEN_HTML', 'Vertical Navigation'),
    ('NAVBAR_TITLE', 'Vertical Navigation Full Width Toolbar'),
    ('NAVBAR_LOGO', ''),
    ('COLOR_THEME', ''),
    ('LAYOUT_STYLE', ''),
    ('LAYOUT_MODE', ''),
)
class WebsiteLayout(models.Model):
    name = models.CharField(max_length=255, default='default_layout', unique=True)
    main_layout_html = models.TextField(default=MAIN_LAYOUT_DEFAULT)
    toolbar_html = models.TextField()
    navigation_html = models.TextField()
    enabled = models.BooleanField(default=True,
                                  help_text='check to enable this, only one item is allowed to be enabled')

class NavigationBar(models.Model):
    name = models.CharField(max_length=255, default='default_layout', help_text='', unique=True)
    title = models.CharField(max_length=55, default='Djangular')
    logo_html_code = models.TextField()
    enabled = models.BooleanField(default=True,
                                  help_text='check to enable this, only one item is allowed to be enabled')

class BootScreenLoader(models.Model):
    name = models.CharField(max_length=255, default='default_layout', unique=True)

    title = models.CharField(max_length=255, default='Djangular Lazarus')
    width = models.IntegerField(default=250)
    font_size = models.IntegerField(default=36)

    logo_background_color = models.CharField(max_length=255, default='white', help_text='"blue", "aqua", "white", etc...')
    font_color = models.CharField(max_length=255, default='black', help_text='"blue", "aqua", "white", etc...')
    main_background_color = models.CharField(max_length=255, default='darkolivegreen', help_text='"blue", "aqua", "white", etc...')

    spinner_color = models.CharField(max_length=255, default='antiquewhite')

    html_code = models.TextField(default=DEFAULT_LOADER)
    enabled = models.BooleanField(default=True, help_text='check to enable this, only one item is allowed to be enabled')


class PressArticle(models.Model):
    title = models.CharField(max_length=255, default='default')
    description = models.CharField(max_length=255, default='default', null=True, blank=True)
    seo_meta_data = models.CharField(max_length=255, default='default', help_text='Search engine optimization keywords.', null=True, blank=True)
    author = models.ForeignKey(User, unique=True)
    pub_date = models.DateTimeField(auto_created=True)
    body = models.TextField()
    media = models.TextField(null=True, blank=True)



