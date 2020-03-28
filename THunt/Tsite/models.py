from django.db import models
from django.utils import timezone

# Create your models here.


class Student(models.Model):

    p = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    usn = models.CharField(max_length=20, unique=True)
    year = models.IntegerField()
    branch = models.CharField(max_length=3)

    def __str__(self):
        return self.name

class Answer(models.Model):
    a = models.AutoField(primary_key=True)
    name = models.ForeignKey(Student,on_delete=models.CASCADE)
    l1 = models.CharField(max_length=200, null=True, blank=True)
    l2 = models.CharField(max_length=200, null=True, blank=True)
    l3 = models.CharField(max_length=200, null=True, blank=True)
    l4 = models.CharField(max_length=200, null=True, blank=True)
    l5 = models.CharField(max_length=200, null=True, blank=True)
    l1_time = models.DateTimeField(null=True, auto_now=False, auto_now_add=False)
    l2_time = models.DateTimeField(null=True, auto_now=False, auto_now_add=False)
    l3_time = models.DateTimeField(null=True, auto_now=False, auto_now_add=False)
    l4_time = models.DateTimeField(null=True, auto_now=False, auto_now_add=False)
    l5_time = models.DateTimeField(null=True, auto_now=False, auto_now_add=False)

    def save(self, *args, **kws):
        try:
            um = Answer.objects.get(a=self.a)
            update_submission = True
        except Answer.DoesNotExist:
            update_submission = False

        for flag_no in range(1, 6):
            flag = f"l{flag_no}"
            flag_ts = f"{flag}_time"

            now = getattr(self, flag)
            if update_submission:
                prv = getattr(um, flag)
            else:
                prv = None

            if now != prv:
                setattr(self, flag_ts, timezone.now())

        super().save(*args, **kws)

    def __str__(self):
        ts = (f"l{x}_time"for x in range(1,6))
        submissions = '\n'.join(f"{f} = {getattr(self, f)}" for f in ts)
        return f"***\n{self.name!r}\n{submissions}\n***\n"
