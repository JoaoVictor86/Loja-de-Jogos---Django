# Generated by Django 4.0.2 on 2022-03-07 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0007_rename_generos_genero_alter_genero_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jogo',
            name='genero',
            field=models.CharField(max_length=10),
        ),
        migrations.DeleteModel(
            name='Genero',
        ),
    ]
