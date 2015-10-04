from django.shortcuts import render
from googleapiclient import discovery
from spotifykodiweb import settings
from django.http import JsonResponse


def index(request):
    return render(request, 'home/index.html')


def accounts_profile(request):
    current_user = request.user
    return render(request, 'accounts/profile.html', {'current_user': current_user})


def get_auth_url(request):
    # TODO: Generate new request ID (uuid)
    long_url = 'http://my.long.url.com/12345678901234567890'
    service = discovery.build('urlshortener', 'v1', developerKey=settings.GOOGLE_API_KEY)

    body = {'longUrl': long_url}
    url_resource = service.url()
    response = url_resource.insert(body=body).execute()
    return JsonResponse(response)

# def start_auth(request, request_id):
# Requests.find(request_id)
