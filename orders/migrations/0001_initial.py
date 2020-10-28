# Generated by Django 3.1.2 on 2020-10-28 21:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flavor', models.CharField(choices=[('MARGARITA', 'Margarita'), ('TEXAS', 'Texas'), ('MARINARA', 'Marinara'), ('SALAMI', 'Salami'), ('PAPPERONI', 'Papperoni')], max_length=255)),
                ('size', models.CharField(choices=[('SMALL', 'Small'), ('MEDIUM', 'Medium'), ('LARGE', 'Large')], max_length=255)),
                ('quantity', models.PositiveIntegerField(default=1)),
            ],
            options={
                'verbose_name': 'Pizza',
                'verbose_name_plural': 'Pizzas',
                'db_table': 'pizza',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_address', models.TextField()),
                ('status', models.CharField(choices=[('ORDER_PLACED', 'Order placed'), ('PREPARE', 'Prepare'), ('BAKE', 'Bake'), ('BOX', 'Box'), ('Delivery', 'Delivery')], default='ORDER_PLACED', max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer', to=settings.AUTH_USER_MODEL)),
                ('pizza', models.ManyToManyField(related_name='pizza', to='orders.Pizza')),
            ],
            options={
                'verbose_name': 'order',
                'verbose_name_plural': 'Orders',
                'db_table': 'order',
                'ordering': ('-id',),
            },
        ),
    ]
