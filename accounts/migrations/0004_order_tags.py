# Generated by Django 4.1.7 on 2023-02-28 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_tag'),
        ('accounts', '0003_order_customer_order_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='tags',
            field=models.ManyToManyField(to='products.tag'),
        ),
    ]