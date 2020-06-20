from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name ="my_todo_app"


urlpatterns = [
    path('index_page/', views.index_page, name="index_page"),
    path('insert_data/', views.insert_data, name="insert_data"),
    path('display_data/', views.display_data, name="display_data"),
    path('update_data/<str:pk>/', views.update_data, name="update_data"),

    path('delete_data/<str:pk>/', views.delete_data, name="delete_data"),
    path('register/', views.register, name="register"),
    path('user_login/', views.user_login, name="user_login"),
    path('user_logout/', views.user_logout, name="user_logout"),

    # sending password reset mail
    path('reset_password/', auth_views.PasswordResetView.as_view(), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]

