from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.static import serve
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.authtoken.views import obtain_auth_token

from orders.views import stripe_webhook_view
from products.views import IndexView

static_urlpatterns = [
    re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
    re_path(r"^static/(?P<path>.*)$", serve, {"document_root": settings.STATIC_ROOT}),
]

schema_view = get_schema_view(
    openapi.Info(
        title="Books API",
        default_version='v1',
        description='Документация для проекта BookForCoders',
        contact=openapi.Contact(email='alberv0r@yandex.ru'),
        license=openapi.License(name="BSD License"),),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(static_urlpatterns)),
    path('', IndexView.as_view(), name='index'),
    path('products/', include('products.urls', namespace='products')),
    path('users/', include('users.urls', namespace='users')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('accounts/', include('allauth.urls')),
    path('webhooks/stripe/', stripe_webhook_view, name='stripe-webhook'),
    path('api/', include('api.urls', namespace='api')),
    path('api-token-auth/', obtain_auth_token),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]


if settings.DEBUG:
    urlpatterns.append(path('__debug__/', include('debug_toolbar.urls')))
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
