# Generated by Django 5.1.1 on 2024-09-18 07:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_customuser_password_alter_customuser_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='DatEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('survey_name', models.CharField(max_length=255)),
                ('date_start', models.DateField()),
                ('date_close', models.DateField()),
                ('crs_name', models.CharField(max_length=255)),
                ('crs_year', models.IntegerField()),
                ('dept_name', models.CharField(max_length=255)),
                ('crs_dir', models.CharField(max_length=255)),
                ('resp_fac', models.CharField(max_length=255)),
                ('eval_id', models.IntegerField()),
                ('eval_uname', models.CharField(max_length=255)),
                ('eval_email', models.CharField(max_length=255)),
                ('t_submit', models.DateTimeField()),
                ('mobile', models.BooleanField(default=False)),
                ('grad_year', models.DateField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('N', 'Not specified')], default='Not specified', max_length=1)),
                ('program', models.CharField(max_length=255)),
                ('research_1', models.CharField(max_length=255)),
                ('research_2', models.CharField(max_length=255)),
                ('research_3', models.CharField(max_length=255)),
                ('question_1', models.IntegerField(default=0, help_text='Rate from -1 to 5', validators=[django.core.validators.MinValueValidator(-1), django.core.validators.MaxValueValidator(5)])),
                ('question_2', models.IntegerField(default=0, help_text='Rate from -1 to 5', validators=[django.core.validators.MinValueValidator(-1), django.core.validators.MaxValueValidator(5)])),
                ('question_3', models.IntegerField(default=0, help_text='Rate from -1 to 5', validators=[django.core.validators.MinValueValidator(-1), django.core.validators.MaxValueValidator(5)])),
                ('question_4', models.IntegerField(default=0, help_text='Rate from -1 to 5', validators=[django.core.validators.MinValueValidator(-1), django.core.validators.MaxValueValidator(5)])),
                ('question_5', models.IntegerField(default=0, help_text='Rate from -1 to 5', validators=[django.core.validators.MinValueValidator(-1), django.core.validators.MaxValueValidator(5)])),
                ('question_6', models.IntegerField(default=0, help_text='Rate from -1 to 5', validators=[django.core.validators.MinValueValidator(-1), django.core.validators.MaxValueValidator(5)])),
                ('question_7', models.IntegerField(default=0, help_text='Rate from -1 to 5', validators=[django.core.validators.MinValueValidator(-1), django.core.validators.MaxValueValidator(5)])),
                ('question_8', models.IntegerField(default=0, help_text='Rate from -1 to 5', validators=[django.core.validators.MinValueValidator(-1), django.core.validators.MaxValueValidator(5)])),
                ('question_9', models.IntegerField(default=0, help_text='Rate from -1 to 5', validators=[django.core.validators.MinValueValidator(-1), django.core.validators.MaxValueValidator(5)])),
                ('question_10', models.IntegerField(default=0, help_text='Rate from -1 to 5', validators=[django.core.validators.MinValueValidator(-1), django.core.validators.MaxValueValidator(5)])),
                ('question_11', models.IntegerField(default=0, help_text='Rate from -1 to 5', validators=[django.core.validators.MinValueValidator(-1), django.core.validators.MaxValueValidator(5)])),
                ('question_12', models.IntegerField(default=0, help_text='Rate from -1 to 5', validators=[django.core.validators.MinValueValidator(-1), django.core.validators.MaxValueValidator(5)])),
                ('question_13', models.IntegerField(default=0, help_text='Rate from -1 to 5', validators=[django.core.validators.MinValueValidator(-1), django.core.validators.MaxValueValidator(5)])),
                ('question_14', models.IntegerField(default=0, help_text='Rate from -1 to 5', validators=[django.core.validators.MinValueValidator(-1), django.core.validators.MaxValueValidator(5)])),
                ('question_15', models.IntegerField(default=0, help_text='Rate from -1 to 5', validators=[django.core.validators.MinValueValidator(-1), django.core.validators.MaxValueValidator(5)])),
                ('question_16', models.IntegerField(default=0, help_text='Rate from -1 to 5', validators=[django.core.validators.MinValueValidator(-1), django.core.validators.MaxValueValidator(5)])),
                ('question_17', models.IntegerField(default=0, help_text='Rate from -1 to 5', validators=[django.core.validators.MinValueValidator(-1), django.core.validators.MaxValueValidator(5)])),
                ('question_18', models.IntegerField(default=0, help_text='Rate from -1 to 5', validators=[django.core.validators.MinValueValidator(-1), django.core.validators.MaxValueValidator(5)])),
                ('question_19', models.IntegerField(default=0, help_text='Rate from -1 to 5', validators=[django.core.validators.MinValueValidator(-1), django.core.validators.MaxValueValidator(5)])),
                ('question_20', models.IntegerField(default=0, help_text='Rate from -1 to 5', validators=[django.core.validators.MinValueValidator(-1), django.core.validators.MaxValueValidator(5)])),
                ('question_21', models.IntegerField(default=0, help_text='Rate from -1 to 5', validators=[django.core.validators.MinValueValidator(-1), django.core.validators.MaxValueValidator(5)])),
                ('question_22', models.IntegerField(default=0, help_text='Rate from -1 to 5', validators=[django.core.validators.MinValueValidator(-1), django.core.validators.MaxValueValidator(5)])),
                ('question_23', models.IntegerField(default=0, help_text='Rate from -1 to 5', validators=[django.core.validators.MinValueValidator(-1), django.core.validators.MaxValueValidator(5)])),
                ('question_24', models.IntegerField(default=0, help_text='Rate from -1 to 5', validators=[django.core.validators.MinValueValidator(-1), django.core.validators.MaxValueValidator(5)])),
                ('question_25', models.IntegerField(default=0, help_text='Rate from -1 to 5', validators=[django.core.validators.MinValueValidator(-1), django.core.validators.MaxValueValidator(5)])),
                ('question_26', models.IntegerField(default=0, help_text='Rate from -1 to 5', validators=[django.core.validators.MinValueValidator(-1), django.core.validators.MaxValueValidator(5)])),
                ('question_27', models.IntegerField(default=0, help_text='Rate from -1 to 5', validators=[django.core.validators.MinValueValidator(-1), django.core.validators.MaxValueValidator(5)])),
                ('question_28', models.IntegerField(default=0, help_text='Rate from -1 to 5', validators=[django.core.validators.MinValueValidator(-1), django.core.validators.MaxValueValidator(5)])),
                ('question_29', models.IntegerField(default=0, help_text='Rate from -1 to 5', validators=[django.core.validators.MinValueValidator(-1), django.core.validators.MaxValueValidator(5)])),
                ('question_30', models.IntegerField(default=0, help_text='Rate from -1 to 5', validators=[django.core.validators.MinValueValidator(-1), django.core.validators.MaxValueValidator(5)])),
                ('question_31', models.IntegerField(default=0, help_text='Rate from -1 to 5', validators=[django.core.validators.MinValueValidator(-1), django.core.validators.MaxValueValidator(5)])),
                ('question_32', models.IntegerField(default=0, help_text='Rate from -1 to 5', validators=[django.core.validators.MinValueValidator(-1), django.core.validators.MaxValueValidator(5)])),
            ],
        ),
    ]
