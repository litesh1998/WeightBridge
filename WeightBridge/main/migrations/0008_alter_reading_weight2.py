# Generated by Django 3.2.7 on 2021-09-11 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_reading_netweight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reading',
            name='weight2',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True),
        ),
    ]
