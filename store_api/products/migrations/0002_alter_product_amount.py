# Generated by Django 5.0 on 2023-12-07 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='amount',
            field=models.DecimalField(decimal_places=4, max_digits=6),
        ),
    ]
