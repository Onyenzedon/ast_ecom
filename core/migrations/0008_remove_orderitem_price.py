# Generated by Django 5.0.3 on 2024-04-08 20:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_orderitem_price_alter_orderitem_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='price',
        ),
    ]
