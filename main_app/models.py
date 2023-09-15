from django.db import models
from django.urls import reverse

# Create your models here.


class Practice(models.Model): 
    title = models.CharField(max_length=150)
    notes = models.TextField(max_length=250)
    date = models.DateField('Day Practiced')

    def __str__(self): 
        return self.title

    def get_absolute_url(self): 
        return reverse('practices_detail', kwargs={'pk': self.id})
    
    class Meta: 
        ordering = ['-date']
    

class Sheet(models.Model): 
    KEY_CHOICES = (
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
    )

    DIATONIC_CHOICES = (
        ('major', 'Major'),
        ('minor', 'Minor')
    )


    title = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    composer = models.CharField(max_length=100)
    key = models.CharField(
        max_length=20, 
        choices=KEY_CHOICES, 
        default='cnatural'
    )
    diatonic = models.CharField(
        max_length=20, 
        choices=DIATONIC_CHOICES, 
        default='major'
    )
    practices = models.ManyToManyField(Practice) 
    

    def __str__(self):
        return self.title
    
    def get_absolute_url(self): 
        return reverse('detail', kwargs={'sheet_id': self.id})
    
class Listening(models.Model):
    STAR_CHOICES = (
        ('1', '⭐'),
        ('2', '⭐⭐'),
        ('3', '⭐⭐⭐'),
        ('4', '⭐⭐⭐⭐'),
        ('5', '⭐⭐⭐⭐⭐'),
    )

    date = models.DateField('Listening Date')  
    performer = models.CharField(max_length=100)
    review = models.CharField(
        max_length=5,
        choices = STAR_CHOICES,
        default=STAR_CHOICES[0][0]
        )
    sheet = models.ForeignKey(
        Sheet,
        on_delete=models.CASCADE 
    )

    def __str__(self):
        return f'{self.sheet.title} performed by {self.performer} on {self.date} was {self.review}'
    
    class Meta: 
        ordering = ['-review']
    
