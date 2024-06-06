from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from project.models import Project  # Replace with your actual models
from task.models import Task  # Replace with your actual models
from user.models import MyModel3  # Replace with your actual models
import random

class Command(BaseCommand):
    help = 'Create users, assign permissions, and add them to groups'

    def handle(self, *args, **kwargs):
        create_users_and_assign_permissions()

def create_users_and_assign_permissions():
    # Create users
    users_data = [
        {'username': 'admin_user', 'email': 'admin@example.com', 'password': 'adminpass'},
        {'username': 'manager_user', 'email': 'manager@example.com', 'password': 'managerpass'},
        {'username': 'employee_user1', 'email': 'employee1@example.com', 'password': 'employeepass1'},
        {'username': 'employee_user2', 'email': 'employee2@example.com', 'password': 'employeepass2'},
    ]

    users = []
    for user_data in users_data:
        user, created = User.objects.get_or_create(username=user_data['username'], defaults={
            'email': user_data['email']
        })
        if created:
            user.set_password(user_data['password'])
            user.save()
        users.append(user)

    # Create groups and assign permissions if they don't exist
    groups = ['Admins', 'Managers', 'Employees']
    for group_name in groups:
        group, created = Group.objects.get_or_create(name=group_name)

    # Define all models you want to assign permissions for
    models = [Project, Task, MyModel3]

    # Get all permissions for these models
    all_permissions = []
    for model in models:
        content_type = ContentType.objects.get_for_model(model)
        permissions = Permission.objects.filter(content_type=content_type)
        all_permissions.extend(permissions)

    # Assign random permissions to users
    for user in users:
        num_permissions = random.randint(1, len(all_permissions))
        user_permissions = random.sample(all_permissions, num_permissions)
        for perm in user_permissions:
            user.user_permissions.add(perm)

    # Add users to groups
    admin_group = Group.objects.get(name='Admins')
    manager_group = Group.objects.get(name='Managers')
    employee_group = Group.objects.get(name='Employees')

    admin_user = User.objects.get(username='admin_user')
    admin_user.groups.add(admin_group)

    manager_user = User.objects.get(username='manager_user')
    manager_user.groups.add(manager_group)

    employee_user1 = User.objects.get(username='employee_user1')
    employee_user1.groups.add(employee_group)

    employee_user2 = User.objects.get(username='employee_user2')
    employee_user2.groups.add(employee_group)

    print("Users created, permissions assigned, and users added to groups successfully.")
