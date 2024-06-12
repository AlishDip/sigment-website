from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from .prediction_text import predict_text


@method_decorator(csrf_exempt, name='dispatch')
class PredictionView(TemplateView):
    template_name = 'prediction.html'
    def post(self, request):
        uploaded_file = request.FILES['file']
        if uploaded_file:
            image_bytes = uploaded_file.read()
            text = predict_text(image_bytes)
            print(text)
            return JsonResponse({'text': text})
        else:
            return JsonResponse({'message': 'No file uploaded'})
