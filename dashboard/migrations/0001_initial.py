# Generated by Django 3.2 on 2023-05-25 19:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('apellido', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('celular', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Ciclo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('carrera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.carrera')),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('apellido', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('celular', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(choices=[('admin', 'Admin'), ('alumno', 'Alumno')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('alumnos', models.ManyToManyField(to='dashboard.Alumno')),
                ('ciclo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.ciclo')),
                ('profesor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.profesor')),
            ],
        ),
        migrations.CreateModel(
            name='Cuenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('rol', models.CharField(max_length=100)),
                ('alumno', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='dashboard.alumno')),
                ('profesor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='dashboard.profesor')),
            ],
        ),
        migrations.AddField(
            model_name='carrera',
            name='ciclos',
            field=models.ManyToManyField(related_name='carreras', to='dashboard.Ciclo'),
        ),
        migrations.AddField(
            model_name='alumno',
            name='carrera',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.carrera'),
        ),
        migrations.AddField(
            model_name='alumno',
            name='cursos',
            field=models.ManyToManyField(to='dashboard.Curso'),
        ),
    ]