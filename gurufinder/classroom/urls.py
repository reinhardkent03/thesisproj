from django.urls import path
from . import views

from module.views import CourseModules, NewModule
from page.views import NewPageModule, PageDetail, MarkPageAsDone
from quiz.views import NewQuiz, NewQuestion, QuizDetail, TakeQuiz, SubmitAttempt, AttemptDetail
from assignment.views import NewAssignment, AssignmentDetail, NewSubmission
from question.views import NewStudentQuestion, Questions, QuestionDetail, MarkAsAnswer, VoteAnswer




app_name = 'classroom'
urlpatterns = [
    path('', views.ClassroomListView.as_view(), name='classroom_list'),
    path('<slug:slug>/', views.SubjectListView.as_view(), name='subject_list'),
    path('<slug:slug>/<int:subject_id>/', views.CourseDetail, name='course'),
    path('<slug:slug>/<int:subject_id>/modules/', CourseModules, name='modules'),
    path('<slug:slug>/<int:subject_id>/modules/new-module/', NewModule, name='new-module'),
    #pages
    path('<slug:slug>/<int:subject_id>/modules/<int:module_id>/pages/new-page/', NewPageModule, name='new-page'),
    path('<slug:slug>/<int:subject_id>/modules/<int:module_id>/pages/<int:page_id>/', PageDetail, name='page-detail'),
    path('<slug:slug>/<int:subject_id>/modules/<int:module_id>/pages/<int:page_id>/done/', MarkPageAsDone, name='mark-page-as-done'),

    #Quizzes
    path('<slug:slug>/<int:subject_id>/modules/<int:module_id>/quiz/new-quiz', NewQuiz, name='new-quiz'),
    path('<slug:slug>/<int:subject_id>/modules/<int:module_id>/quiz/<int:quiz_id>/new-question', NewQuestion, name='new-question'),
    path('<slug:slug>/<int:subject_id>/modules/<int:module_id>/quiz/<int:quiz_id>/', QuizDetail, name='quiz-detail'),
    path('<slug:slug>/<int:subject_id>/modules/<int:module_id>/quiz/<int:quiz_id>/take', TakeQuiz, name='take-quiz'),
    path('<slug:slug>/<int:subject_id>/modules/<int:module_id>/quiz/<int:quiz_id>/take/submit', SubmitAttempt, name='submit-quiz'),
    path('<slug:slug>/<int:subject_id>/modules/<int:module_id>/quiz/<int:quiz_id>/<int:attempt_id>/results', AttemptDetail, name='attempt-detail'),

    #Assignment
    path('<slug:slug>/<int:subject_id>/modules/<int:module_id>/assignment/new-assignment', NewAssignment, name='new-assignment'),
    path('<slug:slug>/<int:subject_id>/modules/<int:module_id>/assignment/<int:assignment_id>', AssignmentDetail, name='assignment-detail'),
    path('<slug:slug>/<int:subject_id>/modules/<int:module_id>/assignment/<int:assignment_id>/start', NewSubmission, name='start-assignment'),

    #Submissions
	path('<slug:slug>/<int:subject_id>/submissions', views.Submissions, name='submissions'),
	path('<slug:slug>/<int:subject_id>/student-submissions', views.StudentSubmissions, name='student-submissions'),
	path('<slug:slug>/<int:subject_id>/submissions/<int:grade_id>/grade', views.GradeSubmission, name='grade-submission'),

    #Questions
    path('<slug:slug>/<int:subject_id>/questions', Questions, name='questions'),
    path('<slug:slug>/<int:subject_id>/questions/new-question', NewStudentQuestion, name='new-student-question'),
    path('<slug:slug>/<int:subject_id>/questions/<int:question_id>', QuestionDetail, name='question-detail'),
    path('<slug:slug>/<int:subject_id>/questions/<int:question_id>/vote', VoteAnswer, name='vote-answer'),
    path('<slug:slug>/<int:subject_id>/questions/<int:question_id>/<int:answer_id>/mark-as-answer', MarkAsAnswer, name='mark-as-answer'),


    #path('<str:classroom>/<slug:slug>/', views.LessonListView.as_view(), name='lesson_list'),
    path('<str:classroom>/<str:slug>/create/', views.LessonCreateView.as_view(), name='lesson_create'),
    path('<str:classroom>/<str:subject>/<slug:slug>/', views.LessonDetailView.as_view(), name='lesson_detail'),
    path('<str:classroom>/<str:subject>/<slug:slug>/<int:lesson_id>/', views.lesson_completed, name='lesson_complete'),
    # path('<str:classroom>/<str:subject>/<slug:slug>/<int:id>/', views.lesson_not_completed, name='lesson_not_completed'),
    path('<str:classroom>/<str:subject>/<slug:slug>/update/', views.LessonUpdateView.as_view(), name='lesson_update'),
    path('<str:classroom>/<str:subject>/<slug:slug>/delete/', views.LessonDeleteView.as_view(), name='lesson_delete'),
]