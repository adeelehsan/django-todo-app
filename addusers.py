#!/usr/bin/env bash
from django.contrib.auth.models import User, Permission
from todo.models import Task

user = User.objects.create_user('ad', password='ad123456')
user.save()
t = Task(title='Learning Django', description='Learning to Change Team')
t.user = user
t.save()

user = User.objects.create_user('adeel', password='adeel123''')
user.save()
t = Task(title='Learning Arabic', description='Try To Learn Arabic')
t.user = user
t.save()

user = User.objects.create_user('specialone', password='special123')
permission = Permission.objects.get(name='can view all task')
user.user_permissions.add(permission)
user.save()
