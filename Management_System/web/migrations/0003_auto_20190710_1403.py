# Generated by Django 2.0.13 on 2019-07-10 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20190710_1353'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classes_name', models.CharField(max_length=20)),
                ('class_number', models.CharField(max_length=20)),
            ],
        ),
        migrations.RenameField(
            model_name='professional',
            old_name='Professional_name',
            new_name='professional_name',
        ),
        migrations.AddField(
            model_name='teacher',
            name='classes',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='c_teacher', to='web.Professional'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='professional',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='p_teacher', to='web.Professional'),
        ),
        migrations.AddField(
            model_name='classes',
            name='professional',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Professional'),
        ),
    ]
