from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns


class Category(models.Model):
    """Model representing a menu category (e.g. Coffees, Tea, Iced Coffee, Pastries)."""
    name = models.CharField(
        max_length=200,
        help_text="Enter a menu category (e.g. Coffees, Tea, Iced Coffee, Pastries etc.)"
        )
    
    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        """Returns the url to access a particular category instance."""
        return reverse('category-detail', args=[str(self.id)])
    
    def __str__(self):
        """String for representing the Model object."""
        return '{0}'.format(self.name)

class Menu(models.Model):
    """Model representing a menu (but not a specific copy of a menu)."""
    title = models.CharField(max_length=200)

    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the menu')

    price = models.FloatField()

    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    # Foreign Key used because book can only have one author, but authors can have multiple books
    # Author as a string rather than object because it hasn't been declared yet in file.

    class Meta:
        ordering = ['title', 'category']

    def get_absolute_url(self):
        """Returns the URL to access a detail record for this menu."""
        return reverse('menu-detail', args=[str(self.id)])
    
    def __str__(self):
        """String for representing the Model object."""
        return self.title

