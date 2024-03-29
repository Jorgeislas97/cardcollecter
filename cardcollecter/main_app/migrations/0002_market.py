# Generated by Django 4.2.2 on 2023-06-15 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Market',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('price', models.CharField(choices=[('B', 'BGS'), ('P', 'PSA'), ('C', 'CGC')], default='B', max_length=1)),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.card')),
            ],
        ),
    ]
