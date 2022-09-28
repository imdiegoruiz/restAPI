from django.shortcuts import render, get_object_or_404

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import serializers
from rest_framework import status
from dmsapi.models import Document, Typification
from cart.cart import Cart
import json


@api_view(['POST'])
def cart_add(request, id):
    cart = Cart(request)
    product = Document.objects.get(id=id)
    if product:
        cart.add(product=product)
        return Response(status=status.HTTP_201_CREATED)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def item_clear(request, id):
    cart = Cart(request)
    product = Document.objects.get(id=id)
    cart.remove(product)
    return Response(status=status.HTTP_202_ACCEPTED)


@api_view(['POST'])
def item_increment(request, id):
    cart = Cart(request)
    product = Document.objects.get(id=id)
    cart.add(product=product)
    return Response(status=status.HTTP_201_CREATED)


@api_view(['POST'])
def item_decrement(request, id):
    cart = Cart(request)
    product = Document.objects.get(id=id)
    cart.decrement(product=product)
    # return all items cart-detail
    return Response(status=status.HTTP_202_ACCEPTED)


@api_view(['POST'])
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return Response(status=status.HTTP_202_ACCEPTED)


@api_view(['GET'])
def cart_detail(request):
    print(request.user.id)
    total_amt = 0
    for id, item in request.session['cart'].items():
        total_amt += int(item['quantity']) * float(item['price'])
    data = request.session['cart'].items()
    return Response(data)
