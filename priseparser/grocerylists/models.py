from django.db import models


class GroceryLists(models.Model):
    list_id = models.SmallAutoField(primary_key=True)
    title = models.CharField('List title', max_length=50, default='MyList')
    note = models.CharField('Note for list', max_length=250, default='')
    creation_date = models.DateField('Date of list creation')
    red_date = models.DateField('Date of the planned shopping')

    def __str__(self):
        return self.title

