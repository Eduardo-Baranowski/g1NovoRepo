# Generated by Django 2.0.3 on 2018-04-02 23:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chamado', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='atendimento',
            old_name='funionariosAtendimento',
            new_name='funcionariosAtendimento',
        ),
    ]
