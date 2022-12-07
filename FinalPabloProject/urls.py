from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView  # new


urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path("accounts/", include("accounts.urls")),  # new
    path("accounts/", include("django.contrib.auth.urls")),  # new
    path('', TemplateView.as_view(template_name='home.html'), name='home'),  # new
]