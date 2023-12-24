from django.core.mail import send_mail, EmailMessage
from django.shortcuts import render
from django.conf import settings


def sendMail(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        message = request.POST.get('message')   
        from_email = request.POST.get('fromemail')
        recipient_list = [request.POST.get('toemail')]
        
        # Assuming you're using a file input field in your form with name 'attechfile'
        attached_file = request.FILES.get('attechfile')
        # Check the size of the attached file
        max_allowed_size = 25 * 1024 * 1024  # 5MB in bytes

        if attached_file:
            if attached_file.size <= max_allowed_size:
                msg = EmailMessage(subject, message, from_email, recipient_list)
                msg.attach(attached_file.name, attached_file.read(), attached_file.content_type)
                msg.send()

                context = {'em': 'Your Email Has Been Sent Successfully!'}
                return render(request, 'app/email.html', context)
            else:
                # Handle case where no file was uploaded
                context = {'error': f'your file size limit is {attached_file.size} bytes more than 25 mb.'}
                return render(request, 'app/email.html', context)

    else:
        return render (request,'app/emailForm.html')
