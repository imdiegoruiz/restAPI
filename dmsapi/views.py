from __future__ import print_function
from django.shortcuts import render, get_object_or_404

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from .models import Document, Typification
from .serializers import DocumentSerializer, TypificationSerializer


@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'all_documents': '/',
        'Search by Name': '/?name=name',
        'Search by Typification': '/?typification=typification',
        'Add': '/create',
        'Update': '/update/pk',
        'Delete': '/document/pk/delete'
    }

    return Response(api_urls)


@api_view(['POST'])
def add_documents(request):
    document = DocumentSerializer(data=request.data)
    # validating for already existing data
    if Document.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
    if document.is_valid():
        document.save()
        return Response(document.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
def update_document(request, pk):
    document = Document.objects.get(pk=pk)
    data = DocumentSerializer(instance=document, data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def view_document(request, pk):
    document = Document.objects.get(pk=pk)
    data = DocumentSerializer(document, context={"request": request})

    if data:
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_document(request, pk):
    document = get_object_or_404(Document, pk=pk)
    document.delete()
    return Response(status=status.HTTP_202_ACCEPTED)


@api_view(['GET'])
def view_documents(request):
    # checking for the parameters from the URL
    documents = Document.objects.all()
    if request.query_params:
        documents = Document.objects.filter(**request.query_params.dict())
    # if there is something in documents else raise error
    if documents:
        data = DocumentSerializer(documents, many=True, context={"request": request})
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def add_typification(request):
    typification = TypificationSerializer(data=request.data)

    # validating for already existing data
    if Typification.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')

    if typification.is_valid():
        typification.save()
        return Response(typification.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def view_typifications(request):
    # checking for the parameters from the URL
    typifications = Typification.objects.all()
    if typifications:
        data = TypificationSerializer(typifications, many=True)
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
