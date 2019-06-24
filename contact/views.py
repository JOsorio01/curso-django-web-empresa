from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm


def contact(request):
	contact_form = ContactForm()
	if request.method == "POST":
		contact_form = ContactForm(data=request.POST)
		if contact_form.is_valid:
			name = request.POST.get('name', '')
			email = request.POST.get('email', '')
			content = request.POST.get('content', '')
			# Envío de correo
			email = EmailMessage(
				"Nuevo mensaje de contacto",
				"De {} <{}>\n\n{}".format(name, email, content),
				"no-reply@inbox.mailtrap.io",
				["jose.osorio261194@gmail.com"],
				reply_to=[email],
			)
			try:
				email.send()
				return redirect(reverse('contact:contact')+"?ok")
			except:
				return redirect(reverse('contact:contact')+"?fail")

	return render(request, "contact/contact.html", {'form': contact_form})
