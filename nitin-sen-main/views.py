from django.core.mail import send_mail, EmailMessage
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings


def portfolio(request):
    return render(request, 'portfolio.html')     


def send_email(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        subject = f'New Contact Form Message from {name}'
        email_message_content = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

        try:
            email_msg = EmailMessage(
                subject=subject,
                body=email_message_content,
                from_email=settings.EMAIL_HOST_USER, # Sender must be the authenticated user
                to=[settings.EMAIL_HOST_USER],       # Send to yourself
                reply_to=[email],                    # Reply to the visitor
            )
            email_msg.send(fail_silently=False)
            
            messages.success(request, 'Message sent successfully!')
        except Exception as e:
            print("Email failed:", e)
            messages.error(request, f'Failed to send message: {e}')

    return redirect('/')



