# Generated by Django 3.0.5 on 2021-06-28 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0005_auto_20210626_1748'),
    ]

    operations = [
        migrations.CreateModel(
            name='HorarioMarcado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeCliente', models.TextField(blank=True, null=True)),
                ('data', models.DateTimeField(blank=True, null=True)),
                ('id_imovel', models.IntegerField(blank=True, null=True)),
                ('tipo_imovel', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
