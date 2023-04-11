from graphene_django.views import GraphQLView

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("home.urls")),
    path("graphql/", csrf_exempt(GraphQLView.as_view(graphiql=True))),
    path("", include("products.urls")),
    path("", include("accounts.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
