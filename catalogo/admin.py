from django.contrib import admin
from catalogo.models import Category, SubCategory, Service

class SubCategoryInline(admin.TabularInline):
    model = SubCategory
    extra = 0
    can_delete = False

class ServiceInline(admin.TabularInline):
    model = Service
    extra = 0
    can_delete = False
    fields = ('title', 'subcategory', 'service_type', 'price','price_type','status', 'due_date','applicant')
    readonly_fields = fields

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [SubCategoryInline]

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category',)
    inlines = [ServiceInline]

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'subcategory', 'service_type', 'price','price_type','status', 'due_date','applicant')
    list_filter = ('status', 'due_date', 'service_type')
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'service_type','subcategory',('price','price_type'),)
        }),
        ('Estado', {
            'fields': (('status', 'due_date','applicant'))
        }),
    )    