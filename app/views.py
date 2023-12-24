from django.core.mail import send_mail, EmailMessage
from django.shortcuts import render
from django.conf import settings


def sendMail(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        message = request.POST.get('message')   
        from_email = request.POST.get('fromemail')
        recipient_list = request.POST.get('toemail')
        recipient_list.split(",")
        recipient_list = list(recipient_list)
        # Assuming you're using a file input field in your form with name 'attechfile'
        attached_file = request.FILES.get('attechfile')
        
        if attached_file:
            msg = EmailMessage(subject, message, from_email, recipient_list)
            msg.attach(attached_file.name, attached_file.read(), attached_file.content_type)
            msg.send()

            context = {'em': 'Your Email Has Been Sent Successfully!'}
            return render(request, 'app/email.html', context)
        else:
            # Handle case where no file was uploaded
            context = {'error': 'No file uploaded.'}
            return render(request, 'app/email.html', context)

    else:
        return render (request,'app/emailForm.html')
