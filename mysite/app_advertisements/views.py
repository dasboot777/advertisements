# from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Advertisement
from .forms import AdvertisementForm
from django.core.handlers.wsgi import WSGIRequest

def index(request):
    # return HttpResponse('Все хорошо!')
    advertisements = Advertisement.objects.all()
    context = {
        'advertisements': advertisements
    }
    return render(request, 'index.html', context)

def top_sellers(request):
    return render(request, 'top-sellers.html')

def advertisement_post(request: WSGIRequest):

    if request.method == "POST":
        form = AdvertisementForm(request.POST, request.FILES) #передали данные в форму
        if form.is_valid(): #проверяем правильность заполнения данных
            adv = Advertisement(**form.cleaned_data) #передаем данные пользователя в БД
            adv.user = request.user  # узнаем пользователя
            adv.save()#сохраняем запись
            return redirect(#переадресация на главную страниуц
                reverse("")
            )
        else: #get
            form = AdvertisementForm()  # экземпляр формы
        context = {
                'form': form
        }

        return render(request, 'advertisement-post.html', context)

def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

def profile(request):
    return render(request, 'profile.html')

# def indexhtml(request):
#     return render(request, 'index.html')










