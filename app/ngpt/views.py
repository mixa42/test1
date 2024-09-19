import json, random
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.models import User
from . import models

from django.contrib.auth.views import LogoutView, LoginView
from django.shortcuts import redirect


class LoginView(LoginView):
    '''
        Переопределяется базовый класс джанго
        для автоматической регистрации нового пользователя при ошибке
    '''
    def dispatch(self, request, *args, **kwargs):
        if self.redirect_authenticated_user and self.request.user.is_authenticated:
            redirect_to = self.get_success_url()
            if redirect_to == self.request.path:
                raise ValueError(
                    "Redirection loop for authenticated user detected. Check that "
                    "your LOGIN_REDIRECT_URL doesn't point to a login page."
                )
            return HttpResponseRedirect(redirect_to)
        
        if request.method == 'POST' and not User.objects.filter(username=request.POST['username']).exists():
            User.objects.create_user(username=request.POST['username'], email=None,password=request.POST['password'], is_staff=1)        
        return super().dispatch(request, *args, **kwargs)


# @login_required
# def register_new(request, login, passw):
#     user =  User.objects.create_user(username=login, email=None,password=passw, is_staff=1)
#     request.user = user
#     return HttpResponseRedirect('/')

@login_required
def index(request):
    ''' 
        Главная страница куда попадает пользователь
        бизнес-логика проста, поэтому не вижу смысла выносить её отдельно
    '''
    questions = models.DialogLog.objects.filter(user=request.user).order_by('-dt_record')
    
    if request.method=='POST':
        form = json.loads(request.body.decode('utf-8'))
        if 'new_q' in form and form['new_q']!='' and form['new_q']!=None:
            qst = models.DialogLog.objects.create(user=request.user, question=form['new_q'], client_ip=None, answer= models.AnswersList[random.randrange(0, len(models.AnswersList)-1)])
            return render(request, 'question.html', {'qst': qst, 'new_qst': True})
            #return HttpResponse(json.dumps(form), content_type="application/json")

    if request.method=='GET':
        return render(request, 'quest_form.html', {'questions':questions, 'users_list': User.objects.filter(is_active=True).order_by('last_login')})


