from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns

# Create your models here.
class Category(models.Model):
    """Model representing a service category."""
    name = models.CharField(max_length=200, help_text='Ingrese la categoría del servicio (ejm. Enseñanza, Servicios del hogar, Servicios de cuidado)', verbose_name='nombre')

    class Meta:
        verbose_name = 'categoría'
        ordering = ['name']        
        
    def __str__(self):
        """String for representing the Model object."""
        return self.name
        
class SubCategory(models.Model):
    """Model representing a service subcategory."""
    name = models.CharField(max_length=200, help_text='Ingrese una subcatecoría del servicio (ejm. idiomas, limpieza de hogar)', verbose_name='nombre')
    
    category = models.ForeignKey('Category',on_delete=models.SET_NULL, null=True, verbose_name='categoría')

    class Meta:
        verbose_name = 'subcategoría'
        ordering = ['category']
        
    def __str__(self):
        """String for representing the Model object."""
        return self.name
        
from django.contrib.auth.models import User
from datetime import date
from djmoney.models.fields import MoneyField

class Service(models.Model):
    """Model representing a specific service."""
    title = models.CharField(max_length=200, verbose_name='título')
    description = models.TextField(max_length=5000, help_text='Ingrese la descripción del servicio', verbose_name='descripción')
    #image = models.Imagefield........
    #slug = models.Slugfield...........
    SERVICE_TYPE = (
        ('o', 'Ofrezco un servicio'),
        ('r', 'Requiero un servicio'),
    )
        
    service_type = models.CharField(
        max_length=1,
        choices=SERVICE_TYPE,
        default='o',
        help_text='Ofrezco/Requiero',
        verbose_name='tipo de servicio'
    )    
    
    subcategory = models.ForeignKey('SubCategory',on_delete=models.SET_NULL, null=True, verbose_name='categoría')
    
    price = MoneyField(max_digits=8, decimal_places=0, default=None, null=True, blank=True, default_currency='PEN', verbose_name='precio')
    
    PRICE_TYPE = (
        ('c', 'A convenir'),
        ('f', 'Gratis'),
        ('n', 'Negociable'),
        ('x', 'Precio fijo'),
    )    
    
    price_type = models.CharField(
        max_length=1,
        choices=PRICE_TYPE,
        default='c',
        help_text='Type of price',
        verbose_name='acuerdo'
    )        
    SERVICE_STATUS = (
        ('a', 'Disponible'),
        ('e', 'Expirado'),
        ('c', 'Cancelado'),
    )
    
    status = models.CharField(
        max_length=1,
        choices=SERVICE_STATUS,
        blank=True,
        default='a',
        help_text='Estado del anuncio',
        verbose_name='estado'
    )

    due_date = models.DateField(null=True, blank=True, verbose_name='anuncio expira')
    
    applicant = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='usuario')
    #created = models.DateTimeField.....
    #updated = models.DateTimeField.....
    
    @property
    def is_overdue(self):
        if self.due_date and date.today() > self.due_date:
            return True
        return False
    
    class Meta:
        ordering = ['-due_date']
        verbose_name = 'servicio'
        #permissions = (("can_mark_returned", "Set book as returned"),) 

    def get_absolute_url(self):
        """Returns the url to access a particular service instance."""
        return reverse('service-detail', args=[str(self.id)])
        
    def __str__(self):
        """String for representing the Model object."""
        return f'({self.id} {self.title})'    