from django.shortcuts import render
from django.views.generic import TemplateView
from openai import OpenAI
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
client = OpenAI()


@method_decorator(csrf_exempt, name='dispatch')
class GPTView(TemplateView):
    template_name = 'gpt.html'

    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body.decode('utf-8'))
            url = data.get('url', None)
            
            if url:
                print(url)
                response = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {
                            "role": "user",
                            "content": [
                                {
                                    "type": "text",
                                    "text": "What are in these images? In kazakh language",
                                },
                                {
                                    "type": "image_url",
                                    "image_url": {
                                        "url": f"{url}",
                                    },
                                },
                            ],
                        }
                    ],
                    max_tokens=300,
                )
                print(response.choices[0])
                # Extract the content from the message object correctly
                message_content = response.choices[0].message.content
                return JsonResponse({'text': message_content}, status=200)
            else:
                return JsonResponse({'error': 'URL not found in the request data'}, status=400)
        
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
        except Exception as e:
            print(e)
            return JsonResponse({'error': str(e)}, status=500)