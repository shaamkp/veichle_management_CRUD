from django.db import models


GENERAL_VEICHLE_TYPE_CHOICES = [
    ('two_wheeler', 'Two_Wheeler'),
    ('three_wheeler', 'Three_Wheeler'),
    ('four_wheeler', 'Four_Wheeler'),
]


class VeichleDetails(models.Model):
    number = models.CharField(max_length=128)
    veichle_type = models.CharField(choices=GENERAL_VEICHLE_TYPE_CHOICES, max_length=128)
    model = models.CharField(max_length=128)
    description = models.TextField(blank=True, null=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'general_veichle_details'
        verbose_name ='Veichle Detail'
        verbose_name_plural ='Veichle Details'
        ordering = ('id',)

    def __str__(self):
        return str(self.id)
