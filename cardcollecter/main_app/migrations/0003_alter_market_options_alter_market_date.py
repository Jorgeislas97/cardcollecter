# Generated by Django 4.2.2 on 2023-06-16 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_market'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='market',
            options={'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='market',
            name='date',
            field=models.DateField(verbose_name='submission date'),
        ),
    ]
