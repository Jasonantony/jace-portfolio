from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        send_mail(
            subject=f"Portfolio Message from {name}",
            message=message,
            from_email=email,
            recipient_list=["yourgmail@gmail.com"],
            fail_silently=False,
        )

    return render(request, "main/index.html")
