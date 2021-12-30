from django.shortcuts import render, get_object_or_404
from django.views import generic
from . import models


class Index(generic.View):
    template_name = 'home.html'
    category_page = None
    products = None

    def get(self, request, category_slug=None, *args, **kwargs):
        if category_slug:
            print(category_slug)
            category_page = get_object_or_404(models.Category, slug=category_slug)
            self.products = models.Product.objects.filter(category=self.category_page, available=True)
        else:
            self.products = models.Product.objects.all().filter(available=True)
        return render(request, self.template_name, {'category': self.category_page, 'products': self.products})


class About(generic.View):
    template_name = 'base_generic.html'

    def get(self, rq):
        return render(rq, self.template_name)


