from django.shortcuts import render, redirect

from FruitiPedia.fruits.forms import CategoryOriginalForm, CreateFruitOriginalForm, EditFruitForm, DeleteFruitForm
from FruitiPedia.fruits.models import Fruit


def index(request):
    return render(request, "common/index.html")


def dashboard(request):
    fruits = Fruit.objects.all()

    context = {
        "fruits": fruits
    }

    return render(request, "common/dashboard.html", context)


def create_fruit(request):
    if request.method == "Get":
        forms = CreateFruitOriginalForm()

    else:
        forms = CreateFruitOriginalForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect("dashboard")

    context = {
        "form": forms
    }

    return render(request, "fruits/create-fruit.html", context)


def delete_fruit(request, pk):
    fruit = Fruit.objects.get(pk=pk)

    if request.method == "GET":
        form = DeleteFruitForm(instance=fruit)

    else:
        form = DeleteFruitForm(request.POST, instance=Fruit)
        fruit.delete()
        return redirect("dashboard")

    context = {
        "fruit": fruit,
        "form": form
    }

    return render(request, "fruits/delete-fruit.html", context)


def details(request, pk):
    fruits = Fruit.objects.get(pk=pk)

    context = {
        "fruit": fruits
    }

    return render(request, "fruits/details-fruit.html", context)


def edit_fruit(request, pk):
    fruit = Fruit.objects.get(pk=pk)

    if request.method == "GET":
        form = EditFruitForm(instance=fruit)

    else:
        form = EditFruitForm(request.POST, instance=fruit)

        if form.is_valid():
            form.save()
            return redirect("dashboard")

    context = {
        "fruit": fruit,
        "form": form
    }

    return render(request, "fruits/edit-fruit.html", context)


def create_category(request):
    if request.method == "GET":
        forms = CategoryOriginalForm()

    else:
        forms = CategoryOriginalForm(request.POST)

        if forms.is_valid():
            forms.save()
            return redirect("index")

    context = {
        "form": forms
    }

    return render(request, "categories/create-category.html", context)