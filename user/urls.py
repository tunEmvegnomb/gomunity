from django.urls import path
from user import views
from user.views import GomunityTokenObtainPairView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView)

urlpatterns =[
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/custom/token/', GomunityTokenObtainPairView.as_view(), name='gomunity_token'),
    path('signup/', views.UserView.as_view(), name="signup"),
]