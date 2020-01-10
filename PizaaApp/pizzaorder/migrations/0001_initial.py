# Generated by Django 3.0.2 on 2020-01-10 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=256)),
                ('customer_addres', models.CharField(max_length=256)),
                ('customer_phone', models.CharField(max_length=256)),
                ('pizza_type', models.CharField(choices=[('sicilian', 'Sicilian'), ('margherita', 'Margherita'), ('greek', 'Greek'), ('checken', 'Checken'), ('chesse', 'Chesse')], max_length=256)),
                ('pizza_size', models.CharField(choices=[('l', 'Large'), ('m', 'Medium'), ('s', 'Small')], max_length=256)),
                ('pizza_number', models.IntegerField()),
                ('status', models.CharField(choices=[('shipped', 'Shipped Number'), ('in_progress', 'In Prigress'), ('canceled', 'Canceled'), ('Delivered', 'delivered')], max_length=256)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]