from django.urls import path
from . import views

urlpatterns = [
    path("notes/", views.NotesViewset.as_view(), name="note-list"),
    # path("quotes/", views.QuotesViewset.as_view(), name="Quotes"),
    path("notes/delete/<int:pk>/", views.NoteDelete.as_view(), name="delete-note")
]