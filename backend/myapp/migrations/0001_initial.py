# Generated by Django 5.0.6 on 2024-07-08 13:26

from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='PatientImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_id', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='patient_images/')),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]