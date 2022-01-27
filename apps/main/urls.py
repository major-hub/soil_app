from django.urls import path, include
from rest_framework import routers
from user.views import UserViewSet
from main.api.files import FileViewSet
from main.api.news import NewsViewSet
from main.api.contact import ContactApiView
from main.api.employee import EmployeeViewSet
from main.api.about import HistoryViewSet
from main.api.service import ServiceModelViewSet, FunctionViewSet
from main.api.document import DocumentViewSet
from main.api.laboratory import LaboratoryViewSet
from main.api.partner import PartnerViewSet
from main.api.gallery import GalleryViewSet, GalleryTpeViewSet
from main.api.static import StaticAPIView

router = routers.DefaultRouter()
router.register('user', UserViewSet, 'user')
router.register('file', FileViewSet, 'file')
router.register('news', NewsViewSet, 'news')
router.register('employee', EmployeeViewSet, 'employee')
router.register('history', HistoryViewSet, 'history')
router.register('service', ServiceModelViewSet, 'service')
router.register('function', FunctionViewSet, 'function')
router.register('document', DocumentViewSet, 'document')
router.register('laboratory', LaboratoryViewSet, 'laboratory')
router.register('partner', PartnerViewSet, 'partner')
router.register('gallery_type', GalleryTpeViewSet, 'gallery_type')
router.register('gallery', GalleryViewSet, 'gallery')

urlpatterns = [
    path('contact/', ContactApiView.as_view()),
    path('static/', StaticAPIView.as_view()),
    path('', include(router.urls))
]
