# Generated by Django 4.0.4 on 2022-06-11 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0008_remove_usuarios_contato_fk_contatos'),
        ('endereco', '0002_alter_contatos_contato'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contatos',
        ),
    ]
