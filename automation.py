import os
import time
import argparse
import subprocess as sp

# cmd:  python3 automation.py project_name

def execute(args):
    get_file = lambda x:'wget -q https://raw.githubusercontent.com/goutham9032/Misc/master/django_misc/%s'%(x)

    # install dependencies
    os.popen('rm -r requirements.txt')
    os.popen(get_file('requirements.txt')).read()
    os.popen('pip3 install -r requirements.txt').read()

    # create project
    del_proj_dir = 'rm -rf %s'%(args.project_name)
    proj_cmd = 'django-admin startproject %s'%(args.project_name)
    app_cmd = 'django-admin startapp %s'%(args.app_name)

    os.popen(del_proj_dir).read()
    os.popen(proj_cmd).read()
    time.sleep(2)

    # create app
    proj_dir = '%s/%s'%(os.getcwd(), args.project_name)
    os.chdir(proj_dir)
    os.popen(app_cmd).read()

    # create templates & static folder and include base files
    os.popen('mkdir templates').read()
    os.popen('mkdir static').read()
    time.sleep(2)
    os.chdir(proj_dir + '/static')
    os.popen('mkdir css').read()
    os.popen('mkdir js').read()
    os.chdir(proj_dir + '/templates')
    os.popen(get_file('base.html')).read()
    os.popen(get_file('home.html')).read()
    os.chdir(proj_dir + '/static/css/')
    os.popen(get_file('home.css')).read()
    os.chdir(proj_dir + '/static/js/')
    os.popen(get_file('main.js')).read()

    # import local settings
    os.chdir(proj_dir + '/%s'%(args.project_name))
    os.popen(get_file('local_settings.py')).read()
    os.popen("echo 'from %s.local_settings import *' >> settings.py"%(args.project_name)).read()

    # import urls and views
    os.popen('rm -r urls.py')
    os.popen(get_file('urls.py'))
    os.chdir(proj_dir + '/%s/'%(args.app_name))
    os.popen(get_file('app_urls.py'))
    os.popen('rm views.py')
    os.popen(get_file('views.py'))

    # run manually makemigations, migrate, runserver

def define_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-project", "--project_name", type=str, default="test_django_project",
                        help="name of the project to create in django")
    parser.add_argument("-app", "--app_name", type=str, default="app",
                        help="name of the app in django")

    args = parser.parse_args()
    return args

args = define_args()
execute(args)



