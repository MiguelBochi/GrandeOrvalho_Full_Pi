# Generated by Django 4.2.6 on 2023-10-14 22:58

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("GrandeOrvalho", "0008_remove_cliente_email_remove_cliente_senha_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="tipousuario",
            options={"verbose_name": "Tipo de usuário", "verbose_name_plural": "Tipos de usuários"},
        ),
    ]
