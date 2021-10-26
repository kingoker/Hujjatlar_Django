import os
import sys

sys.path.append('/home/c/ci79299/KingDesign/public_html')
sys.path.append('/home/c/ci79299/myenv/lib/python3.6/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'KingDesign.settings'
import django
django.setup()

from django.core.handlers import wsgi
application = wsgi.WSGIHandler()
