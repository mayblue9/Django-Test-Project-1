from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class CardSession(models.Model):
    name = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.name        

class Card(models.Model):
    name = models.CharField(max_length=200)
    x_coord = models.FloatField()
    y_coord = models.FloatField()
    global_id = models.CharField(max_length=250, unique=True) # rdf id, format is "0000-[session_id]-[name]"
    session = models.ForeignKey(CardSession)
    
    def __unicode__(self):
        return u'%s %s' % (self.name, self.global_id)
    
    class Meta:
        ordering = ['id']
        
        

# called evey time an object is saved
@receiver(post_save, sender=Card)
def saveSuccess(sender, **kwargs):
    if 'created' in kwargs:
        if kwargs['created']:
            print "New card added"
        else:
            print "Card not added.  Duplicate entry found."