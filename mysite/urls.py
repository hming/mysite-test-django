from django.conf.urls.defaults import *
# from mysite import views
# Uncomment the next two lines to enable the admin:
from django.contrib import admin

# from mysite.contact import views as ss
admin.autodiscover()

urlpatterns = patterns('mysite.views',
   (r'^hello/$','hello'),
   (r'^time/$','current_datetime'),
   (r'^time/plus/(\d{1,2})/$','hours_ahead'),
   (r'^admin/', include(admin.site.urls)),
   (r'^meta/$','display_meta'),
   (r'^search-form/$', 'search_form'),
   (r'^search/$', 'search'),
)
urlpatterns += patterns('mysite.contact.views',
   (r'^contact/$','contact'),
   (r'^contact/thanks/$', 'thanks'),
)
 