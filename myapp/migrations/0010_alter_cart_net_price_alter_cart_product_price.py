# Generated by Django 4.1.7 on 2023-05-21 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0009_cart_razorpay_order_id_cart_razorpay_payment_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cart",
            name="net_price",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="cart",
            name="product_price",
            field=models.IntegerField(),
        ),
    ]
