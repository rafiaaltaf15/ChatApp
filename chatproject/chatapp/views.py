from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework.permissions import IsAuthenticated
from .models import Room ,Message ,Profile
from .serializers import RoomSerializer
from.serializers import MessageSerializer

class SignupAPI(APIView):
    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        if not username or not password:
            return Response({"ERROR": "FIELDS NOT GIVEN"}, status=400)

        if User.objects.filter(username=username).exists():
            return Response({"MESSAGE": "USERNAME ALREADY EXISTS"}, status=400)

        if User.objects.filter(email=email).exists():
            return Response({"MESSAGE": "EMAIL ALREADY EXISTS"}, status=400)

        User.objects.create_user(username=username, password=password, email=email)
        return Response({"MESSAGE": "SUCCESSFULLY CREATED"}, status=201)


class LoginAPI(APIView):
    def post(self, request):
        username_or_email = request.data.get('username')
        password = request.data.get('password')

        if not username_or_email or not password:
            return Response({"ERROR": "USERNAME/EMAIL AND PASSWORD REQUIRED"}, status=400)

        # Check if login is via email or username
        if '@' in username_or_email:
            try:
                user_obj = User.objects.get(email=username_or_email)
                username = user_obj.username
            except User.DoesNotExist:
                return Response({"MESSAGE": "INVALID CREDENTIALS"}, status=400)
        else:
            username = username_or_email

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({"MESSAGE": "SUCCESSFULLY LOGGED IN"}, status=200)

        return Response({"MESSAGE": "INVALID CREDENTIALS"}, status=400)
    
class LogoutAPI(APIView):
    permission_classes =[IsAuthenticated]
    def post(self, request):
        logout(request)
        return Response({"MESSAGE": "SUCCESSFULLY LOGGED OUT"}, status=200)

class CheckLoginAPI(APIView):

    def get(self, request):
        if request.user.is_authenticated:
            return Response({"Logged_In": True})
        return Response({"Logged_In": False})
class GetAllUser(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
            user=User.objects.exclude(id=request.user.id).exclude(is_superuser=True)
            data = [{"id": u.id, "username": u.username, "email": u.email} for u in user]
            return Response(data)
class CreatePrivateRoomAPI(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        other_user_id = request.data.get('user_id')
        if not other_user_id:
            return Response({"ERROR": "user id is not found"}, status=400)
        
        users_id =sorted([request.user.id, other_user_id])
        room_name = f"{users_id[0]}_{users_id[1]}"

        room, created = Room.objects.get_or_create(
            name=room_name,
            defaults={'created_by': request.user}
        )

        return Response({"room":{"id": room.id, "room_name": room.name}}, status=201)
    
class PostMessage(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        room_id = request.data.get('room_id')
        text = request.data.get('text')

        if not room_id or not text:
            return Response({"ERROR": "ROOM ID AND text are REQUIRED"}, status=400)
        room = Room.objects.get(id=room_id)
        data=Message.objects.create(
            room=room,
            sender=request.user,
            text=text
            )
        serializer = MessageSerializer(data)
        return Response({"MESSAGE": "MESSAGE send sucessfully"}, status=201)
class GetMessage(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, room_id):
        if not room_id:
            return Response({"ERROR": "ROOM ID is REQUIRED"}, status=400)
        message= Message.objects.filter(room=room_id).order_by('timestamp')
        serializer=MessageSerializer(message, many=True)
        return Response(serializer.data)

class NewSignupAPI(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        phone_number = request.data.get('phone_number')

        if not username or not password or not phone_number:
            return Response({"ERROR": "FIELDS NOT GIVEN"}, status=400)

        if User.objects.filter(username=username).exists():
            return Response({"MESSAGE": "USERNAME ALREADY EXISTS"}, status=400)

        if Profile.objects.filter(phone_number=phone_number).exists():
            return Response({"MESSAGE": "phonenumber  ALREADY EXISTS"}, status=400)

        user =User.objects.create(username=username, password=password)
        user111=Profile.objects.create(user=user, phone_number=phone_number)    
        return Response({"MESSAGE": "SUCCESSFULLY CREATED"}, status=201)
    
class NewLoginAPI(APIView):
    def post(self, request):
        phone_number= request.data.get('phone_number')
        password = request.data.get('password')


        if not phone_number or not password:
            return Response({"ERROR": "Phone number and password required"}, status=400)

        try:
            profile = Profile.objects.get(phone_number=phone_number)
            user = profile.user
        except Profile.DoesNotExist:
            return Response({"ERROR": "Invalid phone number"}, status=400)

        user = authenticate(username=user.username, password=password)
        if user is not None:
            login(request, user)
            return Response({"MESSAGE": "Successfully logged in"}, status=200)
        else:
            return Response({"ERROR": "Invalid password"}, status=400)
    

class GetAllUserss(APIView):

        def get(self, request):
                user=Profile.objects.exclude(id=request.user.id)
                users_data = [{"id": u.id, "phone_number": u.phone_number} for u in user]
                return Response(users_data)
        
class CreateRoomAPI(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        room_name = request.data.get('room_name')
        if not room_name:
            return Response({"ERROR": "ROOM NAME is REQUIRED"}, status=400)
        
        if Room.objects.filter(name=room_name).exists():
            return Response({"MESSAGE": "ROOM NAME ALREADY EXISTS"}, status=400)

        room = Room.objects.create(
            name=room_name,
            created_by=request.user
        )

        return Response({"room":{"id": room.id, "room_name": room.name}}, status=201)