""" lifeInvader url module """

# Django
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from lifeinvader import views as local_views
from posts import views as post_views
from users import views as user_views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('hello-world/', local_views.hello_world, name='hello_world'),
    path('sorted/', local_views.sort_integers, name='sort'),
    path('hi/<str:name>/<int:age>/', local_views.say_hi, name='hi'),
    path('posts/', post_views.list_posts, name='feed'),
    path('users/login/', user_views.login_view, name='login')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
