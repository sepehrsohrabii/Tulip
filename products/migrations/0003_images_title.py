# Generated by Django 4.1.5 on 2023-02-22 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_subproduct_title_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='title',
            field=models.CharField(default='1', max_length=50),
            preserve_default=False,
        ),
    ]
