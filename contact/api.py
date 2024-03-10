from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ContactAPIView(APIView):
    def get(self, request):
        
        return Response({'message': 'This is a GET request'})

    def post(self, request):
      
        return Response({'message': 'This is a POST request'}, status=status.HTTP_201_CREATED)
@api_view(['GET', 'POST'])
def contact_api(request):
    if request.method == 'GET':
      
        return Response({'message': 'This is a GET request'})
    elif request.method == 'POST':

        return Response({'message': 'This is a POST request'}, status=status.HT
