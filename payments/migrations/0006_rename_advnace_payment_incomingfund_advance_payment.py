# Generated by Django 4.1.7 on 2024-03-01 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0005_incomingfund_advnace_payment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='incomingfund',
            old_name='advnace_payment',
            new_name='advance_payment',
        ),
    ]