# Generated by Django 4.1.7 on 2023-03-02 19:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_remove_product_category_product_categories'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='categories',
            new_name='category',
        ),
    ]
