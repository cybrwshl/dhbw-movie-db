from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'persons', PersonViewSet)
router.register(r'movies', MovieViewSet)
router.register(r'keywords', KeywordViewSet)
router.register(r'companies', CompanyViewSet)
router.register(r'roles', RoleViewSet)

urlpatterns = router.get_urls()
