# Generated by Django 4.2.5 on 2023-09-27 19:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("GrandeOrvalho", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="consulta",
            name="animais",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="consultas",
                to="GrandeOrvalho.animais",
            ),
            preserve_default=False,
        ),
    ]
