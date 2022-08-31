from rest_framework.serializers import ModelSerializer

from core.models import Cachorro, Comedouro, Tag, Publicacoes


class ComedouroSerializer(ModelSerializer):
    class Meta:
        model = Comedouro
        fields = "__all__"


class CachorroSerializer(ModelSerializer):
    class Meta:
        model = Cachorro
        fields = "__all__"


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"

class PublicacoesSerializer(ModelSerializer):
    class Meta:
        model = Publicacoes
        fields = "__all__"
