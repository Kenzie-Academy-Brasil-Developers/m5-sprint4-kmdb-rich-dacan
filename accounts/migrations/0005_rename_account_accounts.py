# Generated by Django 4.1 on 2022-08-25 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        ("admin", "0003_logentry_add_action_flag_choices"),
        ("authtoken", "0003_tokenproxy"),
        ("reviews", "0001_initial"),
        ("accounts", "0004_rename_accounts_account"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Account",
            new_name="Accounts",
        ),
    ]