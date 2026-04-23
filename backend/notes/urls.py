from rest_framework.routers import DefaultRouter
from .views import NoteviewSet


router = DefaultRouter()
router.register(r'notes', NoteviewSet, basename='note')

urlpatterns = router.urls