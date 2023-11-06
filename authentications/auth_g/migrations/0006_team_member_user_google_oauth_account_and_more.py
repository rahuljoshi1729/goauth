# Generated by Django 4.2.7 on 2023-11-04 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('socialaccount', '0006_alter_socialaccount_extra_data'),
        ('auth_g', '0005_teammember_remove_user_google_oauth_account_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='team_member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('role', models.CharField(choices=[('Bid', 'Bid'), ('Code', 'Code')], max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='google_oauth_account',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='custom_user', to='socialaccount.socialaccount'),
        ),
        migrations.AddField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='leader_email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='payment_amount',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='user',
            name='team_member_2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='member_2', to='auth_g.team_member'),
        ),
        migrations.AlterField(
            model_name='user',
            name='team_member_3',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='member_3', to='auth_g.team_member'),
        ),
        migrations.AlterField(
            model_name='user',
            name='team_member_4',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='member_4', to='auth_g.team_member'),
        ),
        migrations.DeleteModel(
            name='TeamMember',
        ),
    ]
