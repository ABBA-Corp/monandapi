# Generated by Django 4.1.7 on 2023-02-27 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0007_filial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="articul",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="product",
            name="information_en",
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name="product",
            name="information_ru",
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name="product",
            name="information_uz",
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name="product",
            name="minimum",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="product",
            name="size",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]