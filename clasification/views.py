from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from .classification import predict


@method_decorator(csrf_exempt, name='dispatch')
class ClassificationView(TemplateView):
    template_name = 'classification.html'

    def post(self, request):
        uploaded_file = request.FILES['file']
        if uploaded_file:
            image_bytes = uploaded_file.read()
            class_name = predict(image_bytes)
            print(class_name)
            return JsonResponse({'class': class_name})
        else:
            return JsonResponse({'message': 'No file uploaded'})


 
