from django.shortcuts import render
from Portal.Serializers.Staff import PersonSerializer,StaffSerializer
from Portal.models.Staff import Person,Staff
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def person_details(request):
    details = Person.objects.all()
    serializer = PersonSerializer(details, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def person(request,pk):
    details = Person.objects.get(id=pk)
    serializer = PersonSerializer(details, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def create_users(request):
    serializer = PersonSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        staff_id = serializer.data['id']
        serializer_staff = StaffSerializer(data={"Staff":staff_id})
        if serializer_staff.is_valid():
            serializer_staff.save()
    return Response(serializer.data)

@api_view(['PUT'])
def update_users(request,pk):
    details = Person.objects.get(id=pk)
    serializer = PersonSerializer(instance=details,data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def staffId(request):
    ls = Staff.objects.all()
    serializer = StaffSerializer(ls,many=True)
    return Response(serializer.data)
