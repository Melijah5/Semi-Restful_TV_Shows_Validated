from django.db import models
  
class ShowManager(models.Manager):
    def basic_validation(self, post_data):
        errors ={}
        if not post_data['title'] or not post_data['network'] or not post_data['description'] or not post_data['release_date']:
            errors['fieldes_required'] = 'all fields are required'
        if len(post_data ['title']) < 2:
            # print('The title is less than 2 char!')
            errors['title'] = 'Oops the title must be at least 2 char!'
        if len(post_data ['network']) < 3:
            # print('The network is less than 3 char!')
            errors['title'] = 'Oops the network must be at least 3 char!'
        if len(post_data ['description']) < 10:
            # print('The network is less than 10 char!')
            errors['description'] = 'Oops the description must be at least 10 char!'
        return errors


class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return (f"{self.title} {self.network} {self.release_date} {self.description}")
    
    objects = ShowManager()