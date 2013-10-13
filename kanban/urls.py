from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from rest_framework import routers

from principal.views import GrupoViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r'grupos', GrupoViewSet)
router.register(r'usuarios', UserViewSet)

urlpatterns = patterns('',
    # Examples:
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url(r'^$', 'kanban.views.home', name='home'),
    # url(r'^kanban/', include('kanban.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
