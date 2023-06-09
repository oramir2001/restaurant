# Generated by Django 4.1.7 on 2023-04-19 16:09

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('food_ordering_guest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('image', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_delivered', models.BooleanField()),
                ('address', models.CharField(max_length=500)),
                ('comment', models.CharField(max_length=1000)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('order_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='food_ordering_guest.cart')),
            ],
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('price', models.IntegerField(validators=[django.core.validators.MaxValueValidator(999999999999999)])),
                ('description', models.CharField(max_length=500)),
                ('image', models.CharField(max_length=500)),
                ('is_gluten_free', models.BooleanField()),
                ('is_vageterian', models.BooleanField()),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_ordering_guest.category')),
            ],
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(validators=[django.core.validators.MaxValueValidator(999999999999999)])),
                ('cart_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_ordering_guest.cart')),
                ('dish_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_ordering_guest.dish')),
            ],
        ),
        migrations.DeleteModel(
            name='FoodOrderingGuest',
        ),
    ]
