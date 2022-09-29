from django.urls import path
from todolist.views import *
app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),  
    path('create_task/', create_task, name='create_task'),
    path('jsonconvert/', jsondata, name='jsondata'),
    path('finish/<int:id>', update_finish, name='finish'),
    path('delete/<int:id>', update_delete, name='delete'),
]