from django.shortcuts import render
from django.views import View

class BobSession(View):
    def get(self, request):
        return render(request, 'bob/index.html')
    
    def post(self, request):
        name = request.POST['bobname'].title()
        user_names = request.session.get('usernames', {})
        if not user_names:
            request.session['usernames'] = {}

        if name in user_names:
            return render(request, 'bob/name.html', {'name': name})
        
        else:
            user_names[name] = True

        request.session['usernames'] = user_names
        return render(request, 'bob/index.html')
