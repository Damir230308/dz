from wavy import rendering
from workers import workers


def all_view(request):
    return '200 OK', rendering('index.html', workers=workers)


def directorfbi_view(request):
    return '200 OK', rendering('worker.html', workers=workers[0])


def cit_view(request):
    return '200 OK', rendering('worker.html', workers=workers[1])


def cit2_view(request):
    return '200 OK', rendering('worker.html', workers=workers[2])


def about(request):
    return '200 OK', "About"