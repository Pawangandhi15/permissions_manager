import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'base.settings')
django.setup()

from django.contrib.auth.models import Group, Permission

def create_admin_group():
    admin_group, created = Group.objects.get_or_create(name='Admin')
    admin_permissions = Permission.objects.all()
    admin_group.permissions.set(admin_permissions)

def create_manager_group():
    manager_group, created = Group.objects.get_or_create(name='Manager')
    manager_permissions = Permission.objects.filter(
        codename__in=['view_project', 'view_task', 'change_task']
    )
    manager_group.permissions.set(manager_permissions)

def create_employee_group():
    employee_group, created = Group.objects.get_or_create(name='Employee')
    employee_permissions = Permission.objects.filter(
        codename__in=['view_project', 'view_task']
    )
    employee_group.permissions.set(employee_permissions)

if __name__ == '__main__':
    create_admin_group()
    create_manager_group()
    create_employee_group()
    print("Groups and permissions created successfully.")
