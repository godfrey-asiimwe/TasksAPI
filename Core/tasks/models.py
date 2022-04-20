from django.db import models


# Create your models here.
class Task(models.Model):
    task_id = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=1000, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    Active_Status = 1
    Inactive_Status = 0
    STATUS_CHOICES = (
        (Active_Status, 'pending'),
        (Inactive_Status, 'completed'),
    )
    status = models.IntegerField(choices=STATUS_CHOICES, default=Active_Status)
    projectId = models.CharField(max_length=255, null=True, blank=True)
    created_by = models.CharField(max_length=255, null=True, blank=True)
    responsible = models.CharField(max_length=255, null=True, blank=True)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self) -> str:
        return self.name
