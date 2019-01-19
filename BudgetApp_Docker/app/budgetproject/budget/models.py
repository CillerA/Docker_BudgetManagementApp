from django.db import models
from django.utils.text import slugify

# Account
class Project(models.Model):
    username = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    budget = models.IntegerField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        super(Project, self).save(*args, **kwargs)

    @property
    def budget_gained(self):
        expense_list = Expense.objects.filter(project=self)
        total_income_amount = 0
        for expense in expense_list:
            if expense.amount < 0:
                total_income_amount = total_income_amount - expense.amount
            
        # temporary solution, because the form currently only allows integer amounts
        total_income_amount = int(total_income_amount)
            
        return self.budget + total_income_amount

    @property
    def budget_left(self):
        expense_list = Expense.objects.filter(project=self)
        total_expense_amount = 0
        for expense in expense_list:
            total_expense_amount += expense.amount
            
        # temporary solution, because the form currently only allows integer amounts
        total_expense_amount = int(total_expense_amount)
            
        return self.budget - total_expense_amount

    @property
    def total_transactions(self):
        expense_list = Expense.objects.filter(project=self)
        return len(expense_list)

class Category(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    category_name = models.CharField(max_length=50)


class Expense(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='expenses')
    title = models.CharField(max_length=100)
    amount = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-amount',)

class Wallet(models.Model):

    # name = 'mywallet'
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    budget = models.IntegerField()
    expenses = models.IntegerField()
    budget_left = models.IntegerField()
    total_transactions = models.IntegerField()

    
    def save(self, *args, **kwargs):
        budget = 0
        self.slug = slugify('wallet')
        super(Project, self).save(*args, **kwargs)
        