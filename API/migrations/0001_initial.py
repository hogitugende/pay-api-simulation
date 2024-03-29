# Generated by Django 2.2.3 on 2019-09-05 15:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InfoTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('prenom', models.CharField(max_length=30)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('source', models.CharField(max_length=30)),
                ('destination', models.CharField(max_length=30)),
                ('montant', models.CharField(max_length=30)),
                ('objet', models.CharField(max_length=30)),
                ('serie', models.CharField(max_length=30)),
            ],
        ),
    ]
