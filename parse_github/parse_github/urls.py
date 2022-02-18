from django.contrib import admin
from django.urls import path
from rest_framework.routers import SimpleRouter
from api.views import GitOverallStatView, GitGiveLinkView, GitGetRepView, GitIndividualStatView, GitGetAllView

router = SimpleRouter()
router.register(r'gitlink', GitGiveLinkView, basename='gitlink')
router.register(r'gitgetall', GitGetAllView, basename='gitgetall')


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('GitOverallStatView/<int:pk>/', GitMaxCommitView.as_view(), name="gitmaxcommitview"),
    path('gitoveral/', GitOverallStatView.as_view(), name='gitoveral'),
    path('gitindividualstats/<int:pk>/', GitIndividualStatView.as_view(), name='gitindividualstats'),
    path('gitgetrep/<int:pk>/', GitGetRepView.as_view(), name='gitgetrep')
]

urlpatterns += router.urls
