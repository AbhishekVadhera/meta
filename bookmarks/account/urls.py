from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views


from . import views

app_name = 'account'
urlpatterns = [
    path("", views.dashboard, name='dashboard'),
    # path("login/", views.user_login, name='user_login'),
    # login logout urls
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # change password urls
    path('password-change/',
         auth_views.PasswordChangeView.as_view(success_url=reverse_lazy('account:password_change_done')),
         name='password_change'),
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(), name="password_change_done"),
    # reset password url
    path('password-reset/',
         auth_views.PasswordResetView.as_view(success_url=reverse_lazy('account:password_reset_done')),
         name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('password-reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('password-reset/complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
    # create user
    path('create-user/', views.register, name='create-user'),
    path('success/', views.success, name='success'),
    path('edit/', views.edit, name='edit'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
