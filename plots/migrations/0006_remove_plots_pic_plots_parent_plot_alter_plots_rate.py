# Generated by Django 4.1.7 on 2024-07-09 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plots', '0005_plotsdocuments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plots',
            name='pic',
        ),
        migrations.AddField(
            model_name='plots',
            name='parent_plot',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_plots', to='plots.plots'),
        ),
        migrations.AlterField(
            model_name='plots',
            name='rate',
            field=models.FloatField(default=0),
        ),
    ]