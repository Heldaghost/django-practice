from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from phone_book.models import *
from phone_book.serializers import PhoneNoteSerializer


@csrf_exempt
def phone_notes_list(request):
    if request.method == 'GET':
        notes = PhoneNote.objects.all()
        serializer = PhoneNoteSerializer(notes, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PhoneNoteSerializer(data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def note_detail(request, pk):
    try:
        note = PhoneNote.objects.get(pk=pk)
    except PhoneNote.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PhoneNoteSerializer(note)
        return JsonResponse(data=serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PhoneNoteSerializer(note, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return  JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        note.delete()
        return HttpResponse(status=204)