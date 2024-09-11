from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Observation
from .forms import UserForm, UserRequest, ContactForm, Spinar
from django.core.mail import send_mail, BadHeaderError
from myproject.settings import RECIPIENTS_EMAIL, DEFAULT_FROM_EMAIL
from .radius import counting

#import logging


#logger = logging.getLogger(__name__)

def transients(request):
    observations = Observation.objects.filter()
    number = observations.count()
    if number % 10 == 1 and number != 11:
        phrase = f'Найден 1 транзиент'
    elif number % 10 in [2,3,4] and (number < 10 or number > 20):
        phrase = f'Найдено {number} транзиента'
    else:
        phrase = f'Найдено{number} транзиентов'

    return render(request, 'transients.html', {'observations':observations, 'phrase':phrase})

def transient(request, number):
    observation = get_object_or_404(Observation, pk = number)
    return render(request, 'transient.html', {'observation':observation})

def edit(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            transient_type = form.cleaned_data['transient_type']
            obs_or_lim = form.cleaned_data['obs_or_lim']
            DataTime = form.cleaned_data['DataTime']
            Ra = form.cleaned_data['Ra']
            Dec = form.cleaned_data['Dec']
            max_limit = form.cleaned_data['max_limit']
            max_magnitude = form.cleaned_data['max_magnitude']
            lightcurve = form.cleaned_data['lightcurve']
            pictures = form.cleaned_data['pictures']
            telescope = form.cleaned_data['telescope']
            publication = form.cleaned_data['publication']
            if_we_first = form.cleaned_data['if_we_first']
            time_from_notice = form.cleaned_data['time_from_notice']
            satellite = form.cleaned_data['satellite']
            discoverer = form.cleaned_data['discoverer']
            observation = Observation(name = name, transient_type = transient_type, obs_or_lim =  obs_or_lim, DataTime = DataTime,
                                      Ra = Ra, Dec = Dec, max_limit = max_limit, max_magnitude = max_magnitude, lightcurve = lightcurve,
                                      pictures = pictures, telescope = telescope, publication = publication, if_we_first = if_we_first,
                                      time_from_notice = time_from_notice, satellite = satellite, discoverer = discoverer)
            observation.save()
            return redirect(ok)
    else:
        form = UserForm()
    return render(request, 'edit.html', {'form':form})

def statistic(request):
    if request.method == 'POST':
        form = UserRequest(request.POST)
        if form.is_valid():
            transient_type = form.cleaned_data['transient_type']
            obs_or_lim = form.cleaned_data['obs_or_lim']
            DataTime = form.cleaned_data['DataTime']
            telescope = form.cleaned_data['telescope']
            publication = form.cleaned_data['publication']
            if_we_first = form.cleaned_data['if_we_first']
            satellite = form.cleaned_data['satellite']
            discoverer = form.cleaned_data['discoverer']
            numbers = Observation.objects.filter()
            if transient_type == '':
                numbers1 = numbers
            else:
                numbers1 = numbers.filter(transient_type = transient_type)
            if obs_or_lim == 'o':
                numbers2 = numbers1
            else:
                numbers2 = numbers1.filter(obs_or_lim = obs_or_lim)
            numbers3 = numbers2
            if telescope == '':
                numbers4 = numbers3
            else:
                numbers4 = numbers3.filter(telescope = telescope)
            if publication == None:
                numbers5 = numbers4
            else:
                numbers5 = numbers4.filter(publication = publication)
            if if_we_first == True:
                numbers6 = numbers5
            else:
                numbers6 = numbers5.filter(if_we_first = if_we_first)
            if satellite == '':
                numbers7 = numbers6
            else:
                numbers7 = numbers6.filter(satellite = satellite)
            if discoverer == '':
                numbers8 = numbers7
            else:
                numbers8 = numbers7.filter(discoverer = discoverer)
            number = numbers8.count()
            if number % 10 == 1 and number != 11:
                phrase = f'Найден 1 транзиент'
            elif number % 10 in [2,3,4] and (number < 10 or number > 20):
                phrase = f'Найдено {number} транзиента'
            else:
                phrase = f'Найдено{number} транзиентов'
        return render(request, 'transients.html', {'observations':numbers8, 'phrase':phrase})
    else:
        form = UserRequest()
        return render(request, 'edit.html', {'form':form})

def ok(request):
    return HttpResponse("Объект успешно добавлен!")

def oke(request):
    return HttpResponse("Запрос отправлен.")

def index(request):
    return render(request, 'index.html')

def send(request):
    # если метод GET, вернем форму
    if request.method == 'GET':
        form = ContactForm()
    elif request.method == 'POST':
        # если метод POST, проверим форму и отправим письмо
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(f'{subject} от {from_email}', message,
                          DEFAULT_FROM_EMAIL, RECIPIENTS_EMAIL)
            except BadHeaderError:
                return HttpResponse('Ошибка в теме письма.')
            return redirect('oke')
    else:
        return HttpResponse('Неверный запрос.')
    return render(request, "send.html", {'form': form})

def success_view(request):
    return HttpResponse('Приняли! Спасибо за вашу заявку.')

def spinar(request):
    if request.method == 'POST':
        form = Spinar(request.POST)
        if form.is_valid():
            m = form.cleaned_data['m']
            ao = form.cleaned_data['ao']
            am = form.cleaned_data['am']
            data = counting(m, ao, am)
            return render(request, "spinar.html", {'data': data})
    else:
        form = Spinar()
    return render(request, 'edit.html', {'form':form})


