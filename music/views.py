from rest_framework.views import APIView
from rest_framework.response import Response


class HelloWorldAPIView(APIView):
    def get(self, request):
        return Response(data={'message': 'Hello World'})

    def post(self, request):
        return Response(data={'greeting': f"Hello {request.data['name']}"})