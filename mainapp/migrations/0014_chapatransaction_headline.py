# Generated by Django 4.2.6 on 2023-10-07 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0013_remove_chapatransaction_checkout_url_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapatransaction',
            name='Headline',
            field=models.CharField(default='KK', max_length=1000),
            preserve_default=False,
        ),
    ]