from rest_framework.response import Response
from rest_framework.decorators import api_view
from core.models import Contact
from .serializers import ContactSerializer


@api_view(['GET'])
def getData(request):
    items = Contact.objects.all()
    serializer = ContactSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addItem(request):
    serializer = ContactSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)