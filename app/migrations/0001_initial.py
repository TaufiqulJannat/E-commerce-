# Generated by Django 3.2.1 on 2021-05-08 09:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('locality', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('zipcode', models.IntegerField()),
                ('state', models.CharField(choices=[('Dhaka', 'Dhaka'), ('Chottogram', 'Chottogram'), ('Barisal', 'Barisal'), ('Maymanshing', 'Maymanshing'), ('Rajshahi', 'Rajshahi'), ('Khulna', 'Khulna'), ('Rangpur', 'Rangpur'), ('Chylet', 'chylet')], max_length=500)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
