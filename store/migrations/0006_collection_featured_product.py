# Generated by Django 3.2.7 on 2021-09-09 21:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_custom_sql_migration_add_collection'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='featured_product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='store.product'),
        ),
    ]
