from rest_framework import status
from rest_framework.response import Response
from .models import MyUser
from .serializers import *
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import generics, viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication


class RegisterView(generics.CreateAPIView):
    queryset = MyUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
    

class GenerateOptView(generics.CreateAPIView):
    queryset = MyUser.objects.all()
    serializer_class = GenerateOptSerializer


class LoginOTPView(generics.CreateAPIView):
    queryset = MyUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def create(self, request, *args, **kwargs):
        phone = request.data['phone']
        one_time = request.data['otp']
        user = MyUser.objects.filter(phone=phone).first()
        if user:
            if one_time == user.otp:
                now = datetime.datetime.now()
                if user.check_otp_expire(now):                    
                    token = get_tokens_for_user(user)
                    return Response({'token': token['access'], 'refresh': token['refresh']}, status=status.HTTP_200_OK)
                else:
                    return Response({'error': "verfication date expired"}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'wrong verfication key'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'detail': 'User not registered'}, status=status.HTTP_404_NOT_FOUND)


class UserViewSet(generics.ListAPIView):
    queryset = MyUser.objects.all()
    serializer_class  = UserSerializer
    
    def list(self, request, *args, **kwargs):
        try:
            jwt_object = JWTAuthentication() 
            validated_token = jwt_object.get_validated_token(request.headers['token'])
            
            print(validated_token)
            user = jwt_object.get_user(validated_token)
            if user:
                if user.image:
                    data = {
                        "id": user.id,
                        "phone": user.phone,
                        "first_name": user.first_name,
                        "image": user.image.url,
                    }
                else:
                    data = {
                        "id": user.id,
                        "phone": user.phone,
                        "first_name": user.first_name,
                        "image": "",
                    }       
                return Response(data, status=status.HTTP_200_OK)
            else:
                Response(status=status.HTTP_404_NOT_FOUND)
        except:
            data = {
                "token": "required"
            }
        return Response(data, status=status.HTTP_406_NOT_ACCEPTABLE)


class UserDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = MyUser.objects.all()
    serializer_class  = UserSerializer
        
    def retrieve(self, request, *args, **kwargs):
        user_id = kwargs['pk']
        object = MyUser.objects.filter(id=user_id).first()
        print(object)
        if object is not None:
            jwt_object = JWTAuthentication()
            if 'token' in request.headers:
                validated_token = jwt_object.get_validated_token(request.headers['token'])
                user = jwt_object.get_user(validated_token)
                if user:
                    data = []
                    if user.id == user_id:
                        if user.image:
                            data = {
                                "id": user.id,
                                "phone": user.phone,
                                "first_name": user.first_name,
                                "image": user.image,
                            }
                        else:
                            data = {
                                "id": user.id,
                                "phone": user.phone,
                                "first_name": user.first_name,
                                "image": "",
                            }       
                        return Response(data, status=status.HTTP_200_OK)
                    else:
                        return Response({"status":"user not match"}, status=status.HTTP_406_NOT_ACCEPTABLE)
            else:
                data = {
                    "token": "required"
                }
                return Response({"token": "required"}, status=status.HTTP_406_NOT_ACCEPTABLE)                        
        else:
            return Response({"detail": "not found"}, status=status.HTTP_404_NOT_FOUND)
    
    def update(self, request, *args, **kwargs):
        user_id = kwargs['pk']
        object = MyUser.objects.filter(id=user_id).first()
        if object is not None:
            jwt_object = JWTAuthentication()
            if 'token' in request.headers:
                validated_token = jwt_object.get_validated_token(request.headers['token'])
                user = jwt_object.get_user(validated_token)
                if user:
                    data = []
                    if user.id == user_id:
                        if 'first_name' in request.data:
                            user.first_name = request.data['first_name']
                        if 'phone' in request.data:
                            pass
                            # user.phone = request.data['phone']
                        if 'image' in request.data:
                            user.image = request.data['image']
                        user.save()
                        url = ''
                        if user.image:
                            url = f"{user.image.url}"
                        else:
                            url = ''
                        data = {
                            "id": user.id,
                            "phone": user.phone,
                            "first_name": user.first_name,
                            "image": url,
                        }
                        return Response(data, status=status.HTTP_200_OK)
                    else:
                        return Response({"status":"user not match"}, status=status.HTTP_406_NOT_ACCEPTABLE)
                else:
                    return Response({"status":"user not match"}, status=status.HTTP_406_NOT_ACCEPTABLE)
            else:
                return Response({"token": "required"}, status=status.HTTP_406_NOT_ACCEPTABLE)                        
        else:
            return Response({"detail": "not found"}, status=status.HTTP_404_NOT_FOUND)


    def destroy(self, request, *args, **kwargs):
        user_id = kwargs['pk']
        object = MyUser.objects.filter(id=user_id).first()
        if object is not None:
            jwt_object = JWTAuthentication()
            if 'token' in request.headers:
                validated_token = jwt_object.get_validated_token(request.headers['token'])
                user = jwt_object.get_user(validated_token)
                if user:
                    if user.id == user_id:
                        user.delete()
                        return Response({"status": "Deleted"}, status=status.HTTP_200_OK)
                    else:
                        return Response({"status":"user not match"}, status=status.HTTP_406_NOT_ACCEPTABLE)
                else:
                    return Response({"status":"user not match"}, status=status.HTTP_406_NOT_ACCEPTABLE)
            else:
                return Response({"token": "required"}, status=status.HTTP_406_NOT_ACCEPTABLE)                        
        else:
            return Response({"detail": "not found"}, status=status.HTTP_404_NOT_FOUND)



class ConfirmUpdatePhoneView(generics.CreateAPIView):
    queryset = MyUser.objects.all()
    serializer_class = ConfirmUpdatePhoneSerializer

    def create(self, request, *args, **kwargs):
        phone = request.data['phone']
        check = MyUser.objects.filter(phone=phone).first()
        one_time = request.data['otp']
        jwt_object = JWTAuthentication()
        if 'token' in request.headers:
            validated_token = jwt_object.get_validated_token(request.headers['token'])
            user = jwt_object.get_user(validated_token)
            if user.phone == check.phone:
                if one_time == user.otp:
                    now = datetime.datetime.now()
                    if user.check_otp_expire(now):
                        user.phone = user.new_phone 
                        user.save()                   
                        token = get_tokens_for_user(user)
                        return Response({'token': token['access'], 'refresh': token['refresh']}, status=status.HTTP_200_OK)
                    else:
                        return Response({'error': "verfication date expired"}, status=status.HTTP_200_OK)
                else:
                    return Response({'error': 'wrong verfication key'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'error': 'token is not valid'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'user not registered'}, status=status.HTTP_404_NOT_FOUND)
            

class UpdatePhoneView(generics.CreateAPIView):
    queryset = MyUser.objects.all()
    serializer_class = UpdatePhoneSerializer

    def create(self, request, *args, **kwargs):
        phone = request.data['phone']
        if isValid(phone):
            check = MyUser.objects.filter(phone=phone).first()
            if check:
                user_id = request.data['user_id']
                jwt_object = JWTAuthentication()
                if 'token' in request.headers:
                    validated_token = jwt_object.get_validated_token(request.headers['token'])
                    user = jwt_object.get_user(validated_token)
                    if user:
                        otp = generateOTP()
                        if user.id == user_id:
                            user.new_phone = phone
                            now = datetime.datetime.now()
                            date = now + datetime.timedelta(0, 180)        
                            user.otp = str(otp)
                            user.otp_expire = date
                            user.save()
                            username = 'monandtex'
                            password = 'a88^hSE^nM-9'
                            sms_data = {
                                "messages":[{"recipient":f"{phone}","message-id":"abc000000001","sms":{"originator": "3700","content": {"text": f"Your confirmation code for Monand:\n {otp}"}}}]}
                            url = "http://91.204.239.44/broker-api/send"
                            res = requests.post(url=url, headers={}, auth=(username, password), json=sms_data)
                            return Response({"status": "Ok"}, status=status.HTTP_200_OK)
                        else:
                            return Response({"error":"user not match"}, status=status.HTTP_406_NOT_ACCEPTABLE)
                    else:
                        return Response({'error': 'token is not valid'}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response({'error': 'user not registered'}, status=status.HTTP_404_NOT_FOUND)
            else:
                return Response({'error': 'phone already used'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'error': 'phone is not valid'}, status=status.HTTP_404_NOT_FOUND)
