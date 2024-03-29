# Generated by Django 2.0.13 on 2019-07-10 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_teacher_position'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parents_name', models.CharField(max_length=5)),
                ('user_name', models.CharField(max_length=12)),
                ('password', models.CharField(max_length=255)),
                ('id_card', models.CharField(max_length=18)),
            ],
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='classes',
        ),
        migrations.AddField(
            model_name='classes',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='t_classes', to='web.Teacher'),
        ),
        migrations.AlterField(
            model_name='classes',
            name='professional',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='p_classes', to='web.Professional'),
        ),
    ]
