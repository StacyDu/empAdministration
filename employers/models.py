from django.core.validators import MinValueValidator
from django.db import models

REFERENCE_CHOICES = (
    (0, 'Facebook'),
    (1, '4programmers'),
    (2, 'Staff'),
    (3, 'Applicant'),
)


class Developers(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    middle_name = models.CharField(max_length=64, null=True)
    email = models.CharField(max_length=128)
    salary = models.IntegerField(validators=[MinValueValidator(0)])
    date_hired = models.DateField(null=True)
    notes = models.CharField(max_length=128, null=True)
    reference = models.IntegerField(choices=REFERENCE_CHOICES)


class PersonalDetails(models.Model):
    developer = models.OneToOneField(Developers, on_delete=models.CASCADE, primary_key=True)
    street = models.CharField(max_length=128)
    postal_code = models.IntegerField(validators=[MinValueValidator(0)])
    city = models.CharField(max_length=128)
    phone_number = models.IntegerField(null=True)
    regon = models.IntegerField(null=True)
    pesel = models.IntegerField(null=True)
    nip = models.IntegerField(null=True)
    company_name = models.CharField(max_length=128, null=True)
    account_number = models.IntegerField(null=True)


class DevelopersContracts(models.Model):
    developer = models.ForeignKey(Developers, on_delete=models.PROTECT, primary_key=True)
    contract = models.FileField(upload_to='pdf/', null=True, blank=True)


class DevelopersTechnologies(models.Model):
    developer = models.OneToOneField(Developers, on_delete=models.CASCADE, primary_key=True)





