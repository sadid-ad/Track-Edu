from rest_framework.routers import DefaultRouter
from .api_views import CourseViewSet, LessonViewSet, CategoryViewSet, EnrollmentViewSet

router = DefaultRouter()
router.register('courses', CourseViewSet)
router.register('lessons', LessonViewSet)
router.register('categories', CategoryViewSet)
router.register('enrollments', EnrollmentViewSet)

urlpatterns = router.urls