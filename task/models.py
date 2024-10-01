from django.db import models
from django.utils import timezone  # Correct import for timezone.now()
from datetime import timezone as dt_timezone  # Import Python's timezone for UTC handling

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class TodoTask(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    created = models.DateField(default=timezone.now)  # Correct use of timezone.now
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    # Example of using UTC from datetime module if needed
    def get_created_in_utc(self):
        return self.created.astimezone(dt_timezone.utc)
