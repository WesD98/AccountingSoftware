import django_tables2 as tables
from accounts.models import AccountM

class AccountTable(tables.Table):
    class Meta:
        model = AccountM
        template_name = "django_tables2/semantic.html"
        fields = ("Account_Number", "Account_Name", "Account_Type", "Account_Description" )