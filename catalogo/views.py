from django.shortcuts import render
from catalogo.models import Category, SubCategory, Service
from django.views import generic

def index(request):
    """View function for home page of site."""

    num_services = Service.objects.all().count()
    
    num_services_available = Service.objects.all()
    
    list_subcategory = SubCategory.objects.all()
    
    context = {
        'num_services': num_services,
        'num_services_available': num_services_available,
        'list_subcategory': list_subcategory,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
    

class ServiceListView(generic.ListView):
    model = Service

class ServiceDetailView(generic.DetailView):
    model = Service