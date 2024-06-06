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




#*************************************************************************************************

# import os
# import django

# # Set up Django environment
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'base.settings')
# django.setup()

# from django.contrib.auth.models import Group, Permission, User

# def create_group(name, permissions):
#     try:
#         group, created = Group.objects.get_or_create(name=name)
#         group.permissions.set(permissions)
#         if created:
#             print(f"Group '{name}' created successfully.")
#         else:
#             print(f"Group '{name}' already exists.")
#     except Exception as e:
#         print(f"An error occurred while creating the group '{name}': {e}")

# def create_user(username, password, email, group_name):
#     try:
#         user, created = User.objects.get_or_create(username=username)
#         if created:
#             user.set_password(password)
#             user.email = email
#             user.save()
#             group = Group.objects.get(name=group_name)
#             user.groups.add(group)
#             print(f"User '{username}' created and added to group '{group_name}' successfully.")
#         else:
#             print(f"User '{username}' already exists.")
#     except Group.DoesNotExist:
#         print(f"Group '{group_name}' does not exist.")
#     except Exception as e:
#         print(f"An error occurred while creating the user '{username}': {e}")

# def create_admin_group():
#     admin_permissions = Permission.objects.all()
#     create_group('Admin', admin_permissions)

# def create_manager_group():
#     manager_permissions = Permission.objects.filter(
#         codename__in=['view_project', 'view_task', 'change_task']
#     )
#     create_group('Manager', manager_permissions)

# def create_employee_group():
#     employee_permissions = Permission.objects.filter(
#         codename__in=['view_project', 'view_task']
#     )
#     create_group('Employee', employee_permissions)

# if __name__ == '__main__':
#     create_admin_group()
#     create_manager_group()
#     create_employee_group()
    
#     # Example users
#     create_user('admin_user', 'password123', 'admin@example.com', 'Admin')
#     create_user('manager_user', 'password123', 'manager@example.com', 'Manager')
#     create_user('employee_user', 'password123', 'employee@example.com', 'Employee')

#     print("Groups, permissions, and users created successfully.")
