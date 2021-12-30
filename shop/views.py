from django.shortcuts import render, get_object_or_404
from django.views import generic
from . import models


def home(request, category_slug=None):
    category_page = None
    products = None
    if category_slug != None:
        category_page = get_object_or_404(models.Category, slug=category_slug)
        products = models.Product.objects.filter(category=category_page, available=True)
    else:
        products = models.Product.objects.all().filter(available=True)
    return render(request, 'home.html', {'category':category_page, 'products': products})


class Index(generic.View):
    template_name = 'home.html'
    category_page = None
    products = None

    def get(self, rq, category_slug=None):
        if category_slug:
            category_page = get_object_or_404(models.Category, slug=category_slug)
            products = models.Product.objects.filter(calendar=category_page, available=True)
        else:
            products = models.Product.objects.all().filter(available=True)
        return render(rq, self.template_name, {'category': self.category_page, 'products': products})


class About(generic.View):
    template_name = 'base_generic.html'

    def get(self, rq):
        return render(rq, self.template_name)


