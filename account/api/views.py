from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from account.models import Account
from account.api.serializers import AccountSerializer


class AccountListCreateAPIView(ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class AccountRetrieveRetrieveDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    lookup_field = "id"
    