# Generated by Django 4.2.6 on 2023-10-07 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0011_chapatransaction_remove_orderitems_order_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chapatransaction',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='chapatransaction',
            name='email',
        ),
        migrations.RemoveField(
            model_name='chapatransaction',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='chapatransaction',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='chapatransaction',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='chapatransaction',
            name='response_dump',
        ),
        migrations.AlterField(
            model_name='chapatransaction',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
