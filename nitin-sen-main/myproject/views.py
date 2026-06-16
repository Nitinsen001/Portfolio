from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import redirect, render


def portfolio(request):
    return render(request, "portfolio.html")


def send_email(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        subject = f"New Contact Form Message from {name}"
        email_message_content = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

        try:
            email_msg = EmailMessage(
                subject=subject,
                body=email_message_content,
                from_email=settings.EMAIL_HOST_USER,
                to=[settings.EMAIL_HOST_USER],
                reply_to=[email] if email else None,
            )
            email_msg.send(fail_silently=False)
            messages.success(request, "Message sent successfully!")
        except Exception as e:
            messages.error(request, f"Failed to send message: {e}")

    return redirect("/")


def handler404(request, exception):
    return HttpResponse("404 - Page not found", status=404)


def handler500(request):
    return HttpResponse("500 - Server error", status=500)

