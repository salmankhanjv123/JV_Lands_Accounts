# Generated by Django 4.1.7 on 2023-11-20 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0008_remove_plotresale_current_project_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='plotresale',
            name='remarks',
            field=models.TextField(blank=True, null=True),
        ),
    ]
