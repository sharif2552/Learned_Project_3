
from django.urls import path,include
from . import views

urlpatterns = [

    path('',views.SignupPage),
    path('signup/',views.SignupPage),
    path('login/',views.LoginPage),
    path('logout/',views.LogoutPage),
    path('all_task/',views.all_task),
    path('add_task/',views.add_task),
    path('delete_task/',views.delete_task),
    path('delete_task/<int:task_id>',views.delete_task),
    path('edit_task',views.edit_task),
    path('edit_task/<str:pk>',views.edit_task),
    path('gotoheaven/',views.SignupPage)
]
