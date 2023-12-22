from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from .models import Profile
from datetime import datetime
from django.contrib import messages

# Create your views here.
# Password for User yogesh - password admin1234
def index(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect("/login")
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        registration = request.POST.get('registration')
        phone = request.POST.get('phone')
        car_meter = request.POST.get('car_meter')
        model = request.POST.get('model')
        vin = request.POST.get('vin')
        address = request.POST.get('address')
        engine_tune = request.POST.get('engine_tune')
        engine_filter = request.POST.get('engine_filter')
        air_filter = request.POST.get('air_filter')
        spark_plug = request.POST.get('spark_plug')
        fuel_filter = request.POST.get('fuel_filter')
        injector = request.POST.get('injector')
        throttle_body = request.POST.get('throttle_body')
        balancing = request.POST.get('balancing')
        alignment = request.POST.get('alignment')
        tyre_rotation = request.POST.get('tyre_rotation')
        gear_oil = request.POST.get('gear_oil')
        coolant = request.POST.get('coolant')
        
        index = Profile(username=username,email=email,
                          registration=registration,
                          phone=phone, car_meter=car_meter, model=model, vin=vin, address=address,
                          engine_tune=engine_tune,
                          engine_filter=engine_filter, air_filter=air_filter, spark_plug=spark_plug,
                          fuel_filter=fuel_filter,
                          injector=injector, throttle_body=throttle_body, balancing=balancing,
                          alignment=alignment, tyre_rotation=tyre_rotation, gear_oil=gear_oil,coolant=coolant,
                          date=datetime.today())
        index.save()
        messages.success(request, "Your message has been sent")

    return render(request, 'index.html')

def loginUser(request):
    if request.method =="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        # Check if user has entered correct credentials
        user = authenticate(username=username, password=password)
        if user is not None:
            # A backend authenticated the credentials
            login(request,user)
            return redirect("/")
        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')

    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")

def about(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'about.html')

def contact(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect("/login")

    return render(request, 'contact.html')

def service(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'service.html')
