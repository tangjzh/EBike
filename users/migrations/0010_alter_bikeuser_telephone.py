# Generated by Django 4.2 on 2024-05-02 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0009_bikeuser_telephone_alter_bikeuser_email"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bikeuser",
            name="telephone",
            field=models.CharField(
                blank=True, max_length=11, null=True, verbose_name="电话号码"
            ),
        ),
    ]
