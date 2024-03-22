# Generated by Django 5.0.3 on 2024-03-22 17:27

import django.db.models.functions.text
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        (
            "jobtracker",
            "0024_alter_job_options_alter_organisationalunit_options_and_more",
        ),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="organisationalunit",
            options={
                "ordering": [django.db.models.functions.text.Lower("name")],
                "permissions": (
                    ("manage_members", "Assign Members"),
                    ("can_view_jobs", "Can view jobs"),
                    ("can_add_job", "Can add jobs"),
                    ("can_update_job", "Can update jobs"),
                    (
                        "can_refire_notifications_job",
                        "Can refire notifications for jobs",
                    ),
                    ("can_delete_job", "Can delete jobs"),
                    ("can_add_note_job", "Can add a note to jobs"),
                    ("can_assign_poc_job", "Can assign a Point of Contact to jobs"),
                    (
                        "can_manage_framework_job",
                        "Can assign a Point of Contact to jobs",
                    ),
                    ("can_add_phases", "Can add phases"),
                    ("can_delete_phases", "Can add phases"),
                    ("can_schedule_job", "Can schedule phases"),
                    ("view_users_schedule", "View Members Schedule"),
                    ("view_job_schedule", "View a Job's Schedule"),
                    ("can_scope_jobs", "Can scope jobs"),
                    ("can_signoff_scopes", "Can signoff scopes"),
                    ("can_signoff_own_scopes", "Can signoff own scopes"),
                    ("can_tqa_jobs", "Can TQA jobs"),
                    ("can_pqa_jobs", "Can PQA jobs"),
                    (
                        "can_view_all_leave_requests",
                        "Can view all leave for members of the unit",
                    ),
                    ("can_approve_leave_requests", "Can approve leave requests"),
                ),
            },
        ),
    ]