# Generated by Django 4.1.7 on 2024-07-11 10:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0027_plotresale_amount_received_plotresale_remaining'),
    ]

    operations = [
        migrations.AddField(
            model_name='plotresale',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
