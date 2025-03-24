from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=155)
    image = models.ImageField(upload_to='recipes/',validators=[FileExtensionValidator(allowed_extensions=['jpg','jpeg','png','svg'])])

    def __str__(self):
        return self.name
    
class Steps(models.Model):
    recipe = models.ForeignKey(Recipe,related_name='steps',on_delete=models.CASCADE)
    desc =  models.TextField(100)

    def __str__(self):
        return f'Step {self.desc} \t {self.recipe.name}'
    
class Ingredients(models.Model):
    recipe = models.ForeignKey(Recipe,related_name='ingredients',on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.recipe.name}'                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            