from django.shortcuts import render
from .models import *
from .serializers import *
# Create your views here.

from rest_framework.response import Response
from rest_framework.decorators import api_view,APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ViewSet
# :::::::::::::::::::::::::::::::: registation function:::::::::::::::::::::::::::::

@api_view(['POST'],)
def registation(request):
    if request.method == 'POST':
        username = request.data['username']
        email = request.data['email']
        first_name = request.data['first_name']
        last_name = request.data['last_name']
        password1 = request.data['password1']
        password2 = request.data['password2']
        if password1 != password2:
            return Response({"error":"two password didn't match "})
        if User.objects.filter(username=username).exists():
            return Response({"error":"username allready exists!"})

        user = User()
        user.username = username
        user.email = email
        user.first_name = first_name
        user.last_name = last_name  
        user.set_password(raw_password=password1)
        user.save()
    return Response({'success':'successfully login'})
    










#:::::::::::::::::::::::::::::::::::::: function base api ::::::::::::::::::::::::::::::::::::::::::::::::::


@api_view(['POST','GET'])

def first_function(request):
    if request.method == 'POST':
        name = request.data['name']
        age = request.data['age']
        email = request.data['email']
        s=frist_model(name=name,age=age,email=email)
        s.save()
        return Response({'success':'successfull saved'})
    context={
        'name':'meherin',
        'age':1,
        'email':'meherin@gmail.com'
    }
    return Response(context)
    
@api_view(['GET'])
def first_get(request):
    obj = frist_model.objects.all()
    serializer = first_serializer(obj, many=True)
    return Response(serializer.data)


# :::::::::::::::::::::::::::::::::: class base api form decorators ::::::::::::::::::::::::::::::::::

class first_class(APIView):
    def post(self,request,format=None):
        if request.method == 'POST':
            serializer = second_serializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
    def get(self,request,format=None):
        obj = second_model.objects.all()
        serializer= second_serializer(obj, many=True)
        return Response(serializer.data)
    
from django.http import Http404
class second_class(APIView):
    def get_object(self, id):
        try:
            return second_model.objects.get(id=id)
        except second_model.DoesNotExist:
            raise Http404
        
    def get(self , request, id ,  format=None):
        obj_instance = self.get_object(id)
        serializer = second_serializer(obj_instance)
        return Response(serializer.data)
    
    def put(self, request, id , format=None):
        obj_instance = self.get_object(id)
        serializer = second_serializer(obj_instance,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error':'update error!'})
    
    def delete(self, request, id , format=None):
        obj_instance = self.get_object(id)
        obj_instance.delete()
        return Response({'success':'successfully deleted data!'})

    

# :::::::::::::::::::::::::::::::: Class base api view using generic ::::::::::::::::::::::::::::::


class thirth_class_generic(ListCreateAPIView):
    queryset = thirth_model.objects.all()
    serializer_class = thirth_serializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
   

class fourth_class_generic(RetrieveUpdateDestroyAPIView):
    queryset = thirth_model.objects.all()
    serializer_class = thirth_serializer
    lookup_field='id'




# :::::::::::::::::::::::::::::::: class base view using viewset ::::::::::::::::::::::::::::::::::
    

class fifth_class(ViewSet):
    permission_classes=[AllowAny]
    def create(self,request):
        serializer = fourth_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)        
     

    def list(self,request):
        queryset = fourth_model.objects.all()
        serializer = fourth_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk):
        id = pk
        if id is not None:
            obj = fourth_model.objects.get(id=id)
            serializer = fourth_serializer(obj)
            return Response(serializer.data)
        else:
            return Response({"error":"not found"})
    
    def update(self, request, pk):
        id = pk
        if id is not None:
            obj = fourth_model.objects.get(id = id)
            serializer = fourth_serializer(obj,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        
    def partial_update(self,request,pk):
        id = pk
        if id is not None:
            obj = fourth_model.objects.get(id=id)
            serializer = fourth_serializer(obj, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        
    def delete(self, request,pk):
        id = pk
        if id is not None:
            obj = fourth_model.objects.get(id=id)
            obj.delete()
            return Response({"success":"successfully data deleted! "})
      