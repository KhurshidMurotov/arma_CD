from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from apps.about.models import Review
from .models import Brand, Car  # Explicit imports


@require_POST
def handle_review(request, car_id=None):
    """Process review form submission"""
    name = request.POST.get('name')
    phone_number = request.POST.get('phone_number')
    time = request.POST.get('time')
    
    if not all([name, phone_number, time]):
        return redirect('main')
    
    car = None
    if car_id:
        car = get_object_or_404(Car, pk=car_id)
    
    Review.objects.create(
        name=name,
        phone_number=phone_number,
        car=car,
        time=time,
    )
    
    return redirect('car-profile', pk=car_id) if car_id else redirect('main')


def main_page(request):
    if request.method == 'POST' and request.POST.get('type') == 'new_review':
        return handle_review(request)
    
    context = {
        'brands': Brand.objects.filter(status='active')[:5],
        'cars': Car.objects.filter(status='active')[:8],
        'featured_cars': Car.objects.filter(
            status='active', 
            is_featured=True
        )[:6],
    }
    return render(request, 'main/main_page.html', context)


def brands(request):
    context = {
        'brands': Brand.objects.filter(status='active')
    }
    return render(request, 'main/brands.html', context)


def car_profile(request, pk):
    car = get_object_or_404(Car, pk=pk)
    
    if request.method == 'POST' and request.POST.get('type') == 'new_review':
        return handle_review(request, car.id)
    
    context = {
        'car': car,
        'reviews': Review.objects.filter(car=car)[:10]  
    }
    return render(request, 'main/car-profile.html', context)