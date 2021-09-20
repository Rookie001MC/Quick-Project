from django.db import models
from django.core.validators import RegexValidator

jail_section = (
    ("Nhà giam chung", "Nhà giam chung"),
    ("Nhà giam riêng", "Nhà giam riêng"),
    ("Nhà kỉ luật", "Nhà kỷ luật"),
)

# Create your models here.


class Prisoner(models.Model):
    prisoner_id = models.CharField(
        primary_key=True,
        max_length=6, 
        validators=[RegexValidator(r'^\d{1,10}$')]
    )
    prisoner_name = models.CharField(
        max_length=64,
        unique=True
    )
    prisoner_image = models.ImageField()
    prisoner_about = models.TextField()
    prisoner_current_charges = models.TextField()
    prisoner_old_charges = models.TextField()
    prisoner_jail_time = models.PositiveSmallIntegerField()
    prisoner_jail_section = models.CharField(
        choices=jail_section, 
        default="common", 
        max_length=20
    )
    prisoner_jail_room = models.PositiveSmallIntegerField()
