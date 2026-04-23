from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken


class RegisterView(APIView):
    
    permission_classes = [AllowAny]  # ← pubblico!

    def post(self, request):
        
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        # 1. Controlla se l'utente esiste già
        if User.objects.filter(username=username).exists():
            return Response({'error': "User already exists"}, status = status.HTTP_400_BAD_REQUEST)
        else:
            # 2. Crea l'utente
            user = User.objects.create_user(username=username, email=email, password=password)

        refresh = RefreshToken.for_user(user)
        
        # 4. Restituisci i token
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_201_CREATED)