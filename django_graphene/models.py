from django.db import models

class Store(models.Model):
    class Meta:
        db_table = "store"

    name = models.CharField(verbose_name="ストア名", max_length=255)
    address = models.CharField(verbose_name="住所", max_length=255)
    is_opened = models.BooleanField(default=False)

class Staff(models.Model):
    class Meta:
        db_table = "staff"

    store = models.ForeignKey(Store, on_delete=models.PROTECT, related_name="staffs")
    name = models.CharField(verbose_name="スタッフ名", max_length=255)
