"""
URL configuration for chatproject project.

The urlpatterns list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from chatapp.views import SignupAPI
from chatapp.views import LoginAPI
from chatapp.views import LogoutAPI 
from chatapp.views import CheckLoginAPI
from chatapp.views import GetAllUser
from chatapp.views import CreatePrivateRoomAPI
from chatapp.views import PostMessage
from chatapp.views import GetMessage
from chatapp.views import NewSignupAPI
from chatapp.views import NewLoginAPI
from chatapp.views import GetAllUserss
from chatapp.views import CreateRoomAPI
urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', SignupAPI.as_view(), name='Signup'),
    path('login/', LoginAPI.as_view(), name='Login'),
    path('logout/', LogoutAPI.as_view(), name='Logout'),
    path('checklogin/', CheckLoginAPI.as_view(), name='CheckLogin'),
    path('getalluser/', GetAllUser.as_view(), name='GetAllUser'),
    path('createroom/', CreatePrivateRoomAPI.as_view(), name='createroom'),
    path('postmessage/', PostMessage.as_view(), name='postmessage'),
    path('getmessage/<int:room_id>/', GetMessage.as_view(), name='getmessage'),
    path('newsignup/', NewSignupAPI.as_view(), name='Signup'),
    path('newlogin/', NewLoginAPI.as_view(), name='Login'),
    path('getalluserss/', GetAllUserss.as_view(), name='GetAllUserss'),
     path('createroom/', CreateRoomAPI.as_view(), name='CreateRoomAPI'),
]

