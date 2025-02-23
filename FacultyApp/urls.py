from django.urls import path

from . import views

urlpatterns = [path("index.html", views.index, name="index"),
               path("AdminLogin.html", views.AdminLogin, name="AdminLogin"),	      
               path("AdminLoginAction", views.AdminLoginAction, name="AdminLoginAction"),
               path("AddFacultyAction", views.AddFacultyAction, name="AddFacultyAction"),
               path("AddFaculty.html", views.AddFaculty, name="AddFaculty"),
               path("AddStudentAction", views.AddStudentAction, name="AddStudentAction"),
               path("AddStudent.html", views.AddStudent, name="AddStudent"),
	       path("StudentLogin.html", views.StudentLogin, name="StudentLogin"),
	       path("StudentLoginAction", views.StudentLoginAction, name="StudentLoginAction"),
	       path("FacultyLogin.html", views.FacultyLogin, name="FacultyLogin"),
               path("FacultyLoginAction", views.FacultyLoginAction, name="FacultyLoginAction"),
	       path("ViewFaculty", views.ViewFaculty, name="ViewFaculty"),
               path("ViewStudent", views.ViewStudent, name="ViewStudent"),	   
	       path("SubjectsSchedules.html", views.SubjectsSchedules, name="SubjectsSchedules"),
               path("SubjectsSchedulesAction", views.SubjectsSchedulesAction, name="SubjectsSchedulesAction"),
	       path("ManagePublications.html", views.ManagePublications, name="ManagePublications"),
               path("ManagePublicationsAction", views.ManagePublicationsAction, name="ManagePublicationsAction"),
	       path("UploadMarks.html", views.UploadMarks, name="UploadMarks"),
               path("UploadMarksAction", views.UploadMarksAction, name="UploadMarksAction"),
	       path("Engagement.html", views.Engagement, name="Engagement"),
               path("EngagementAction", views.EngagementAction, name="EngagementAction"),
	       path("ViewSchedules", views.ViewSchedules, name="ViewSchedules"),
	       path("ViewPublications", views.ViewPublications, name="ViewPublications"),
	       path("DownloadMarks", views.DownloadMarks, name="DownloadMarks"),
	       path("ViewEngagement", views.ViewEngagement, name="ViewEngagement"),
	       path("DownloadAction", views.DownloadAction, name="DownloadAction"),
]

