from django.urls import path
from . import views

urlpatterns = [
    path('',views.movie_list,name='movie_list'), 
    path('register/',views.register_view,name='register'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('movie/<int:id>/',views.movie_detail,name='movie_detail'), 
    path('success/',views.reg_success,name='reg_success'),
    path('add/',views.add_movie,name='add_movie'), 
    path('edit/<int:movieid>/',views.edit_movie,name='edit_movie'), #add edit/movieid/ to link(eg:edit/2/)
    path('delete/<int:movieid>/',views.delete_movie,name='delete_movie'), #add delete/movieid/ to link(eg:delete/4/)
    path('profile/',views.edit_profile,name='edit_profile'),
]
