from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from app.custome_views import common,user

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path('home/',common.home,name='home'),
    path('loginPage/',common.loginPage,name='loginPage'),
    path('registerPage/',common.registerPage,name='registerPage'),
    path('registerUserSave/',common.registerUserSave,name='registerUserSave'),
    path('loginCheck/',user.loginCheck,name='loginCheck'),

    path('userBlog/',user.userBlog,name="userBlog"),
    path('userBlogView/',user.userBlogView,name="userBlogView"),
    path('userBlogPost/',user.userBlogPost,name="userBlogPost"),

]


