from django.db import models
from django.urls import reverse

# Create your models here.


class Sheet(models.Model): 
    key_choices = [
    ('cflat', 'C♭'),
    ('cnatural', 'C'),
    ('csharp', 'C♯'),
    ('dflat', 'D♭'),
    ('dnatural', 'D'),
    ('dsharp', 'D♯'),
    ('eflat', 'E♭'),
    ('enatural', 'E'),
    ('esharp', 'E♯'),
    ('fflat', 'F♭'),
    ('fnatural', 'F'),
    ('fsharp', 'F♯'),
    ('gflat', 'G♭'),
    ('gnatural', 'G'),
    ('gsharp', 'G♯'),
    ('aflat', 'A♭'),
    ('anatural', 'A'),
    ('asharp', 'A♯'),
    ('bflat', 'B♭'),
    ('bnatural', 'B'),
    ]

    diatonic_choices = [
        ('major', 'Major'),
        ('minor', 'Minor')
    ]


    title = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    composer = models.CharField(max_length=100)
    key = models.CharField(
        max_length=20, 
        choices=key_choices, 
        default='cnatural'
    )
    diatonic = models.CharField(
        max_length=20, 
        choices=diatonic_choices, 
        default='major'
    )
    

    def __str__(self):
        return self.title
    
    def get_absolute_url(self): 
        return reverse('detail', kwargs={'sheet_id': self.id})
    
    