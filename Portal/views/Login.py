from Portal.models.Login import Login
from Portal.models.Staff import Person
from Portal.Serializers.Login import LoginSerializer
from Portal.Serializers.Staff import PersonSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['POST'])
def login(request):
    serializer = LoginSerializer(data=request.data)
    person_detail = Person.objects.all()

    if serializer.is_valid():
        if (serializer.data['Email'] == Person.objects.filter(Email)) and (serializer.data['Password'] == Person.objects.filter(PasswordHash)):
            # save_details = Login(Login.Firstname = person_detail[''])  
            print('Working')              
        return Response(person_detail.data)