from django.shortcuts import render


def index(request):
    return render(request, 'home/index.html')


def accounts_profile(request):
    current_user = request.user
    return render(request, 'accounts/profile.html', {current_user: current_user})
