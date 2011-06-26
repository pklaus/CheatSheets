#!/usr/bin/env python
# -*- encoding: UTF8 -*-

"""
Generate the Cheat Sheets as HTML from the Markdown input.
"""

TEMPLATES_FOLDER = 'templates'
CSS_FOLDER = TEMPLATES_FOLDER+'/css'
OUTPUT_DIRECTORY = 'generated_html'
INPUT_DIRECTORY = 'cheatsheets_markdown'

import sys
def show_requirements(missing_module):
    print "Your python installation is missing the module", missing_module
    print "To get all dependencies on Ubuntu/Debian run:"
    print "sudo aptitude install python-django python-markdown"
    print "On Mac OS X you need:"
    print "easy_install django; easy_install Markdown"

# to use the django template engine without a proper django project we have to setup the django settings
# according to http://docs.djangoproject.com/en/dev/topics/settings/#settings-without-django-settings-module
try:
    from django.conf import settings
    from django.template import TemplateSyntaxError, loader
except:
    show_requirements("django")
    sys.exit(1)

settings.configure(DEBUG=True, 
    TEMPLATE_DEBUG=True,
    INSTALLED_APPS=('django.contrib.markup',),
    TEMPLATE_DIRS = ( "templates", ),
)

from django.template import Context, Template # for the template engine
import os # for os.listdir()
from distutils.dir_util import copy_tree
import re # for regular expression matching of the scriptnames in the directory
import pdb # for debugging using pdb.set_trace()
import datetime


def main():
    path = os.path.dirname( os.path.realpath( __file__ ) )+'/'+INPUT_DIRECTORY

    cheatsheets,cheatsheets_list = [],[]
    dir_list = os.listdir(path)
    for fname in dir_list:
        if re.search('.mkd$',fname) != None or re.search('.md$',fname) != None or re.search('.markdown$',fname) != None:
            cheatsheets_list.append(fname)

    for cheatsheet_name in cheatsheets_list:
        cheatsheet_file = open(path+'/'+cheatsheet_name,'r')
        content = cheatsheet_file.read()
        cheatsheets.append({ 'url':  cheatsheet_name+'.html',
                             'name': cheatsheet_name.replace('.md','') })
        output_file_handle = open(OUTPUT_DIRECTORY+'/'+cheatsheet_name+'.html','w')
        try:
            output_file_handle.write(loader.render_to_string('cheatsheet.html', { 'title': cheatsheet_name, 'cheatsheet_markdown': content}))
        except TemplateSyntaxError:
            show_requirements("markdown")
            sys.exit(1)

    output_file_handle = open(OUTPUT_DIRECTORY+'/'+'index.html','w')
    output_file_handle.write(loader.render_to_string('index.html',{ 'title': 'Cheat Sheets for Free', 'cheatsheets': cheatsheets, }))

    copy_tree( CSS_FOLDER, OUTPUT_DIRECTORY+'/css')
    print "Finished creating the HTML versions of the Markdown Cheat Sheets."

if __name__ == '__main__':
    main()
