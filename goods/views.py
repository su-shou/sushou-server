from rest_framework.views import APIView

from users.views import userAuth

class categories(APIView):
    @userAuth
    def get(self, request):
        print(request.data)
        pass