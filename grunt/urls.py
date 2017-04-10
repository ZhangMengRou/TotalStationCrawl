"""grunt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from grunt import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.index),
    url(r'^frequently-asked-questions',views.grunt_frequently_asked_questions),
    url(r'^api/grunt.option',views.grunt_api_grunt_option),
    url(r'^blog/2016-02-11-grunt-1.0.0-rc1-released',views.grunt_blog_2016_02_11_grunt_1_0_0_rc1_released),
    url(r'^creating-tasks',views.grunt_creating_tasks),
    url(r'^2013-03-13-grunt-0.4.1-released',views.grunt_2013_03_13_grunt_0_4_1_released),
    url(r'^2013-02-15-updating-plugins-to-grunt-0.4',views.grunt_2013_02_15_updating_plugins_to_grunt_0_4),
    url(r'^upgrading-from-0.3-to-0.4',views.grunt_upgrading_from_0_3_to_0_4),
    url(r'^index',views.grunt_index),
    url(r'^blog/2014-03-14-grunt-0.4.4-released',views.grunt_blog_2014_03_14_grunt_0_4_4_released),
    url(r'^grunt.template',views.grunt_grunt_template),
    url(r'^grunt',views.grunt_grunt),
    url(r'^cdn-cgi/l/email-protection',views.grunt_cdn_cgi_l_email_protection),
    url(r'^grunt.log',views.grunt_grunt_log),
    url(r'^blog/2013-02-15-updating-plugins-to-grunt-0.4',views.grunt_blog_2013_02_15_updating_plugins_to_grunt_0_4),
    url(r'^api/grunt.task',views.grunt_api_grunt_task),
    url(r'^built-with-grunt-badge',views.grunt_built_with_grunt_badge),
    url(r'^using-the-cli',views.grunt_using_the_cli),
    url(r'^project-scaffolding',views.grunt_project_scaffolding),
    url(r'^blog/2013-03-13-grunt-0.4.1-released',views.grunt_blog_2013_03_13_grunt_0_4_1_released),
    url(r'^contrib',views.grunt_contrib),
    url(r'^api/grunt',views.grunt_api_grunt),
    url(r'^www.gruntjs.net',views.grunt_www_gruntjs_net),
    url(r'^api/inside-tasks',views.grunt_api_inside_tasks),
    url(r'^api/grunt.file',views.grunt_api_grunt_file),
    url(r'^grunt.util',views.grunt_grunt_util),
    url(r'^upgrading-from-0.4-to-1.0',views.grunt_upgrading_from_0_4_to_1_0),
    url(r'^2016-04-04-grunt-1.0.0-released',views.grunt_2016_04_04_grunt_1_0_0_released),
    url(r'^inside-tasks',views.grunt_inside_tasks),
    url(r'^grunt.task',views.grunt_grunt_task),
    url(r'^contributing',views.grunt_contributing),
    url(r'^grunt.file',views.grunt_grunt_file),
    url(r'^rss',views.grunt_rss),
    url(r'^plugins/contrib',views.grunt_plugins_contrib),
    url(r'^configuring-tasks',views.grunt_configuring_tasks),
    url(r'^api/grunt.fail',views.grunt_api_grunt_fail),
    url(r'^email-protection',views.grunt_email_protection),
    url(r'^blog',views.grunt_blog),
    url(r'^api/',views.grunt_api),
    url(r'^api/grunt.event',views.grunt_api_grunt_event),
    url(r'^2013-11-21-grunt-0.4.2-released',views.grunt_2013_11_21_grunt_0_4_2_released),
    url(r'^plugins',views.grunt_plugins),
    url(r'^exit-codes',views.grunt_exit_codes),
    url(r'^creating-plugins',views.grunt_creating_plugins),
    url(r'^2014-03-14-grunt-0.4.4-released',views.grunt_2014_03_14_grunt_0_4_4_released),
    url(r'^2014-05-12-grunt-0.4.5-released',views.grunt_2014_05_12_grunt_0_4_5_released),
    url(r'^development-team',views.grunt_development_team),
    url(r'^getting-started',views.grunt_getting_started),
    url(r'^blog/2013-11-21-grunt-0.4.2-released',views.grunt_blog_2013_11_21_grunt_0_4_2_released),
    url(r'^api/grunt.util',views.grunt_api_grunt_util),
    url(r'^who-uses-grunt',views.grunt_who_uses_grunt),
    url(r'^blog/2016-04-04-grunt-1.0.0-released',views.grunt_blog_2016_04_04_grunt_1_0_0_released),
    url(r'^grunt.config',views.grunt_grunt_config),
    url(r'^grunt.event',views.grunt_grunt_event),
    url(r'^2016-02-11-grunt-1.0.0-rc1-released',views.grunt_2016_02_11_grunt_1_0_0_rc1_released),
    url(r'^grunt.fail',views.grunt_grunt_fail),
    url(r'^blog/2014-03-07-grunt-0.4.3-released',views.grunt_blog_2014_03_07_grunt_0_4_3_released),
    url(r'^help-resources',views.grunt_help_resources),
    url(r'^api/grunt.config',views.grunt_api_grunt_config),
    url(r'^installing-grunt',views.grunt_installing_grunt),
    url(r'^api/grunt.log',views.grunt_api_grunt_log),
    url(r'^sample-gruntfile',views.grunt_sample_gruntfile),
    url(r'^api/exit-codes',views.grunt_api_exit_codes),
    url(r'^blog/2014-05-12-grunt-0.4.5-released',views.grunt_blog_2014_05_12_grunt_0_4_5_released),
    url(r'^api/grunt.template',views.grunt_api_grunt_template),
    url(r'^blog/2013-02-18-grunt-0.4.0-released',views.grunt_blog_2013_02_18_grunt_0_4_0_released),
    url(r'^grunt.option',views.grunt_grunt_option),
    url(r'^2014-03-07-grunt-0.4.3-released',views.grunt_2014_03_07_grunt_0_4_3_released),
    url(r'^2013-02-18-grunt-0.4.0-released',views.grunt_2013_02_18_grunt_0_4_0_released)


]
