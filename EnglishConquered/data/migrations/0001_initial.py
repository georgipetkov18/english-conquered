# Generated by Django 4.0.4 on 2022-05-03 12:08

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('deleted_on', models.DateTimeField(null=True)),
                ('unit', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Vocabulary',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('deleted_on', models.DateTimeField(null=True)),
                ('content', models.CharField(max_length=256)),
                ('description', models.CharField(max_length=1024)),
                ('type', models.CharField(choices=[('Word', 'Word'), ('Collocation', 'Collocation'), ('Phrasal verb', 'Phrasal Verb'), ('Idiom', 'Idiom')], default='Word', max_length=15)),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.module')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Grammar',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('deleted_on', models.DateTimeField(null=True)),
                ('subject', models.CharField(max_length=256)),
                ('content', models.CharField(max_length=1024)),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.module')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
