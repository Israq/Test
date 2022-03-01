from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
	return render(request,'home.html',{})
def about(request):
    return render(request, 'about.html')
def blog(request):
    return render(request, 'blog.html')
def blog_details(request):
    return render(request, 'blog_details.html')

def service(request):
    return render(request, 'service.html')
def implant(request):
    return render(request, 'implant.html')
def g_dentistry(request):
    return render(request, 'g_dentistry.html')


def contact(request):
	if request.method == "POST":
		message_name 	= request.POST['message-name']
		message_email 	= request.POST['message-email']
		message 	 	= request.POST['message']

		#send an email
		send_mail(
			message_name,
			message,
			message_email,
			['ragib.israq@northsouth.edu'],
			)
		return render(request,'contact.html',{'message_name': message_name,})
	else:
		return render(request,'contact.html',{})

def appointment(request):
    if request.method == "POST":
        your_name = request.POST['your-name']
        your_phone = request.POST['your-phone']
        your_email = request.POST['your-email']
        your_address = request.POST['your-address']
        your_schedule = request.POST['your-schedule']
        your_date = request.POST.get('your-date')
        your_message = request.POST['your-message']

        ### Send an Email Start ###
        appointment = "Name: " + your_name + " Phone: " + your_phone + " Email: " + your_email + " Address: " + your_address + " Schedule: " + your_schedule + " Message: " + your_message

        send_mail(
            'Appointment Request', # subject
            appointment, # message
            your_email, # from email
            ['ragib.israq@northsouth.edu'],
			)
        ### Send an Email End ###

        return render(request, 'appointment.html', {
            'your_name':your_name,
            'your_phone':your_phone,
            'your_email':your_email,
            'your_address':your_address,
            'your_schedule':your_schedule,
            'your_date':your_date,
            'your_message': your_message
        })

    else:
        return render(request, 'home.html', {})


