from django.db.models.signals import pre_save
from django.utils import timezone
from django.dispatch import receiver
from todo.models import Task

@receiver(pre_save, sender=Task)
def update_log(sender, **kwargs):
    task = kwargs.get('instance')
    task.log = 'Task[%s] by User[%s] at %s ' % (task.title, task.user.username, timezone.datetime.now())