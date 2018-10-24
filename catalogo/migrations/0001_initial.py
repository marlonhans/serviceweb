# Generated by Django 2.1.2 on 2018-10-23 22:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import djmoney.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Ingrese la categoría del servicio (ejm. Enseñanza, Servicios del hogar, Servicios de cuidado)', max_length=200, verbose_name='nombre')),
            ],
            options={
                'verbose_name': 'categoría',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='título')),
                ('description', models.TextField(help_text='Ingrese la descripción del servicio', max_length=5000, verbose_name='descripción')),
                ('service_type', models.CharField(choices=[('o', 'Ofrezco un servicio'), ('r', 'Requiero un servicio')], default='o', help_text='Ofrezco/Requiero', max_length=1, verbose_name='tipo de servicio')),
                ('price_currency', djmoney.models.fields.CurrencyField(choices=[('PEN', 'Nuevo Sol'), ('USD', 'US Dollar')], default='PEN', editable=False, max_length=3)),
                ('price', djmoney.models.fields.MoneyField(blank=True, decimal_places=0, default=None, default_currency='PEN', max_digits=8, null=True, verbose_name='precio')),
                ('price_type', models.CharField(choices=[('c', 'A convenir'), ('f', 'Gratis'), ('n', 'Negociable'), ('x', 'Precio fijo')], default='c', help_text='Type of price', max_length=1, verbose_name='acuerdo')),
                ('status', models.CharField(blank=True, choices=[('a', 'Disponible'), ('e', 'Expirado'), ('c', 'Cancelado')], default='a', help_text='Estado del anuncio', max_length=1, verbose_name='estado')),
                ('due_date', models.DateField(blank=True, null=True, verbose_name='anuncio expira')),
                ('applicant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='usuario')),
            ],
            options={
                'verbose_name': 'servicio',
                'ordering': ['-due_date'],
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Ingrese una subcatecoría del servicio (ejm. idiomas, limpieza de hogar)', max_length=200, verbose_name='nombre')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalogo.Category', verbose_name='categoría')),
            ],
            options={
                'verbose_name': 'subcategoría',
                'ordering': ['category'],
            },
        ),
        migrations.AddField(
            model_name='service',
            name='subcategory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalogo.SubCategory', verbose_name='categoría'),
        ),
    ]
