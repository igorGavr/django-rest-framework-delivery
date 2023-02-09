# Generated by Django 4.1.6 on 2023-02-09 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0004_store_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='market.product'),
        ),
        migrations.AlterField(
            model_name='store',
            name='provider',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='market.provider'),
        ),
    ]
