from .models import GitItem, GitUser
from .serializers import GitItemSerialize, GitGiveLinkSerialize
from rest_framework.viewsets import ReadOnlyModelViewSet
from django.db.models import Avg
from rest_framework.response import Response
from rest_framework.views import APIView


class GitGetAllView(ReadOnlyModelViewSet):
    """ Апи получения всех репозиториевв """
    queryset = GitItem.objects.all()
    serializer_class = GitItemSerialize


class GitGiveLinkView(ReadOnlyModelViewSet):
    """ Апи получения ссылок на страницы пользователей (или проектов) """
    queryset = GitUser.objects.all()
    serializer_class = GitGiveLinkSerialize


class GitGetRepView(APIView):
    """ Апи получения репозиториев пользователя (или проекта) """
    queryset = GitItem.objects.all()
    serializer_class = GitItemSerialize

    def get(self, request, *args, **kwargs):
        get_rep_user = GitItem.objects.filter(owner_id=self.kwargs.get('pk'))
        return Response(get_rep_user.values())


class GitIndividualStatView(APIView):
    """
            Индивидуальная статистика:
                Репозиторий с максимальным количеством коммитов (название репозитория - количество)
                Среднее количество звезд в репозиториях

    """

    def get(self, request, *args, **kwargs):
        max_count_commit = \
            GitItem.objects.filter(owner=self.kwargs.get('pk')).values('name_rep', 'commit_count').order_by(
                '-commit_count')[
                0]
        average_stars = GitItem.objects.filter(owner=self.kwargs.get('pk')).values('stars').aggregate(Avg('stars'))
        return Response({'Репозиторий с максимальным количеством коммитов': max_count_commit,
                         'Среднее количество звезд в репозиториях': average_stars})


class GitOverallStatView(APIView):
    """
            Общая статистика:
                Количество пользователей(проектов)
                Общее количество репозиториев
                Среднее количество репозиториев
     """

    def get(self, request, *args, **kwargs):
        user_count = GitUser.objects.all().count()
        count_repo = GitItem.objects.all().count()
        return Response({'Количество пользователей(проектов)': user_count, 'Общее количество репозиториев': count_repo,
                         'Среднее количество репозиториев': count_repo / user_count})
