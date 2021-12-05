from django.shortcuts import render
from django.http import HttpResponse

project_list = [
    {'id': 1,
     'title': 'E-commers',
     'description': 'Fool function internet shop'},
    {'id': 2,
     'title': 'E-learning',
     'description': 'Web portal for internet education'},
    {'id': 3,
     'title': 'News portal',
     'description': 'The breaking news site'}
]

def projects(request):
    page = 'projects'
    projects_quantity = len(project_list)

    return render(request, 'projects/projects.html', {'page': page, 'projects_quantity': projects_quantity, 'projects': project_list})

def project(request, pk):
    project_obj = None
    for i in project_list:
        if i['id'] == pk:
            project_obj = i

    return render(request, 'projects/single-project.html', {'project': project_obj})


