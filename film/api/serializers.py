from rest_framework import serializers
from film.models import FilmModel ,ActorModel, CommentModel, LikeModel, ViewsCountModel

class FilmSerializer(serializers.ModelSerializer):

    class Meta:
        model = FilmModel
        fields = "__all__"


class ActorSerializer(serializers.ModelSerializer):

    class Meta:
        model = ActorModel
        fields = "__all__"

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = CommentModel
        fields = "__all__"


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = LikeModel
        fields = "__all__"


class ViewCountSerializer(serializers.ModelSerializer):

    class Meta:
        model = ViewsCountModel
        fields = "__all__"