import datetime

from django.db.models import Q
from django.shortcuts import render
from myfiles.models import *
# Create your views here.

def index(malumot):
    if 'name' in malumot.POST:
        ismi = malumot.POST.get('name')
        mail = malumot.POST.get('mail')
        mavzu = malumot.POST.get('subject')
        xabar = malumot.POST.get('message')
        vaqt = datetime.datetime.now()

        Murojaat(name=ismi, mail=mail, title=mavzu, text=xabar, date=vaqt).save()

    if 'soz' in malumot.POST:
        text = str(malumot.POST.get('soz'))
        text = text.strip()
        qidirish_p = Q(nomi__startswith = text) | Q(company_name__startswith = text) |\
                   Q(date__startswith = text) | Q(url__startswith = text) |\
                   Q(malumot__startswith = text) | Q(tur__nomi__startswith = text)
        works = Portfolio.objects.filter(qidirish_p)
        turlar = Type.objects.all()
        qidirish_s = Q(nomi__startswith= text) | Q(malumot__startswith = text)
        services = Service.objects.filter(qidirish_s)
        teams = Team.objects.all()
        lugat = {
            'works': works,
            "types": turlar,
            'services': services,
            'teams': teams
        }
        return render(malumot, 'index.html',lugat)


    elif malumot.method == "POST":
        mail = malumot.POST.get('mail')
        Subscribe(mail=mail).save()

    else:
        works = Portfolio.objects.all()
        turlar = Type.objects.all()
        services = Service.objects.all()
        teams = Team.objects.all()

        lugat = {
            'works': works,
            "types": turlar,
            'services': services,
            'teams' : teams
        }
        return render(malumot,'index.html',lugat)


def filter_index(malumot,id):
    if id=='0':
        works = Portfolio.objects.all()
    else:
        works = Portfolio.objects.filter(tur_id=id)
    turlar = Type.objects.all()
    services = Service.objects.all()
    teams = Team.objects.all()

    lugat = {
        'works': works,
        "types": turlar,
        'services': services,
        'teams': teams
    }
    return render(malumot, 'index.html', lugat)

def portfolio(malumot):
    if malumot.method == "POST":
        mail = malumot.POST.get('email')
        Subscribe(mail=mail).save()
    return render(malumot,'portfolio-details.html')


def inner_page(malumot):
    return render(malumot, 'inner-page.html')


def single_portfolio(malumot,id):
    work = Portfolio.objects.get(id=id)
    if malumot.method == "POST":
        mail = malumot.POST.get('email')
        Subscribe(mail=mail).save()
    return render(malumot,'portfolio-details.html',{'work':work})


def team(malumot):

    return render(malumot,'index.html')

def service(malumot):
    services = Service.objects.all()
    return render(malumot,'index.html',{'services': services})