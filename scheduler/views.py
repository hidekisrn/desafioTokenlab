from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from scheduler.models import Event
from scheduler.serializer import EventSerializer

class EventViewSet(APIView):
    permission_classes = (IsAuthenticated,)
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def get(self, request):
        events = Event.objects.filter(user=request.user)
        data = self.serializer_class(events, many=True).data
        return Response(data=data, status=200)

    def post(self, request):
        try:
            data = request.data
            data['user'] = request.user
            event = self.serializer_class().create(data)
            return Response(status=201)
        except Exception as e:
            if e.message == 'busy time':
                return Response(data={'log': 'busy time'}, status=400)
            return Response(data={}, status=400)

    def put(self, request):
        user = request.user
        data = request.data
        response = Response()
        try:
            event = user.events.get(id=data.pop('id'))
            data['user'] = user
            self.serializer_class().update(instance=event, validated_data=data)
            response.status_code = 204
        except ObjectDoesNotExist:
            response.data = {'log': 'event does not exist'}
            response.status_code = 400
        except ValidationError:
            response.data = {'log': 'busy time'}
            response.status_code = 400
        except Exception as e:
            response.data = {'log': str(e)}
            response.status_code = 400
        return response
    
    def delete(self, request):
        user = request.user
        data = request.data
        response = Response()
        try:
            event = user.events.get(id=data.pop('id'))
            event.delete()
            response.status_code = 204
        except ObjectDoesNotExist:
            response.data = {'log': 'event does not exist'}
            response.status_code = 400
        except Exception as e:
            response.data = {'log': str(e)}
            response.status_code = 400
        return response
