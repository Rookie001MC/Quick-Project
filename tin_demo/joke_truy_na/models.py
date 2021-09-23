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
        validators=[RegexValidator(r'^\d{1,10}$')],
        verbose_name="Mã tù nhân"
    )
    prisoner_name = models.CharField(
        max_length=64,
        unique=True,
        verbose_name="Họ tên"
    )
    prisoner_image = models.ImageField(verbose_name="Ảnh tù nhân")
    prisoner_about = models.TextField(verbose_name="Tiểu sử")
    prisoner_current_charges = models.TextField(verbose_name="Tội trạng")
    prisoner_old_charges = models.TextField(verbose_name="Tiền án tiền sự")
    prisoner_jail_time = models.PositiveSmallIntegerField(verbose_name="Thời gian giam giữ")
    prisoner_jail_section = models.CharField(
        choices=jail_section, 
        default="common", 
        max_length=20,
        verbose_name="Khu giam giữ"
    )
    prisoner_jail_room = models.PositiveSmallIntegerField(verbose_name="Phòng giam")
