from django.db import models

# Create your models here.
class Enquiry(models.Model):
	name = models.CharField(max_length =60)
	contact = models.CharField(max_length=10)
	emailid = models.CharField(max_length=60)
	age =models.CharField(max_length=40)
	gender = models.CharField(max_length=10)


def __str__(self):
	return self.name


class Equipment(models.Model):
	equipmentname = models.CharField(max_length =100)
	price = models.CharField(max_length=10)
	unit = models.CharField(max_length=10)
	date =models.CharField(max_length=40)
	discription = models.CharField(max_length=200)


def __str__(self):
	return self.name


class Plan(models.Model):
	name = models.CharField(max_length =60)
	amount = models.CharField(max_length=10)
	duration = models.CharField(max_length=30)


def __str__(self):
	return self.name


class Member(models.Model):
	name = models.CharField(max_length =60)
	contact = models.CharField(max_length=10)
	emailid = models.CharField(max_length=60)
	age =models.CharField(max_length=10)
	gender = models.CharField(max_length=10)
	plan = models.CharField(max_length= 30)
	joindate = models.CharField(max_length=50)
	expiredate = models.CharField(max_length=50)
	initialamount= models.CharField(max_length=20)
	remainingamount = models.CharField(max_length=20)


def __str__(self):
	return self.name












