# Generated by Django 4.2.5 on 2023-10-02 16:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("uploader", "0001_initial"),
        ("GrandeOrvalho", "0002_consulta_animais"),
    ]

    operations = [
        migrations.AddField(
            model_name="animais",
            name="capa",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="uploader.image",
            ),
        ),
    ]
