from django.shortcuts import render, redirect, get_object_or_404
from store.models import Product
from .models import Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse

def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def add_cart(request, product_id):
    current_user = request.user
    product = Product.objects.get(id=product_id)  # Obtener el producto

    # Si el usuario está autenticado
    if current_user.is_authenticated:
        try:
            # Intentar obtener el item del carrito para ese producto y usuario
            cart_item = CartItem.objects.get(product=product, user=current_user)
            cart_item.quantity += 1  # Incrementar la cantidad
            cart_item.save()
        except CartItem.DoesNotExist:
            # Si no existe, crear un nuevo item en el carrito
            cart_item = CartItem.objects.create(
                product=product,
                quantity=1,
                user=current_user,
            )
            cart_item.save()
        return redirect('cart')

    # Si el usuario no está autenticado
    else:
        try:
            cart = Cart.objects.get(cart_id=_cart_id(request))  # Obtener el carrito usando el cart_id de la sesión
        except Cart.DoesNotExist:
            cart = Cart.objects.create(
                cart_id=_cart_id(request)
            )
        cart.save()

        try:
            # Intentar obtener el item del carrito para ese producto y carrito (anónimo)
            cart_item = CartItem.objects.get(product=product, cart=cart)
            cart_item.quantity += 1  # Incrementar la cantidad
            cart_item.save()
        except CartItem.DoesNotExist:
            # Si no existe, crear un nuevo item en el carrito
            cart_item = CartItem.objects.create(
                product=product,
                quantity=1,
                cart=cart,
            )
            cart_item.save()
        return redirect('cart')


def remove_cart(request, product_id, cart_item_id):
    product = get_object_or_404(Product, id=product_id)
    
    try:
        if request.user.is_authenticated:
            # Si el usuario está autenticado, obtenemos el item del carrito basado en el usuario
            cart_item = CartItem.objects.get(product=product, user=request.user, id=cart_item_id)
        else:
            # Si no está autenticado, usamos el carrito de la sesión
            cart = Cart.objects.get(cart_id=_cart_id(request))
            cart_item = CartItem.objects.get(product=product, cart=cart, id=cart_item_id)
        
        # Si la cantidad es mayor a 1, la decrementamos
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            # Si la cantidad es 1 o menor, eliminamos el item del carrito
            cart_item.delete()
    except CartItem.DoesNotExist:
        # Manejamos el caso donde el cart_item no exista, aunque no haríamos nada en este caso
        pass
    
    return redirect('cart')


def remove_cart_item(request, product_id, cart_item_id):
    product = get_object_or_404(Product, id=product_id)
    if request.user.is_authenticated:
        cart_item = CartItem.objects.get(product=product, user=request.user, id=cart_item_id)
    else:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_item = CartItem.objects.get(product=product, cart=cart, id=cart_item_id)
    cart_item.delete()
    return redirect('cart')


def cart(request, total=0, quantity=0, cart_items=None):
    try:
        tax = 0
        grand_total = 0
        if request.user.is_authenticated:
            cart_items = CartItem.objects.filter(user=request.user, is_active=True)
        else:
            cart = Cart.objects.get(cart_id=_cart_id(request))
            cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity
        tax = (2 * total)/100
        grand_total = total + tax
    except ObjectDoesNotExist:
        pass #just ignore

    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
        'tax'       : tax,
        'grand_total': grand_total,
    }
    return render(request, 'store/cart.html', context)


@login_required(login_url='login')
def checkout(request, total=0, quantity=0, cart_items=None):
    try:
        tax = 0
        grand_total = 0
        if request.user.is_authenticated:
            cart_items = CartItem.objects.filter(user=request.user, is_active=True)
        else:
            cart = Cart.objects.get(cart_id=_cart_id(request))
            cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity
        tax = (2 * total)/100
        grand_total = total + tax
    except ObjectDoesNotExist:
        pass #just ignore

    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
        'tax'       : tax,
        'grand_total': grand_total,
    }
    return render(request, 'store/checkout.html', context)