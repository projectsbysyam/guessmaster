# Generated by Django 4.2.5 on 2023-09-26 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0007_alter_agentpackage_box_dc_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agentpackage',
            name='box_dc',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='agentpackage',
            name='box_first_prize',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='agentpackage',
            name='box_first_prize_dc',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='agentpackage',
            name='box_rate',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='agentpackage',
            name='box_series_dc',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='agentpackage',
            name='box_series_prize',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='agentpackage',
            name='double2_dc',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='agentpackage',
            name='double2_prize',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='agentpackage',
            name='double_dc',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='agentpackage',
            name='double_rate',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='agentpackage',
            name='fifth_dc',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='agentpackage',
            name='fifth_prize',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='agentpackage',
            name='first_dc',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='agentpackage',
            name='first_prize',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='agentpackage',
            name='fourth_dc',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='agentpackage',
            name='fourth_prize',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='agentpackage',
            name='guarantee_dc',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='agentpackage',
            name='guarantee_prize',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='agentpackage',
            name='second_dc',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='agentpackage',
            name='second_prize',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='agentpackage',
            name='single1_dc',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='agentpackage',
            name='single1_prize',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='agentpackage',
            name='single_dc',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='agentpackage',
            name='single_rate',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='agentpackage',
            name='super_dc',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='agentpackage',
            name='super_rate',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='agentpackage',
            name='third_dc',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='agentpackage',
            name='third_prize',
            field=models.IntegerField(),
        ),
    ]
