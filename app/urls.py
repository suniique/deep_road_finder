"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from rest_framework.routers import SimpleRouter

from app.index import views as index_view
from app.train_plan import views as train_plan_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', index_view.index_page)
]

router = SimpleRouter()
router.register('api/plan', train_plan_view.PlanEdit)
router.register('api/trial', train_plan_view.TrialEdit)

urlpatterns += router.urls
