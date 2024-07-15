from django.db import models

class Course(models.Model):
    course_title= models.CharField()
    course_category= models.CharField()
    course_start_date= models.DateField()
    course_end_date = models.DateField()
    course_code =models.SmallIntegerField()
    teacher_code= models.SmallIntegerField()
    course_attendees= models.CharField()
# Create your models here.


class MilkRecord:
    def __init__(self, date, amount):
        self.date = date
        self.amount = amount

class LoanApplication:
    def __init__(self, farmer_id, amount_requested, purpose):
        self.farmer_id = farmer_id
        self.amount_requested = amount_requested
        self.purpose = purpose

class TransactionRecord:
    def __init__(self, loan_id, transaction_type, amount):
        self.loan_id = loan_id
        self.transaction_type = transaction_type
        self.amount = amount



class FarmersMobileService:
    def __init__(self):
        self.milk_records = []
        self.loan_applications = []
        self.transactions = []

    def add_milk_record(self, milk_record):
        self.milk_records.append(milk_record)

    def submit_loan_application(self, loan_application):
        self.loan_applications.append(loan_application)

    def record_transaction(self, transaction_record):
        self.transactions.append(transaction_record)
