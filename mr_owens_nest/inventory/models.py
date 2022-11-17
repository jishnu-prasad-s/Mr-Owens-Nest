from django.db.models import (
    Model, 
    CharField, 
    ImageField, 
    IntegerField, 
    SlugField,
    DateTimeField
)
from django.template.defaultfilters import slugify

class InventoryItems(Model):
    item_code = CharField('Item Code', max_length=20, unique=True)
    name = CharField("Name of Item", max_length=300)
    slug = SlugField('Item Slug', blank=True, null=True)
    thumbnail = ImageField("Thumbnail Image", upload_to='uploads/Inventory/', blank=True)
    stock = IntegerField('Amount of the specified item')
    date_added = DateTimeField('Date Joined', auto_now_add=True)
    date_updated = DateTimeField('Last Updated', auto_now=True)
    
    class Meta:
        verbose_name = "item"
        verbose_name_plural = "items"
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.name)
            self.item_code = self.item_code.upper()
        super(InventoryItems, self).save(*args, **kwargs)
    
    
    
