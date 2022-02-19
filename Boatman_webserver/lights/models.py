from django.db.models import Model, PositiveIntegerField, CharField, ManyToManyField
from django.core.validators import MaxValueValidator

class Light(Model):
    number = PositiveIntegerField(validators=[MaxValueValidator(15)])
    name = CharField(max_length=16)
    duty = PositiveIntegerField(default=0, validators=[MaxValueValidator(255)])
    def __str__(self):
        return self.name

class Group(Model):
    number = PositiveIntegerField(validators=[MaxValueValidator(15)])
    name = CharField(max_length=16)
    duty = PositiveIntegerField(default=0, validators=[MaxValueValidator(255)])
    lights = ManyToManyField(Light)
    def __str__(self):
        return self.name
