from django.db import models

class Reactor(models.Model):
    REACTOR_TYPES = [
        ('CSTR', 'Continuous Stirred-Tank Reactor'),
        ('PFR', 'Plug Flow Reactor'),
        ('PBR', 'Packed Bed Reactor'),
        ('BATCH', 'Batch Reactor'),
    ]
    
    name = models.CharField(max_length=100)
    description = models.TextField()
    benefits = models.TextField()
    uses = models.TextField()
    reactor_type = models.CharField(max_length=5, choices=REACTOR_TYPES)

    def __str__(self):
        return self.name