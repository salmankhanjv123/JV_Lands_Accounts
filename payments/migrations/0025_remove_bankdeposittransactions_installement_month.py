# Generated by Django 4.1.7 on 2024-06-25 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0024_alter_bank_main_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bankdeposittransactions',
            name='installement_month',
        ),
    ]