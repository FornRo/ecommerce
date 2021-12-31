from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from . import models
from django.contrib.auth.models import Group, User
from . import forms


class Index(generic.View):
    template_name = 'home.html'
    category_page = None
    products = None

    def get(self, request, category_slug=None, *args, **kwargs):
        if category_slug:
            self.category_page = get_object_or_404(models.Category, slug=category_slug)
            self.products = models.Product.objects.filter(category=self.category_page, available=True)
        else:
            self.products = models.Product.objects.all().filter(available=True)
        return render(request, self.template_name, {'category': self.category_page, 'products': self.products})


class About(generic.View):
    template_name = 'base_generic.html'

    def get(self, rq):
        return render(rq, self.template_name)


class ProductView(generic.View):
    template_name = 'product.html'
    category_slug = None
    product_slug = None
    model = models.Product

    def get(self, request, category_slug, product_slug):
        try:
            product = self.model.objects.get(category__slug=category_slug, slug=product_slug)
        except Exception as error_:
            raise error_
        return render(request, self.template_name, {'product': product})


class CartView(generic.View):
    template_name = 'cart.html'

    def get(self, rq):
        context = {}
        return render(rq, self.template_name, context)


def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


class Add_CartView(generic.View):
    def get(self, request, product_id):
        product = models.Product.objects.get(id=product_id)

        try:
            cart = models.Cart.objects.get(cart_id=_cart_id(request))
        except models.Cart.DoesNotExist:
            cart = models.Cart.objects.create(cart_id=_cart_id(request))
            cart.save()

        try:
            cart_item = models.CartItem.objects.get(product=product, cart=cart)
            if cart_item.quantity < cart_item.product.stock:
                cart_item.quantity += 1
            cart_item.save()
        except models.CartItem.DoesNotExist:
            cart_item = models.CartItem.objects.create(product=product, quantity=1, cart=cart)
            cart_item.save()

        return redirect('shop:cart_detail')


class CartDetailView(generic.View):
    def get(self, request, total=0, counter=0, cart_items=None):
        try:
            cart = models.Cart.objects.get(cart_id=_cart_id(request))
            cart_items = models.CartItem.objects.filter(cart=cart, active=True)
            for cart_item in cart_items:
                total += (cart_item.product.price * cart_item.quantity)
                counter += cart_item.quantity

        except ObjectDoesNotExist:
            pass

        return render(request, 'cart.html', dict(cart_items=cart_items, total=total, counter=counter))

# __________________________________________________
def cart_remove(request, product_id):
    cart = models.Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(models.Product, id=product_id)
    cart_item = models.CartItem.objects.get(product=product, cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('shop:cart_detail')


def cart_remove_product(request, product_id):
    cart = models.Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(models.Product, id=product_id)
    cart_item = models.CartItem.objects.get(product=product, cart=cart)
    cart_item.delete()
    return redirect('shop:cart_detail')


def signUpView(request):
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = forms.SignUpForm()
    return render(request, 'signup.html', {'form': form})

# ___________________________________
# _______________________________++++

def loginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('shop:home')
            else:
                return redirect('shop:signup')

    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# ___________________________________

# ___________________________________

# from django.contrib.auth.views import LoginView as DjangoLoginView
#
# class LoginView(DjangoLoginView):
#     template_name = 'login.html'
#     def post(self, request, *args, **kwargs):



def signoutView(request):
    logout(request)
    return redirect('shop:login')



