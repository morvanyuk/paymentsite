"""paymentsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from paymentsite import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include
from pay.views import payment, contacts, home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contacts/', contacts.as_view(), name='contacts'),
    path('payment/', payment.as_view(), name='payment'),
    path("", home.as_view(), name='home'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
