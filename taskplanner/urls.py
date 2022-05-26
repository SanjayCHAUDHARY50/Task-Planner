from django.contrib import admin
from django.urls import path, include
from taskplanner import views
from todolist_app import views as todolist_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('task/', include('todolist_app.urls')),
    path('account/', include('users_app.urls')),
    path('', views.index, name = 'index'),
    path('contact-us', todolist_views.contact, name = 'Contact Us'),
    path('about-us', todolist_views.about, name = 'About Us'),
]
