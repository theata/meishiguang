from django.db import models

class TimeLine(models.Model):

    PRIVACY_LEVELS = (
        (1, 'all people could access'),
        (2, u'only friends could access'),
        (3, u'just self could access'),
    )

    title = models.CharField(max_length=128)
    summary = models.CharField(max_length=4096)
    ctime = models.DateField(auto_now_add=True, blank=False)
    ptime = models.DateField(auto_now_add=True, blank=False)
    privacy = models.IntegerField(choices=PRIVACY_LEVELS)

    def __unicode__(self):
        return self.title


class Event(models.Model):
    summary = models.CharField(max_length=1024,null=True)
    ctime = models.DateField(blank=True)
    url = models.URLField(null=True)


    def __unciode__(self):
        return self.summary

