import sqlite3
from django.shortcuts import render
from libraryapp.models import Library
from ..connection import Connection


def list_libraries(request):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        select
            l.id,
            l.title,
            l.address
        from libraryapp_library l
        """)

        all_libraries = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            lib = Library()
            lib.id = row["id"]
            lib.title = row["title"]
            lib.address = row["address"]

            all_libraries.append(lib)

    template_name = 'libraries/list.html'

    context = {
        'all_libraries': all_libraries
    }

    return render(request, template_name, context)