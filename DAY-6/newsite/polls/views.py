from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def about(request):
    context = {
        'name': 'Ahnsh Jaiswal',
        'bio': 'A passionate Full Stack Developer with a love for creating beautiful and functional web applications.',
        'skills': ['Python', 'Django', 'JavaScript', 'HTML/CSS', 'React', 'SQL', 'Git']
    }
    return render(request, 'about.html', context)


def contact(request):
    return render(request, 'contact.html')

