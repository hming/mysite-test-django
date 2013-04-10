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
   (r'^my_image$','my_image'),
   (r'^csv$','unruly_passengers_csv'),
   (r'^show_color/$','show_color'),
   (r'^set_color/$','set_color'),
)
urlpatterns += patterns('mysite.contact.views',
   (r'^contact/$','contact'),
   (r'^contact/thanks/$', 'thanks'),
)
 