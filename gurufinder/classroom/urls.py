from django.urls import path
from . import views

app_name = 'classroom'
urlpatterns = [
    path('', views.ClassroomListView.as_view(), name='classroom_list'),
    path('<slug:slug>/', views.SubjectListView.as_view(), name='subject_list'),
    path('<str:classroom>/<slug:slug>/', views.LessonListView.as_view(), name='lesson_list'),
    path('<str:classroom>/<str:slug>/create/', views.LessonCreateView.as_view(), name='lesson_create'),
    path('<str:classroom>/<str:subject>/<slug:slug>/', views.LessonDetailView.as_view(), name='lesson_detail'),
    path('<str:classroom>/<str:subject>/<slug:slug>/<int:lesson_id>/', views.lesson_completed, name='lesson_complete'),
    # path('<str:classroom>/<str:subject>/<slug:slug>/<int:id>/', views.lesson_not_completed, name='lesson_not_completed'),
    path('<str:classroom>/<str:subject>/<slug:slug>/update/', views.LessonUpdateView.as_view(), name='lesson_update'),
    path('<str:classroom>/<str:subject>/<slug:slug>/delete/', views.LessonDeleteView.as_view(), name='lesson_delete'),
]