from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.permissions import AllowAny
from users.models import User

@api_view(['POST'])
@permission_classes((AllowAny, ))
def user_register(request):
    username = request.data['username']
    password = request.data['password']
    try:
        User.objects.get(username=username)
        return Response(data={'log': 'user already exists'}, status=400)
    except ObjectDoesNotExist:
        user = User.objects.create(username=username)
        user.set_password(password)
        user.save()
        return Response(status=201)