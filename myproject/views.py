from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings

def home(request):
    return render(request, 'home.html')     

def portfolio(request):
    return render(request, 'portfolio.html')     

def about(request):
    return render(request, 'about.html')     

def contact(request):
    return render(request, 'contact.html')     

def skills(request):
    return render(request, 'skill.html')

def send_email(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        subject = f'New Contact Form Message from {name}'
        email_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

        try:
            send_mail(
                subject=subject,
                message=email_message,
                # from_email=settings.EMAIL_HOST_USER,
                from_email=email,
                recipient_list=['nitinsen70671@gmail.com'],
                fail_silently=False,
            )
            messages.success(request, 'Message sent successfully!')
        except Exception as e:
            print("Email failed:", e)
            messages.error(request, 'Failed to send message. Please try again.')

    return redirect('/#contact')



