# Generated by Django 4.0.1 on 2022-09-27 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_rename_id_cardobject_cardid'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardobject',
            name='id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
