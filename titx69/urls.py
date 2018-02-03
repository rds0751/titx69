"""oscardemo URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from oscar.app import application
from django.conf import settings
from django.conf.urls.static import static
from django.views.i18n import javascript_catalog
from oscar.app import shop
from stores.app import application as stores_app
from stores.dashboard.app import application as dashboard_app


urlpatterns = [
    url(r'^i18n/', include('django.conf.urls.i18n')),
    # django admin is not officially supported by oscar - you should use the dashboard instead
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include(application.urls)),

    # adds URLs for the dashboard store manager
    url(r'^dashboard/stores/', dashboard_app.urls),

    # adds URLs for overview and detail pages
    url(r'^stores/', stores_app.urls),

    # adds internationalization URLs
    (r'^jsi18n/$', javascript_catalog, name="javascript-catalogue"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)