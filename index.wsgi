#!/usr/bin/env python
import os
import sys

apache_configuration = os.path.dirname(__file__)
project = os.path.dirname(apache_configuration)
workspace = os.path.dirname(project)
sys.path.append(workspace)
sys.path.append("C:\Users\Nicolas-PC\pyproj\webdesk")
sys.path.append("C:\Users\Nicolas-PC\pyproj\webdesk\webdesk")

os.environ['DJANGO_SETTINGS_MODULE'] = 'webdesk.settings'
os.environ['PYTHON_EGG_CACHE'] = '/tmp'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler() 
