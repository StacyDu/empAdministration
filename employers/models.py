from time import strftime

from django.core.validators import MinValueValidator
from django.db import models

REFERENCE_CHOICES = (
    (0, 'Facebook'),
    (1, '4programmers'),
    (2, 'Staff'),
    (3, 'Applicant'),
)

TECHNOLOGIES_CHOICES = (
    (0, 'Python'),
    (1, 'JavaScript'),
    (2, 'Java'),
    (3, 'Golang'),
    (4, 'C#'),
    (5, 'C++'),
    (6, 'Blockchain'),
    (7, 'Data Science'),
    (8, 'Machine Learning'),
    (9, 'Groovy'),
    (10, 'Kotlin'),
    (11, 'Android'),
    (12, 'iOS'),
    (13, 'Scala'),
    (14, 'PHP'),
    (15, 'DevOps'),
    (16, 'Kotlin'),
    (17, 'Ruby'),
)


# Table with Technologies

class Technologies(models.Model):
    technology_name = models.CharField(max_length=128)


# Table with developers


class Developers(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    middle_name = models.CharField(max_length=64, null=True)
    email = models.CharField(max_length=128)
    salary = models.IntegerField(validators=[MinValueValidator(0)])
    date_hired = models.DateField(null=True)
    notes = models.CharField(max_length=128, null=True)
    reference = models.IntegerField(choices=REFERENCE_CHOICES)
    technology = models.ManyToManyField(
        Technologies,
        through='DevelopersTechnologies',
    )


# Table with personal details needed for contracts


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


# Table with pdf documents of all contracts for different tasks

def contract_path(self, instance: Developers):
    return "/{}_{}_{}_{}.pdf".format(instance.first_name, instance.last_name, instance.id, strftime('%Y%m%d'))


class DevelopersContracts(models.Model):
    contract = models.FileField(upload_to=contract_path, null=True, blank=True)
    developer = models.ForeignKey(Developers, on_delete=models.PROTECT)


# Table with Technologies per candidate and vice versa


class DevelopersTechnologies(models.Model):
    developer = models.ForeignKey(Developers, on_delete=models.PROTECT)
    technology_name = models.ForeignKey(Technologies, on_delete=models.PROTECT)
