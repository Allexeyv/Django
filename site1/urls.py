from django.conf.urls import include, url
from django.contrib import admin
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'attractions', views.AttractionsViewSet)
router.register(r'towns', views.TownsViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^search/$', views.search, name='search'),
    url(r'^pages/(.+)$', views.pages, name='pages'),
    url(r'^my_cart/$', views.my_cart),
    url(r'^add_to_cart/(.+)$', views.add_to_cart),
    url(r'^order/$', views.order),
    url(r'^$', views.index, name='index'),

    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls'))
]



