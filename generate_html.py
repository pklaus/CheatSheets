#!/usr/bin/env python
# -*- encoding: UTF8 -*-

"""
Generate the Cheat Sheets as HTML from the Markdown input.
"""

CHEATSHEET_TEMPLATE='templates/cheatsheet.html'
INDEX_TEMPLATE='templates/index.html'
OUTPUT_DIRECTORY='generated_html'
INPUT_DIRECTORY='cheatsheets_markdown'

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
    from django.template import TemplateSyntaxError
except:
    show_requirements("django")
    sys.exit(1)

settings.configure(DEBUG=True, 
    TEMPLATE_DEBUG=True,
    INSTALLED_APPS=('django.contrib.markup',))

from django.template import Context, Template # for the template engine

import os # for os.listdir()

import re # for regular expression matching of the scriptnames in the directory

import pdb # for debugging using pdb.set_trace()

import datetime


def main():
    path = os.path.dirname( os.path.realpath( __file__ ) )+'/'+INPUT_DIRECTORY

    template_file_handle = open(CHEATSHEET_TEMPLATE,'r')
    t = Template(template_file_handle.read())
    
    cheatsheets,cheatsheets_list = [],[]
    dir_list = os.listdir(path)
    for fname in dir_list:
        if re.search('.mkd$',fname) != None or re.search('.md$',fname) != None or re.search('.markdown$',fname) != None:
            cheatsheets_list.append(fname)

    for cheatsheet_name in cheatsheets_list:
        cheatsheet_file = open(path+'/'+cheatsheet_name,'r')
        content = cheatsheet_file.read()
        cheatsheets.append({ 'url':  cheatsheet_name+'.html',
                             'name': cheatsheet_name })
        c = Context({ 'title': cheatsheet_name,
                      'cheatsheet_markdown': content,})
        output_file_handle = open(OUTPUT_DIRECTORY+'/'+cheatsheet_name+'.html','w')
        #try:
        output_file_handle.write(t.render(c))
        #except TemplateSyntaxError:
        #    show_requirements("markdown")
        #    sys.exit(1)

    t = Template(open(INDEX_TEMPLATE,'r').read())
    output_file_handle = open(OUTPUT_DIRECTORY+'/'+'index.html','w')
    c = Context({ 'cheatsheets': cheatsheets, })
    output_file_handle.write(t.render(c))
    print "Finished creating the HTML versions of the Markdown Cheat Sheets."

def parse_description(file_handle):
    description = ''
    start = file_handle.readline()
    p = re.compile('""".*?"""|\'\'\'.*?\'\'\'', re.DOTALL)
    if re.match('#!',start) != None: # search for shebang
        start = file_handle.readline()
    if re.search('encoding',start) != None: # seems to be a python file
        start = file_handle.readline()
        input_text = file_handle.read()
        search = p.search(input_text)
        if search != None:
            description = search.group().replace('"""','').replace("'''",'')
    while start == '\n' or len(start)>0 and start[0]=='#':
        while start == '\n':
            start = file_handle.readline()
        while re.match('#',start):
            description += start.replace('#','')
            start = file_handle.readline()
    return description

if __name__ == '__main__':
    main()
