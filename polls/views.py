from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
import os
import json

from .models import Question

def manifest(request):
    # Ruta absoluta al archivo manifest.json (ajusta según la estructura de tu proyecto)
    manifest_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'manifest.json')
    
    try:
        # Lee el archivo y devuelve su contenido como JSON
        with open(manifest_path, 'r', encoding='utf-8') as f:
            data = json.load(f)  # Carga el archivo como JSON
        
        # Devuelve la respuesta JSON
        return JsonResponse(data, safe=False)
    
    except FileNotFoundError:
        # Si el archivo no se encuentra, devuelve un error 404
        return HttpResponse("Archivo manifest.json no encontrado", status=404)
    
    except json.JSONDecodeError:
        # Si hay un error en el formato del JSON, devuelve un error 500
        return HttpResponse("Error al decodificar manifest.json", status=500)
        
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
