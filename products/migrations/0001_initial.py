# Generated by Django 4.1.5 on 2023-01-23 13:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('type', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dimensions', models.CharField(max_length=50)),
                ('brand', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=50)),
                ('material', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('image', models.CharField(max_length=300)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to=settings.AUTH_USER_MODEL)),
                ('type', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='type.type')),
            ],
        ),
    ]
