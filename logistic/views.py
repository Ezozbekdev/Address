from time import timezone

from django.shortcuts import render, redirect
from .models import About_Us, Services, Vehicles, Testimonials, Contact, Newsletter, Logistic, Address
from .forms import ContactForm, Subs, logistic


def index(request):
    about = About_Us.objects.all()
    service = Services.objects.all()
    vehicTruck = Vehicles.Truck.objects.all()
    vehicAir = Vehicles.AirFreight.objects.all()
    vehicRail = Vehicles.RailFreight.objects.all()
    test = Testimonials.Test.objects.all()
    testR = Testimonials.Reail.objects.all()
    address = Address.objects.all()

    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            cret = Contact.objects.create(
                name=data['name'],
                email=data['email'],
                phone_number=data['phone_number'],
                message=data['message'],
            )

    if request.method == 'GET':
        form = Subs()
    else:
        form = Subs(request.POST)
        if form.is_valid():
                data = form.cleaned_data
                cret = Newsletter.objects.create(
                    email=data['email']
                )

    if request.method == 'GET':
        form = logistic()
    else:
        form = logistic(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            cret = Logistic.objects.create(
                location=data['location'],
                to_destination=data['to_destination'],
                email=data['email'],
                number=data['number'],
            )


    context = {
        'about': about,
        'service': service,
        'veh': vehicTruck,
        'vehAir': vehicAir,
        'vehRail': vehicRail,
        'test': test,
        'testR': testR,
        'form': form,
        'address': address
    }
    return render(request, 'all/index.html', context)
