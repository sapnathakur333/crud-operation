
from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth import (
    login,
    logout,
    authenticate
)

from django.contrib.auth.decorators import login_required

from django.core.paginator import Paginator

from .forms import CarForm, SimpleSignupForm

from .models import Car

# SIGNUP
def signup_view(request):

    if request.method == 'POST':

        form = SimpleSignupForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            return redirect('car_list')

    else:

        form = SimpleSignupForm()

    return render(
        request,
        'signup.html',
        {'form': form}
    )



# LOGIN
def login_view(request):

    if request.method == "POST":

        username = request.POST.get("username")

        password = request.POST.get("password")


        user = authenticate(
            request,
            username=username,
            password=password
        )


        if user is not None:

            login(request, user)

            return redirect("car_list")

        else:

            return render(
                request,
                "login.html",
                {
                    "error": "Invalid Username or Password"
                }
            )

    return render(request, "login.html")



# LOGOUT
def logout_view(request):

    logout(request)

    return redirect("login")



# CAR LIST
@login_required
def car_list(request):

    cars = Car.objects.filter(
        user=request.user
    ).order_by("-id")


@login_required
def car_list(request):

    cars = Car.objects.filter(
        user=request.user
    ).order_by("-id")


    # SEARCH

    search = request.GET.get("q")

    if search:

        cars = cars.filter(
            car_name__icontains=search
        ) | cars.filter(
            car_model__icontains=search
        ) | cars.filter(
            car_color__icontains=search
        ) | cars.filter(
            car_price__icontains=search
        )


    # PAGINATION

    paginator = Paginator(cars, 3)

    page_number = request.GET.get("page")

    page_obj = paginator.get_page(page_number)


    return render(
        request,
        'car_list.html',
        {
            'page_obj': page_obj
        }
    )



# CREATE
@login_required
def car_create(request):

    if request.method == 'POST':

        form = CarForm(request.POST)

        if form.is_valid():

            car = form.save(commit=False)

            car.user = request.user

            car.save()

            return redirect('car_list')

    else:

        form = CarForm()

    return render(
        request,
        'car_form.html',
        {'form': form}
    )



# EDIT
@login_required
def car_edit(request, id):

    car = get_object_or_404(
        Car,
        id=id,
        user=request.user
    )

    if request.method == "POST":

        form = CarForm(
            request.POST,
            instance=car
        )

        if form.is_valid():

            form.save()

            return redirect("car_list")

    else:

        form = CarForm(instance=car)

    return render(
        request,
        "car_form.html",
        {
            "form": form
        }
    )



# DELETE
@login_required
def car_delete(request, id):

    car = get_object_or_404(
        Car,
        id=id,
        user=request.user
    )

    car.delete()

    return redirect("car_list")

