from django.db import models
import shortuuid

def generate_uuid():
    base = shortuuid.uuid()
    truncated = base[:11]
    return truncated

class Link(models.Model):
    id = models.CharField(max_length=11, 
    primary_key=True, 
    default=generate_uuid, 
    editable=False,
    unique=True)

    created = models.DateField(auto_now_add=True, editable=False)
    
    url = models.URLField(max_length=200)
    clicked = models.PositiveIntegerField(default=0, editable=False)

    def __str__(self):
        return self.url
