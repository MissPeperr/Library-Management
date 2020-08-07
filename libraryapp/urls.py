from django.urls import include, path
from .views import *

app_name = "libraryapp"

urlpatterns = [
    path('', home, name='home'),
    path('books/', book_list, name='books'),
    path('book/form', book_form, name='book_form'),
    path('books/<int:book_id>/', book_details, name='book'),
    path('books/<int:book_id>/form/', book_edit_form, name='book_edit_form'),
    path('librarians/', list_librarians, name='librarians'),
    path('librarian/<int:librarian_id>/', librarian_details, name='librarian'),
    path('libraries/', list_libraries, name='locations'),
    path('libraries/form', library_form, name='libraries_form'),
    path('libraries/<int:library_id>/', library_details, name='library'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', logout_user, name='logout'),
]