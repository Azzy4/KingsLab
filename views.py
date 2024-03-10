from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactForm
from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ContactInquiry
from .serializers import ContactInquirySerializer

index_view = never_cache(TemplateView.as_view(template_name='index.html'))

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message_content = form.cleaned_data['message']

            subject = 'New Message from Contact Form'
            full_message = f"Received message from {name}, Email: {email}\n\n{message_content}"

           
            return redirect('success_view')  
    else:
        form = ContactForm() 

    return render(request, 'contact.html', {'form': form})

def success_view(request):
   
    return render(request, 'success.html')  


@api_view(['GET', 'POST'])
def contact_inquiry_list_create(request):
    if request.method == 'GET':
        inquiries = ContactInquiry.objects.all()
        serializer = ContactInquirySerializer(inquiries, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ContactInquirySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
