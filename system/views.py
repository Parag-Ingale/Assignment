from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
import re
from .models import CustomUser, Content
from django.http.response import HttpResponse
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate,login,logout
from rest_framework.views import APIView
from .Serializers import UpdateSerializer

class RegisterView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        post_data=request.data
        fullname = post_data.get('fullname')
        phone = post_data.get('phone')
        if len(str(phone))==10:
            mobile=phone
        else:
            return HttpResponse('mobile number must be of 10 digits')

        password = post_data.get('password')
        if re.findall('[A-Z]', password) and re.findall('[a-z]', password) and len(password)>8:
            password1=password
        else:
            return HttpResponse('password must be greater than 8 characters and must contain 1 lower and 1 upper case character')

        email = post_data.get('email')
        if re.findall('[@]', email):
            email1 = email
        else:
            return HttpResponse('enter valid email')

        address = post_data.get('address')
        city = post_data.get('city')
        state = post_data.get('state')
        country = post_data.get('country')
        pincode = post_data.get('pincode')
        if len(str(pincode))==6:
            pin=pincode
        else:
            return HttpResponse('pincode must be of 6 digits')

        obj = CustomUser.objects.create_user(fullname=fullname, phone=mobile, password=password1, email=email1, address=address, city=city,
                            state=state, country=country, pincode=pin)
        obj.save()
        return HttpResponse(Token.objects.create(user=obj))

class LoginView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        post_data = request.data
        email = post_data.get('email')
        password = post_data.get('password')
        user = authenticate(email=email, password=password)
        custom_user = CustomUser.objects.filter(email=email).last()
        if user:
            login(request, user)
            return HttpResponse('user logged in')
        else:
            return HttpResponse('user is not registered')


class ContentView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        custom_user = request.user
        obj = Content.objects.filter(user__email=custom_user).values()
        return HttpResponse(obj)

    def post(self, request):
        custom_user=request.user
        post_data = request.data
        title = post_data.get('title')
        body = post_data.get('body')
        summary = post_data.get('summary')
        doc= post_data.get('doc')
        categories = post_data.get('categories')
        obj = Content.objects.create(user=custom_user, title=title, body=body, summary=summary, doc_pdf=doc, categories=categories)
        obj.save()
        return HttpResponse('Content created')

    def put(self, request):
        custom_user = request.user
        id = request.GET.get('id')
        obj = Content.objects.get(id=id)
        data = request.data
        serializer = UpdateSerializer(instance=obj, data=data)
        if serializer.is_valid():
            serializer.save()
        return HttpResponse('Content updated')


    def delete(self, request):
        custom_user = request.user
        id = request.GET.get('id')
        obj=Content.objects.filter(id=id)
        if obj:
            obj.delete()
            return HttpResponse('Content deleted')
        else:
            return HttpResponse('Content doesnt exist')
