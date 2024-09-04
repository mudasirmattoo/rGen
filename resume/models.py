from django.db import models

# Create your models here.

class Profile(models.Model):
            
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.IntegerField(null=True, blank=True)
    linkedin = models.CharField(max_length=200)
    objective = models.TextField(max_length=500)
    
    work1 = models.CharField(max_length=200, null=True, blank=True)
    work1r = models.CharField(max_length=200, null=True, blank=True)
    work1d = models.TextField(max_length=200, null=True, blank=True)
    work2 = models.CharField(max_length=200, null=True, blank=True)
    work2r = models.CharField(max_length=200, null=True, blank=True)
    work2d = models.TextField(max_length=200, null=True, blank=True)
    work3 = models.CharField(max_length=200, null=True, blank=True)
    work3r = models.CharField(max_length=200, null=True, blank=True)
    work3d = models.TextField(max_length=200, null=True, blank=True)
    
    college = models.CharField(max_length=200, null=True, blank=True)
    degree = models.CharField(max_length=200)
    cgpa = models.FloatField(null=True, blank=True)
    ctime = models.CharField(max_length=100, null=True, blank=True)

    
    higher = models.CharField(max_length=200, null=True, blank=True)
    higherp = models.FloatField(null=True, blank=True)
    stime = models.CharField(max_length=100, null=True, blank=True)
    
    high = models.CharField(max_length=200, null=True, blank=True)
    highp = models.FloatField(null=True, blank=True)
    htime = models.CharField(max_length=100, null=True, blank=True)

    proj1 = models.CharField(max_length=200, null=True, blank=True)
    proj1d = models.TextField(max_length=200, null=True, blank=True)
    proj2 = models.CharField(max_length=200, null=True, blank=True)
    proj2d = models.TextField(max_length=200, null=True, blank=True)
    proj3 = models.CharField(max_length=200, null=True, blank=True)
    proj3d = models.TextField(max_length=200, null=True, blank=True)
    

    cert1 = models.CharField(max_length=200,null=True, blank=True)
    cert2 = models.CharField(max_length=200,null=True, blank=True)

    skills = models.TextField(max_length=300,null=True, blank=True)
    ach1 = models.CharField(max_length=200,null=True, blank=True)
    ach2 = models.CharField(max_length=200,null=True, blank=True)
    
    
    def save(self, *args, **kwargs):
        if self.phone == '':
            self.phone = None
        if self.cgpa == '':
            self.cgpa = None
        if self.higherp == '':
            self.higherp = None
        if self.highp == '':
            self.highp = None
        # Add other fields as necessary
        
        super(Profile, self).save(*args, **kwargs)


    def clean_cgpa(self):
        data = self.cleaned_data.get('cgpa')
        if data == '':
            return None
        return data
    
    def clean_higherp(self):
        data = self.cleaned_data.get('higherp')
        if data == '':
            return None
        return data
    
    
    def clean_highp(self):
        data = self.cleaned_data.get('highp')
        if data == '':
            return None
        return data
