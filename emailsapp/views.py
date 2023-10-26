from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
import csv
from django.views import View
from django.http import HttpResponseRedirect
from .forms import CSVUploadForm
from .models import EmailList
from django.contrib import messages

def index(request):
    # Your view logic here
    return render(request,"emailsapp/home.html")

class AboutView(TemplateView):
    template_name = "emailsapp/about.html"

class ServicesView(TemplateView):
    template_name = "emailsapp/services.html"

class ContactView(TemplateView):
    template_name = "emailsapp/contact.html"

class CSVUploadView(View):
    template_name = 'emailsapp/upload.html'  # The template to render the form

    def get(self, request):
        form = CSVUploadForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = CSVUploadForm(request.POST, request.FILES)
        success_count = 0  # Initialize success_count
        if form.is_valid():
            csv_file = form.cleaned_data['csv_file']
            # Process the CSV file
            decoded_file = csv_file.read().decode('utf-8')
            csv_data = csv.reader(decoded_file.splitlines(), delimiter=',')
            for row in csv_data:
                email = row[0].strip()
                if email:
                    EmailList.objects.get_or_create(email=email)
                    success_count += 1
            if success_count > 0:
                # import pdb
                # pdb.set_trace();
                messages.success(request, f'Successfully uploaded {success_count} email(s).')
            return render(request, self.template_name, {'message': messages.success(request, f'Successfully uploaded {success_count} email(s).')})
        else:
            messages.error(request, 'Failed to upload the CSV file.')
        return render(request, self.template_name, {'form': form})