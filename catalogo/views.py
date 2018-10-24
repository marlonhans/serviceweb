from django.shortcuts import render
from catalogo.models import Category, SubCategory, Service
from django.views import generic

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_services = Service.objects.all().count()
    
    # Available services (status = 'a')
    num_services_available = Service.objects.filter(status__exact='a').count()
    
    # The 'all()' is implied by default.    
    num_subcategory = SubCategory.objects.count()
    
    context = {
        'num_services': num_services,
        'num_services_available': num_services_available,
        'num_subcategory': num_subcategory,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
    

class ServiceListView(generic.ListView):
    model = Service

class ServiceDetailView(generic.DetailView):
    model = Service