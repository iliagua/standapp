# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def index(request):
	project_name = 'StandCalendar'
	author = 'Cameron Vargas'
	backend_project_name = 'api'
	backend_postgres_db_name = 'db_postgres_backend'
	backend_postgres_username = 'admin'
	frontend_project_name = 'calendar'
	frontend_project_description = 'Django-React project for generating and a calendar and scheduler for public witnessing stands'
	frontend_app_style_slug = 'calendar_style'
	frontend_app_slug = 'calendar'
	date_generated = 'July 16, 2018 - 18:01'

	context = {
		'project': project_name,
		'author': author,
		'date_generated': date_generated,
		'backend_name': backend_project_name,
		'backend_db_name': backend_postgres_db_name,
		'backend_db_user': backend_postgres_username,
		'frontend_name': frontend_project_name,
		'frontend_desc': frontend_project_description,
		'frontend_app_style_slug': frontend_app_style_slug,
		'frontend_app_slug': frontend_app_slug,
	}

	return render(request, 'index.html', context)
