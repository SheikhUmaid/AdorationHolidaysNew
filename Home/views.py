from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from Home import models
from django.core.mail import send_mail


# Create your views here.
@csrf_exempt
def index(request):
    if request.method == 'POST':
        if request.POST.get('type') == "contact":
            fname = request.POST.get('fname')
            lname = request.POST.get('lname', '----')
            email = request.POST.get('email')
            message = request.POST.get('message')
            contact = models.ContactSubmit.objects.create(fname=fname,
                                                          lname=lname,
                                                          email=email,
                                                          message=message)
            contact.save()
            Message_to_send = f'Hello {fname},\n\nThank you for contacting us. We will get back to you as soon as possible. Be sure you provided the proper information.\n\nName: {fname}\n\nEmail: {email}\n\nRegards,\nAdoration Team'
            try:
                send_mail(
                    "Adoration Holidays",
                    Message_to_send,  #Message to send
                    'info@adorationholidays.com',  # from email
                    [email, 'sheikhumaid@pm.me'],  # to email Poduction
                    # [email], # to email
                    fail_silently=False,
                )
                contact.mail_recieved = True
                contact.save()
            except Exception as e:
                contact.mail_error = str(e)
                contact.save()
        elif request.POST.get('type') == "modelform":
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            destination = request.POST.get('destination')
            model = models.ModelSubmit.objects.create(name=name,
                                                      email=email,
                                                      phone=phone,
                                                      destination=destination)
            model.save()
            Message_to_send = f'Hello {name},\n\nThank you for contacting us. We will get back to you as soon as possible. Be sure you provided the proper information.\n\nName: {name}\nPhone: {phone}\nEmail: {email}\n\nRegards,\nAdoration Team'
            try:
                send_mail(
                    "Adoration Holidays",
                    Message_to_send,  #Message to send
                    'info@adorationholidays.com',  # from email
                    [email, 'sheikhumaid@pm.me'],  # to email Poduction
                    # [email], # to email
                    fail_silently=False,
                )
                model.mail_recieved = True
                model.save()
            except Exception as e:
                model.mail_error = str(e)
                model.save()



              
        elif request.POST.get('type') == "hero":
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            hero = models.HeroSubmit.objects.create(name=name,
                                                    email=email,
                                                    phone=phone)
            hero.save()
            Message_to_send = f'Hello {name},\n\nThank you for contacting us. We will get back to you as soon as possible. Be sure you provided the proper information.\n\nName: {name}\nPhone: {phone}\nEmail: {email}\n\nRegards,\nAdoration Team'
            try:
                send_mail(
                    "Adoration Holidays",
                    Message_to_send,  #Message to send
                    'info@adorationholidays.com',  # from email
                    [email, 'sheikhumaid@pm.me'],  # to email Poduction
                    # [email], # to email
                    fail_silently=False,
                )
                hero.mail_recieved = True
                hero.save()
            except Exception as e:
                hero.mail_error = str(e)
                hero.save()

    return render(request, "index.html")
