# Generated by Django 4.2.6 on 2023-10-08 18:16

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0017_chapatransaction_amount_chapatransaction_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='order_items',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='orderuniqueId',
        ),
        migrations.AddField(
            model_name='orders',
            name='amount',
            field=models.FloatField(default=848848483),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orders',
            name='checkout_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='orders',
            name='currency',
            field=models.CharField(default='ETB', max_length=25),
        ),
        migrations.AddField(
            model_name='orders',
            name='description',
            field=models.TextField(default='andi.fab@gmsm.Com'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orders',
            name='email',
            field=models.EmailField(default='andi.fab@gmsm.Com', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orders',
            name='first_name',
            field=models.CharField(default='andi.fab@gmsm.Com', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orders',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='orders',
            name='last_name',
            field=models.CharField(default='andi.fab@gmsm.Com', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orders',
            name='payment_title',
            field=models.CharField(default='Payment', max_length=255),
        ),
        migrations.AddField(
            model_name='orders',
            name='phone_number',
            field=models.CharField(default='andi.fab@gmsm.Com', max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orders',
            name='response_dump',
            field=models.JSONField(blank=True, default=dict),
        ),
    ]