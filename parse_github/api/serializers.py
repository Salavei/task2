from rest_framework.serializers import ModelSerializer
from .models import GitItem, GitUser


class GitItemSerialize(ModelSerializer):
    """ Общий сериализатор по репозиториям """
    class Meta:
        model = GitItem
        fields = '__all__'


class GitGiveLinkSerialize(ModelSerializer):
    """ Сериализатор по Юзерам для ссылки """
    class Meta:
        model = GitUser
        fields = '__all__'
