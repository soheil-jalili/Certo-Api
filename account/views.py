from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from account.serializer import SignUpSerializer, SignInSerializer


class SignUpView(APIView):
    def post(self, request):
        sign_up_serializer = SignUpSerializer(data=request.data)
        if sign_up_serializer.is_valid():
            user = sign_up_serializer.save()
            token, created = Token.objects.get_or_create(user=user)

            return Response({
                'message': 'Sign up successful',
                'data': sign_up_serializer.data,
                'token': token.key
            })

        return Response(sign_up_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SignInView(APIView):
    def post(self, request):
        serializer = SignInSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']

            try:
                user_obj = User.objects.get(email=email)
            except User.DoesNotExist:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

            user = authenticate(username=user_obj.username, password=password)

            if user is not None:
                token, created = Token.objects.get_or_create(user=user)
                return Response({
                    'message': 'Sign in successful',
                    'token': token.key,
                })

            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SignOutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            request.user.auth_token.delete()
        except (AttributeError, ObjectDoesNotExist):
            pass
        return Response({"detail": "Successfully signed out."}, status=status.HTTP_200_OK)

