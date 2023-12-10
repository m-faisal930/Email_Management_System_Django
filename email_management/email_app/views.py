from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .models import Contact
# Create your views here.

def index(request):
    return render(request, 'index.html')
def add_contact(request):
    return render(request, 'add_contact.html')
def see_contact(request):
    contacts = Contact.objects.all()
    return render(request, 'see_contact.html', {'contacts': contacts})
def send_message(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        subject = request.POST.get('subject')
        from_email = settings.EMAIL_HOST_USER
        list = Contact.objects.all()
        recipient_list = [contact.email for contact in list]
        recipient_names = [Contact.name for name in list]
        # recipient_list = ["redmindigo@gmail.com", "faisal.mr333@gmail.com", "faisal.muhammad7363@gmail.com"]
        for i in range(len(recipient_list)-1):
            message = "Dear " + str(recipient_names[i]) + '\n' + message
            send_mail(subject, message, from_email, [recipient_list[i]], "Muhammad Faisal")
        return HttpResponse("Message sent successfully")
    return render(request, 'send_message.html')
def see_history(request):
    return render(request, 'see_history.html')

def submit_contact(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('name')
        # Create a new Contact instance and save it to the database
        contact = Contact.objects.create(name=name, email=email)

        # Your logic to process the form data goes here

    return render(request, 'index.html')

# def send_email_to_client(request):
#     subject = "test"
#     message = "test"
#     from_email = settings.EMAIL_HOST_USER
#     recipient_list = ["redmindigo@gmail.com", "faisal.mr333@gmail.com", "faisal.muhammad7363@gmail.com"]
#     send_mail(subject, message, from_email, recipient_list, "Muhammad Faisal")
#     return HttpResponse("Message sent successfully")

