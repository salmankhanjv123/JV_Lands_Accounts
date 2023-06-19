# Generated by Django 4.1.7 on 2023-06-19 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0003_alter_paymentreminder_table_expenseperson'),
    ]

    operations = [
        migrations.AddField(
            model_name='outgoingfund',
            name='person',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='payments.expenseperson'),
            preserve_default=False,
        ),
    ]
