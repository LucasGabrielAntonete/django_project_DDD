from django.db import models
import uuid

class Publisher(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "publisher"
        verbose_name = "Publisher"
        verbose_name_plural = "Publishers"