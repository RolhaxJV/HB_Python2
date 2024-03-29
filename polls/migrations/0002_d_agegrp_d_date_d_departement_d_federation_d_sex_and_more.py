# Generated by Django 5.0.2 on 2024-02-16 14:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='D_AgeGRP',
            fields=[
                ('label', models.CharField(default=None, max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='D_Date',
            fields=[
                ('date', models.DateField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='D_Departement',
            fields=[
                ('code_Commune', models.CharField(default='0', max_length=5)),
                ('code_QPV', models.CharField(default='0', max_length=5)),
                ('code_Departement', models.CharField(default=0, max_length=5)),
                ('pk_depart', models.CharField(default=None, max_length=100, primary_key=True, serialize=False)),
                ('label_Commune', models.CharField(default='0', max_length=100)),
                ('label_QPV', models.CharField(default='0', max_length=100)),
                ('label_Departement', models.CharField(default='0', max_length=100)),
                ('label_Region', models.CharField(default='0', max_length=100)),
                ('statut', models.CharField(default='0', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='D_Federation',
            fields=[
                ('code', models.IntegerField(primary_key=True, serialize=False)),
                ('label', models.CharField(default=None, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='D_Sex',
            fields=[
                ('code', models.CharField(default=None, max_length=1, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='D_Type',
            fields=[
                ('label', models.CharField(default=None, max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='F_Club',
            fields=[
                ('nomber', models.IntegerField(default=None)),
                ('pk_F', models.CharField(default=None, max_length=100, primary_key=True, serialize=False)),
                ('Date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.d_date')),
                ('Federation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.d_federation')),
                ('Geo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.d_departement')),
                ('Type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.d_type')),
            ],
        ),
        migrations.CreateModel(
            name='F_Licence',
            fields=[
                ('nomber', models.IntegerField(default=0)),
                ('pk_L', models.CharField(default=None, max_length=100, primary_key=True, serialize=False)),
                ('Age_grp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.d_agegrp')),
                ('Date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.d_date')),
                ('Federation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.d_federation')),
                ('Geo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.d_departement')),
                ('Sex', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.d_sex')),
            ],
        ),
        migrations.CreateModel(
            name='ODS_CLUBS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_commune', models.CharField(default='0', max_length=100)),
                ('commune', models.CharField(default='0', max_length=100)),
                ('code_QPV', models.CharField(default='0', max_length=100)),
                ('nom_QPV', models.CharField(default='0', max_length=100)),
                ('departement', models.CharField(default='0', max_length=100)),
                ('region', models.CharField(default='0', max_length=100)),
                ('statut_geo', models.CharField(default='0', max_length=100)),
                ('code', models.CharField(default='0', max_length=100)),
                ('federation', models.CharField(default='0', max_length=100)),
                ('clubs', models.CharField(default='0', max_length=100)),
                ('EPA', models.CharField(default='0', max_length=100)),
                ('Total', models.CharField(default='0', max_length=100)),
                ('Date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ODS_Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_commune', models.CharField(default='0', max_length=100)),
                ('commune', models.CharField(default='0', max_length=100)),
                ('code_QPV', models.CharField(default='0', max_length=100)),
                ('nom_QPV', models.CharField(default='0', max_length=100)),
                ('departement', models.CharField(default='0', max_length=100)),
                ('region', models.CharField(default='0', max_length=100)),
                ('statut_geo', models.CharField(default='0', max_length=100)),
                ('code', models.CharField(default='0', max_length=100)),
                ('federation', models.CharField(default='0', max_length=100)),
                ('F_1_4_ans', models.CharField(default='0', max_length=100)),
                ('F_5_9_ans', models.CharField(default='0', max_length=100)),
                ('F_10_14_ans', models.CharField(default='0', max_length=100)),
                ('F_15_19_ans', models.CharField(default='0', max_length=100)),
                ('F_20_24_ans', models.CharField(default='0', max_length=100)),
                ('F_25_29_ans', models.CharField(default='0', max_length=100)),
                ('F_30_34_ans', models.CharField(default='0', max_length=100)),
                ('F_35_39_ans', models.CharField(default='0', max_length=100)),
                ('F_40_44_ans', models.CharField(default='0', max_length=100)),
                ('F_45_49_ans', models.CharField(default='0', max_length=100)),
                ('F_50_54_ans', models.CharField(default='0', max_length=100)),
                ('F_55_59_ans', models.CharField(default='0', max_length=100)),
                ('F_60_64_ans', models.CharField(default='0', max_length=100)),
                ('F_65_69_ans', models.CharField(default='0', max_length=100)),
                ('F_70_74_ans', models.CharField(default='0', max_length=100)),
                ('F_75_79_ans', models.CharField(default='0', max_length=100)),
                ('F_80_99_ans', models.CharField(default='0', max_length=100)),
                ('F_NR', models.CharField(default='0', max_length=100)),
                ('H_1_4_ans', models.CharField(default='0', max_length=100)),
                ('H_5_9_ans', models.CharField(default='0', max_length=100)),
                ('H_10_14_ans', models.CharField(default='0', max_length=100)),
                ('H_15_19_ans', models.CharField(default='0', max_length=100)),
                ('H_20_24_ans', models.CharField(default='0', max_length=100)),
                ('H_25_29_ans', models.CharField(default='0', max_length=100)),
                ('H_30_34_ans', models.CharField(default='0', max_length=100)),
                ('H_35_39_ans', models.CharField(default='0', max_length=100)),
                ('H_40_44_ans', models.CharField(default='0', max_length=100)),
                ('H_45_49_ans', models.CharField(default='0', max_length=100)),
                ('H_50_54_ans', models.CharField(default='0', max_length=100)),
                ('H_55_59_ans', models.CharField(default='0', max_length=100)),
                ('H_60_64_ans', models.CharField(default='0', max_length=100)),
                ('H_65_69_ans', models.CharField(default='0', max_length=100)),
                ('H_70_74_ans', models.CharField(default='0', max_length=100)),
                ('H_75_79_ans', models.CharField(default='0', max_length=100)),
                ('H_80_99_ans', models.CharField(default='0', max_length=100)),
                ('H_NR', models.CharField(max_length=100)),
                ('NR_NR', models.CharField(max_length=100)),
                ('Total', models.CharField(max_length=100)),
                ('Date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Player',
        ),
    ]
