# Generated by Django 4.1.7 on 2024-05-27 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plots', '0004_plots_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlotsDocuments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='media/plot_files')),
                ('description', models.TextField()),
                ('type', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('plot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='plots.plots')),
            ],
        ),
    ]