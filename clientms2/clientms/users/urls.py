from django.urls import path

# from . import views
from .views import SignUpView, PasswordResetView, ChangePasswordResetDoneSuccessView, PasswordResetDoneView, ChangePasswordResetDoneView, PasswordResetCompleteView, PasswordResetConfirmView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),

    path('reset_password/', PasswordResetView.as_view(), name='reset_password'),
    path('reset_password/done/', PasswordResetDoneView.as_view(), name='reset_password_done'),
    path('reset_confirmation/<uidb64>/<token>', PasswordResetConfirmView.as_view(), name='reset_password_confirmation'),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='reset_password_complete'),

    path('password_change/', ChangePasswordResetDoneView.as_view(), name='change_password'),
    path('change_password_done', ChangePasswordResetDoneSuccessView.as_view(), name='change_password_done'),
]
