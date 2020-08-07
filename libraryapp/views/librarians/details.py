import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from libraryapp.models import Librarian, Library
from ..connection import Connection


def create_librarian(cursor, row):
    _row = sqlite3.Row(cursor, row)

    librarian = Librarian()
    librarian.id = _row['id']
    librarian.first_name = _row['first_name']
    librarian.last_name = _row['last_name']

    library = Library()
    library.id = _row['location_id']
    library.title = _row['title']
    library.address = _row['address']

    librarian.location = library

    return librarian


def get_librarian(librarian_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = create_librarian
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            l.id,
            l.location_id,
            l.user_id,
            u.first_name,
            u.last_name,
            u.email,
            library.title,
            library.address
        FROM libraryapp_librarian l
        JOIN auth_user u on l.user_id = u.id
        JOIN libraryapp_library as library ON l.location_id = library.id
        WHERE l.id = ?
        """, (librarian_id,))

        return db_cursor.fetchone()

@login_required
def librarian_details(request, librarian_id):
    if request.method == 'GET':
        librarian = get_librarian(librarian_id)

        template = 'librarians/detail.html'
        context = {
            'librarian': librarian,
            'library': librarian.location
        }

        return render(request, template, context)