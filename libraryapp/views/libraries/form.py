import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from libraryapp.models import Library
from ..connection import Connection

@login_required
def library_form(request):
    if request.method == 'GET':
        template = 'libraries/form.html'
        context = {
            'all_libraries': ""
        }

        return render(request, template, context)