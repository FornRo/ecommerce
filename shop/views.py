from django.shortcuts import render
from django.views import generic


class Index(generic.View):
    template_name = 'home.html'

    def get(self, rq):
        return render(rq, self.template_name)


class About(generic.View):
    template_name = 'base_generic.html'

    def get(self, rq):
        return render(rq, self.template_name)


