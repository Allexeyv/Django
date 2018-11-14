from django.conf.urls import include, url
from django.contrib import admin
from project_app import views
from rest_framework import routers
from graphene_django.views import GraphQLView

router = routers.DefaultRouter()
router.register(r'attraction', views.AttractionViewSet)
router.register(r'town', views.TownViewSet)
router.register(r'order', views.OrderViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^graphql', GraphQLView.as_view(graphiql=True)),
]