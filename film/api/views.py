from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView, RetrieveUpdateDestroyAPIView
from film.models import FilmModel, ActorModel, LikeModel, CommentModel,ViewsCountModel
from film.api.serializers import FilmSerializer, ActorSerializer, CommentSerializer, LikeSerializer, ViewCountSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from film.api.permissions import IsSuperUser, IsOwner
# class FilmListAPIView(ListAPIView):
#     queryset = FilmModel.objects.all()
#     serializer_class = FilmSerializer

# class FilmCreateAPIView(CreateAPIView):
#     queryset = FilmModel.objects.all()
#     serializer_class = FilmSerializer

class FilmListCreateAPIView(ListCreateAPIView):
    queryset = FilmModel.objects.all()
    serializer_class = FilmSerializer

# class FilmRetrieveAPIView(RetrieveAPIView):
#     queryset = FilmModel.objects.all()
#     serializer_class = FilmSerializer
#     lookup_field = "id"

# class FilmUpdateAPIView(UpdateAPIView):
#     queryset = FilmModel.objects.all()
#     serializer_class = FilmSerializer
#     lookup_field = "id"

# class FilmDestroyAPIView(DestroyAPIView):
#     queryset = FilmModel.objects.all()
#     serializer_class = FilmSerializer
#     lookup_field = "id"

class FilmRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = FilmModel.objects.all()
    serializer_class = ActorSerializer
    lookup_field = "id"

class ActorListAPIView(ListAPIView):
    queryset = ActorModel.objects.all()
    serializer_class = ActorSerializer

class ActorCreateAPIView(CreateAPIView):
    queryset = ActorModel.objects.all()
    serializer_class = ActorSerializer

class ActorUpdateAPIView(UpdateAPIView):
    queryset = ActorModel.objects.all()
    serializer_class = ActorSerializer
    lookup_field = "id"

class ActorRetrieveAPIView(RetrieveAPIView):
    queryset = ActorModel.objects.all()
    serializer_class = ActorSerializer
    lookup_field = "id"

class ActorDestroyAPIView(DestroyAPIView):
    queryset = ActorModel.objects.all()
    serializer_class = ActorSerializer
    lookup_field = "id"

class CommentListAPIView(ListAPIView):
    queryset = CommentModel.objects.all()
    serializer_class = CommentSerializer

class CommentCreateAPIView(CreateAPIView):
    queryset = CommentModel.objects.all()
    serializer_class = CommentSerializer

# class CommentListCreateAPIView(ListCreateAPIView):
#     queryset = CommentModel.objects.all()
#     serializer_class = CommentSerializer
#     permission_classes = (IsAuthenticated,)

# class CommentUpdateAPIView(UpdateAPIView):
#     queryset = CommentModel.objects.all()
#     serializer_class = CommentSerializer
#     lookup_field = "id"

# class CommentRetrieveAPIView(RetrieveAPIView):
#     queryset = CommentModel.objects.all()
#     serializer_class = CommentSerializer
#     lookup_field = "id"

# class CommentDestroyAPIView(DestroyAPIView):
#     queryset = CommentModel.objects.all()
#     serializer_class = CommentSerializer
#     lookup_field = "id"

class CommentUpdateRetrieveDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = CommentModel.objects.all()
    serializer_class = CommentSerializer
    lookup_field = "id"
    permission_classes = (IsAdminUser,IsOwner)

class FilmCommentListAPIView(ListAPIView):
    def get_queryset(self, request):
        id=self.kwargs.get("id")
        return CommentModel.objects.filter(
            film_id = id,
        )
    serializer_class = CommentSerializer


class LikeListAPIView(ListCreateAPIView):
    queryset = LikeModel.objects.all()
    serializer_class = LikeSerializer
   

class LikeCreateAPIView(ListCreateAPIView):
    queryset = LikeModel.objects.all()
    serializer_class = LikeSerializer
   

class LikeRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = LikeModel.objects.all()
    serializer_class = LikeSerializer
    lookup_field = "id"
    pagination_class = (IsAdminUser,IsOwner)

class FilmLikeListAPIView(ListAPIView):
    def get_queryset(self, request):
        id = self.kwargs.get("id")
        return LikeModel.objects.filter(
            film_id=id
        )
    serializer_class = LikeSerializer

class ViewCountListAPIView(ListCreateAPIView):
    queryset = ViewsCountModel.objects.all()
    serializer_class = ViewCountSerializer
   

class ViewCountCreateAPIView(ListCreateAPIView):
    queryset = ViewsCountModel.objects.all()
    serializer_class = ViewCountSerializer

class ViewCountRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = ViewsCountModel.objects.all()
    serializer_class = ViewCountSerializer
    lookup_field = "id"
    pagination_class = (IsAdminUser,IsOwner)

class FilmViewCountListAPIView(ListAPIView):
    def get_queryset(self, request):
        id = self.kwargs.get("id")
        return ViewsCountModel.objects.filter(
            film_id = id,
        )
    serializer_class = ViewCountSerializer