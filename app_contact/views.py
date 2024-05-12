from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Inquiry
from .serializers import InquirySerializer
from django.core.mail import send_mail
from django.conf import settings

class InquiryViewSet(viewsets.ModelViewSet):
    queryset = Inquiry.objects.all()
    serializer_class = InquirySerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        inquiry = serializer.instance
        subject = 'Yangi Murojat!'
        message = f"Yangi murojat: {inquiry.fullname}\nEmail: {inquiry.email}\nTelefon: {inquiry.phone}\nRahbariyat: {inquiry.rahbariyat}\nMurojaat matni: {inquiry.message}"
        from_email = settings.DEFAULT_FROM_EMAIL
        to_email = [inquiry.email]
        send_mail(subject, message, from_email, to_email)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
