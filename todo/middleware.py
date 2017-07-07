from django.utils import timezone

class TimezoneMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        file = open('LoggingFile.txt', 'w')
        file.write(request.user.username)
        file.write(timezone.now().time().__str__())
        file.close()
        return self.get_response(request)
