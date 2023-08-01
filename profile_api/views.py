from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Tes API View."""

    def get(self, resquest, format=None):
        """ Retorna uma lista das recursos do APIView."""

        o_apiview = [
                'Usa métodos HTTP como funções(get, post, patch, put, delete)',
                'Te dá maior controle sobre a lógica da sua aplicação',
                'É mapeada manualmente para URLs'
        ]

        return Response({'message':'Hello!', 'an_apiview': an_apiview})
