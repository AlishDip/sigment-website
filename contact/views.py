from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json

@method_decorator(csrf_exempt, name='dispatch')
class ContactView(TemplateView):
    template_name = 'contact.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active'] = 'contact'
        return context
    def post(self, request, *args, **kwargs):
        
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        comment = request.POST.get('message')
        send_telegram_message([name,email,subject,comment],telegram_id = 1385019206)
        send_telegram_message([name,email,subject,comment],telegram_id = 996341004)
        return redirect('contact')


from telegram import Bot

bot_token = '6759512598:AAH2MywB0NecGRYhqvsgynoyyCYMA554Lew'
bot = Bot(token=bot_token)


def send_telegram_message(text, telegram_id):  
    message = f"Жаңа хабарлама \nАты: {text[0]}\nEmail: {text[1]}\nТақырыбы: {text[2]}\nХабарлама: {text[3]}"

    bot.send_message(chat_id=telegram_id, text=message)


