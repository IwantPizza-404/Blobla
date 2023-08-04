from django.shortcuts import render

def error_404(request, exception):
    data = {}
    response = render(request, '404.html', data)
    response.status_code = 404
    return response


def error_500(request):
    data = {}
    response = render(request, '500.html', data)
    response.status_code = 500
    return response