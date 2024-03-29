# Generated by Django 3.2.7 on 2021-09-11 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_vehicletype_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reading',
            name='netWeight',
            field=models.DecimalField(decimal_places=3, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='reading',
            name='weight1',
            field=models.DecimalField(decimal_places=3, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='reading',
            name='weight2',
            field=models.DecimalField(decimal_places=3, max_digits=6, null=True),
        ),
    ]
