# Generated by Django 5.0.3 on 2024-04-08 20:40

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_remove_orderitem_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_id',
            field=models.UUIDField(default=uuid.UUID('4d9d9229-a9f7-43e3-99fe-a9cebb000932'), editable=False, null=True, unique=True),
        ),
    ]