from django.shortcuts import render, redirect
from apps.about.models import Review
from .models import *


def main_page(request):

    url_data = request.POST
    if url_data:
        if 'type' in url_data and url_data['type']:
            if url_data['type'] == 'new_review':
                name = url_data['name']
                phone_number = url_data['phone_number']
                car_id = url_data['model_id']
                time = url_data['time']
                cars = Car.objects.filter(pk=car_id)
                if cars.exists():
                    car = cars.first()
                else:
                    return redirect('main')
                new_review = Review(
                    name=name,
                    phone_number=phone_number,
                    car=car,
                    time=time,
                )
                new_review.save()
                return redirect('main')

    context = {
        'brands': Brand.objects.filter(status='active')[:5],
        'cars': Car.objects.filter(status='active')[:8],
        'featured_cars': Car.objects.filter(status='active').filter(is_featured=True)[:6],
    }

    return render(request, 'main/main_page.html', context = context)


def brands(request):

    context = {
        'brands': Brand.objects.filter(status='active')
    }

    return render(request, 'main/brands.html', context = context)


def car_profile(request, pk):

    cars = Car.objects.filter(pk=pk)
    if cars.exists():
        car = cars.first()
    else:
        return redirect('main')

    url_data = request.POST
    if url_data:
        if 'type' in url_data and url_data['type']:
            if url_data['type'] == 'new_review':
                name = url_data['name']
                phone_number = url_data['phone_number']
                time = url_data['time']
                new_review = Review(
                    name=name,
                    phone_number=phone_number,
                    car=car,
                    time=time,
                )
                new_review.save()
                return redirect('car-profile', pk)

    context = {
        'car': car
    }

    return render(request, 'main/car-profile.html', context = context)
