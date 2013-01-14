import sys,os
ROOT_PATH = os.path.dirname(__file__)
swapleaf_project = os.path.join(ROOT_PATH, 'swapleaf')
sys.path.append(swapleaf_project)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from django.contrib.sites.models import Site
try:
	site = Site.objects.get(pk=1)
except Site.DoesNotExist:
	new_site = Site.objects.create(domain='swapleaf.com', name='swapleaf')

from django.contrib.auth.models import User
a = User.objects.get(id=1)
a.is_staff = True
a.is_superuser = True
a.first_name = 'Admin'
a.last_name = " Dang Nguyen"
a.save()
	
print "Fix DB successfully"