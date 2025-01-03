"""
URL configuration for mpgstone project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mpgstoneuk.views import frontpage, shop, product, product_detail, category_detail, aboutus,dynamic_page
from django.conf import settings
from django.conf.urls.static import static
# from . import views

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('about-us/', aboutus, name='aboutus'),
    path('shop/', shop, name='shop'),
    # path('categories/<slug:category_slug>/', shop, name='shop'),
    path('product/', product, name='product'),
    # path('product/<int:pk>/', product_detail, name='product_detail'),
    path('categories/<slug:category_slug>/', category_detail, name='category_detail'),
    path('product/<slug:category_slug>/<slug:product_slug>/', product_detail, name='product_detail'),
    path('<slug:slug>/', dynamic_page, name='dynamic_page'),
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)