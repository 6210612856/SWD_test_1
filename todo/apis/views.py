from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from lists.models import ToDoList
from .serializers import ListSerializer

@api_view(['GET'])
def getData(request):
    lists = ToDoList.objects.all()
    serializer = ListSerializer(lists, many=True)
    return Response(serializer.data, status= status.HTTP_200_OK)

@api_view(['POST'])
def addData(request):
    serializer = ListSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status= status.HTTP_201_CREATED)
    return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def deleteData(request):
    ids = request.data.get('ids',[])    
    queryset = ToDoList.objects.all()
    target = queryset.filter(id__in=ids)
    if len(target) < 1:
        return Response(status=status.HTTP_404_NOT_FOUND)
    target.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def editData(request):
    ids = request.data.get('ids',[])
    title = request.data.get('title',[])
    desc = request.data.get('desc',[])
    target = queryset.filter(id__in=ids)

    queryset = ToDoList.objects.all()
    if len(target) < 1:
        return Response(status=status.HTTP_404_NOT_FOUND)

    target.update(title=title,desc=desc)
    return Response(status=status.HTTP_200_OK)
    
