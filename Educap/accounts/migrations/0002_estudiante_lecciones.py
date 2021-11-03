# Generated by Django 3.2.8 on 2021-11-02 00:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('LearningCatalog', '0002_alter_categoria_descripcion'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiante_Lecciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.estudiante')),
                ('leccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LearningCatalog.leccion')),
            ],
        ),
    ]