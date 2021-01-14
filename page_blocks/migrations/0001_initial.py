# Generated by Django 3.1.5 on 2021-01-14 15:10

import django.contrib.auth.models
import django.contrib.auth.validators
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlockWithFourTexts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('top_left_text', models.CharField(blank=True, max_length=255, null=True)),
                ('top_right_text', models.CharField(blank=True, max_length=255, null=True)),
                ('bottom_left_text', models.CharField(blank=True, max_length=255, null=True)),
                ('bottom_right_text', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'block_four_text',
            },
        ),
        migrations.CreateModel(
            name='BlockWithImageAndList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(blank=True, null=True, upload_to='images')),
                ('list_items', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), blank=True, null=True, size=5)),
            ],
            options={
                'db_table': 'block_image_and_list',
            },
        ),
        migrations.CreateModel(
            name='BlockWithTitleTextAndButton',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('text', models.TextField(blank=True, null=True)),
                ('button_text', models.CharField(blank=True, max_length=30, null=True)),
                ('button_action', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'block_title_text_and_button',
            },
        ),
        migrations.CreateModel(
            name='BlockWithTitleTextImageAndButtons',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(blank=True, null=True, upload_to='images')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('text', models.TextField(blank=True, null=True)),
                ('first_button_text', models.CharField(blank=True, max_length=30, null=True)),
                ('first_button_action', models.CharField(blank=True, max_length=30, null=True)),
                ('second_button_text', models.CharField(blank=True, max_length=30, null=True)),
                ('second_button_action', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'block_title_text_image_and_buttons',
            },
        ),
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.SlugField()),
                ('sorting', models.PositiveSmallIntegerField(default=0, help_text='Sequence of block pins on a page')),
                ('is_active', models.BooleanField(default=True)),
                ('object_id', models.PositiveIntegerField(blank=True, editable=False, null=True)),
                ('content_type', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='content_type_block', to='contenttypes.contenttype')),
            ],
            options={
                'ordering': ['is_active', 'sorting'],
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user_group', models.CharField(choices=[('client', 'Client'), ('admin', 'Admin')], default='Client', help_text='Select user group', max_length=10)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]