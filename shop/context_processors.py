from . import models
from .views import _cart_id


def counter(request):
	item_count = 0
	if 'admin' in request.path:
		return {}
	else:
		try:
			cart = models.Cart.objects.filter(cart_id=_cart_id(request))
			cart_items = models.CartItem.objects.all().filter(cart=cart[:1])
			for cart_item in cart_items:
				item_count += cart_item.quantity
		except models.Cart.DoesNotExist:
			item_count = 0
	return dict(item_count=item_count)


def menu_links(request):
	links = models.Category.objects.all()
	return dict(links=links)
