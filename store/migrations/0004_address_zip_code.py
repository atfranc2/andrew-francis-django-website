# Generated by Django 3.2.7 on 2021-09-09 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_add_slug_to_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='zip_code',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
