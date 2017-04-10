# coding=utf-8
import sys

from django.shortcuts import render

default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)


def index(request):
    return render(request, 'html/index.html')


def grunt_frequently_asked_questions(request):
    return render(request, 'html/frequently-asked-questions.html')


def grunt_api_grunt_option(request):
    return render(request, 'html/api_grunt.option.html')


def grunt_blog_2016_02_11_grunt_1_0_0_rc1_released(request):
    return render(request, 'html/blog_2016-02-11-grunt-1.0.0-rc1-released.html')


def grunt_creating_tasks(request):
    return render(request, 'html/creating-tasks.html')


def grunt_2013_03_13_grunt_0_4_1_released(request):
    return render(request, 'html/2013-03-13-grunt-0.4.1-released.html')


def grunt_2013_02_15_updating_plugins_to_grunt_0_4(request):
    return render(request, 'html/2013-02-15-updating-plugins-to-grunt-0.4.html')


def grunt_upgrading_from_0_3_to_0_4(request):
    return render(request, 'html/upgrading-from-0.3-to-0.4.html')


def grunt_index(request):
    return render(request, 'html/index.html')


def grunt_blog_2014_03_14_grunt_0_4_4_released(request):
    return render(request, 'html/blog_2014-03-14-grunt-0.4.4-released.html')


def grunt_grunt_template(request):
    return render(request, 'html/grunt.template.html')


def grunt_grunt(request):
    return render(request, 'html/grunt.html')


def grunt_cdn_cgi_l_email_protection(request):
    return render(request, 'html/cdn-cgi_l_email-protection.html')


def grunt_grunt_log(request):
    return render(request, 'html/grunt.log.html')


def grunt_blog_2013_02_15_updating_plugins_to_grunt_0_4(request):
    return render(request, 'html/blog_2013-02-15-updating-plugins-to-grunt-0.4.html')


def grunt_api_grunt_task(request):
    return render(request, 'html/api_grunt.task.html')


def grunt_built_with_grunt_badge(request):
    return render(request, 'html/built-with-grunt-badge.html')


def grunt_using_the_cli(request):
    return render(request, 'html/using-the-cli.html')


def grunt_project_scaffolding(request):
    return render(request, 'html/project-scaffolding.html')


def grunt_blog_2013_03_13_grunt_0_4_1_released(request):
    return render(request, 'html/blog_2013-03-13-grunt-0.4.1-released.html')


def grunt_contrib(request):
    return render(request, 'html/contrib.html')


def grunt_api_grunt(request):
    return render(request, 'html/api_grunt.html')


def grunt_www_gruntjs_net(request):
    return render(request, 'html/www.gruntjs.net.html')


def grunt_api_inside_tasks(request):
    return render(request, 'html/api_inside-tasks.html')


def grunt_api_grunt_file(request):
    return render(request, 'html/api_grunt.file.html')


def grunt_grunt_util(request):
    return render(request, 'html/grunt.util.html')


def grunt_upgrading_from_0_4_to_1_0(request):
    return render(request, 'html/upgrading-from-0.4-to-1.0.html')


def grunt_2016_04_04_grunt_1_0_0_released(request):
    return render(request, 'html/2016-04-04-grunt-1.0.0-released.html')


def grunt_inside_tasks(request):
    return render(request, 'html/inside-tasks.html')


def grunt_grunt_task(request):
    return render(request, 'html/grunt.task.html')


def grunt_contributing(request):
    return render(request, 'html/contributing.html')


def grunt_grunt_file(request):
    return render(request, 'html/grunt.file.html')


def grunt_rss(request):
    return render(request, 'html/rss.html')


def grunt_plugins_contrib(request):
    return render(request, 'html/plugins_contrib.html')


def grunt_configuring_tasks(request):
    return render(request, 'html/configuring-tasks.html')


def grunt_api_grunt_fail(request):
    return render(request, 'html/api_grunt.fail.html')


def grunt_email_protection(request):
    return render(request, 'html/email-protection.html')


def grunt_blog(request):
    return render(request, 'html/blog.html')


def grunt_api(request):
    return render(request, 'html/api.html')


def grunt_api_grunt_event(request):
    return render(request, 'html/api_grunt.event.html')


def grunt_2013_11_21_grunt_0_4_2_released(request):
    return render(request, 'html/2013-11-21-grunt-0.4.2-released.html')


def grunt_plugins(request):
    return render(request, 'html/plugins.html')


def grunt_exit_codes(request):
    return render(request, 'html/exit-codes.html')


def grunt_creating_plugins(request):
    return render(request, 'html/creating-plugins.html')


def grunt_2014_03_14_grunt_0_4_4_released(request):
    return render(request, 'html/2014-03-14-grunt-0.4.4-released.html')


def grunt_2014_05_12_grunt_0_4_5_released(request):
    return render(request, 'html/2014-05-12-grunt-0.4.5-released.html')


def grunt_development_team(request):
    return render(request, 'html/development-team.html')


def grunt_getting_started(request):
    return render(request, 'html/getting-started.html')


def grunt_blog_2013_11_21_grunt_0_4_2_released(request):
    return render(request, 'html/blog_2013-11-21-grunt-0.4.2-released.html')


def grunt_api_grunt_util(request):
    return render(request, 'html/api_grunt.util.html')


def grunt_who_uses_grunt(request):
    return render(request, 'html/who-uses-grunt.html')


def grunt_blog_2016_04_04_grunt_1_0_0_released(request):
    return render(request, 'html/blog_2016-04-04-grunt-1.0.0-released.html')


def grunt_grunt_config(request):
    return render(request, 'html/grunt.config.html')


def grunt_grunt_event(request):
    return render(request, 'html/grunt.event.html')


def grunt_2016_02_11_grunt_1_0_0_rc1_released(request):
    return render(request, 'html/2016-02-11-grunt-1.0.0-rc1-released.html')


def grunt_grunt_fail(request):
    return render(request, 'html/grunt.fail.html')


def grunt_blog_2014_03_07_grunt_0_4_3_released(request):
    return render(request, 'html/blog_2014-03-07-grunt-0.4.3-released.html')


def grunt_help_resources(request):
    return render(request, 'html/help-resources.html')


def grunt_api_grunt_config(request):
    return render(request, 'html/api_grunt.config.html')


def grunt_installing_grunt(request):
    return render(request, 'html/installing-grunt.html')


def grunt_api_grunt_log(request):
    return render(request, 'html/api_grunt.log.html')


def grunt_sample_gruntfile(request):
    return render(request, 'html/sample-gruntfile.html')


def grunt_api_exit_codes(request):
    return render(request, 'html/api_exit-codes.html')


def grunt_blog_2014_05_12_grunt_0_4_5_released(request):
    return render(request, 'html/blog_2014-05-12-grunt-0.4.5-released.html')


def grunt_api_grunt_template(request):
    return render(request, 'html/api_grunt.template.html')


def grunt_blog_2013_02_18_grunt_0_4_0_released(request):
    return render(request, 'html/blog_2013-02-18-grunt-0.4.0-released.html')


def grunt_grunt_option(request):
    return render(request, 'html/grunt.option.html')


def grunt_2014_03_07_grunt_0_4_3_released(request):
    return render(request, 'html/2014-03-07-grunt-0.4.3-released.html')


def grunt_2013_02_18_grunt_0_4_0_released(request):
    return render(request, 'html/2013-02-18-grunt-0.4.0-released.html')


def about(request):
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'boldmessage': "I am bold font from the context"}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.

    return render(request, 'one/about.html', context_dict)
