from django.db import models
from django.utils.translation import gettext_lazy as _
from core.base_items import BaseModel


class CustomerCreditRiskParameters(BaseModel):
    """
    This model contains the values of customer credit risk parameters for existing customers and
     later on will contain the value for new customers
    """
    CustomerId = models.BigAutoField(
        _("Id"),
        primary_key=True,
    )
    IsGoodCreditRisk = models.BooleanField(
        _("Is Good Credit Risk"),
        null=True,
        blank=True,
    )
    Status = models.PositiveIntegerField(
        _("Status of the debtor's checking account with the bank (categorical)"),
        null=True,
        blank=True,
    )
    Duration = models.PositiveIntegerField(
        _("Credit duration in months (quantitative)"),
        null=True,
        blank=True,
    )
    CreditHistory = models.PositiveIntegerField(
        _("History of compliance with previous or concurrent credit contracts (categorical)"),
        null=True,
        blank=True,
    )
    Purpose = models.PositiveIntegerField(
        _("Purpose for which the credit is needed (categorical)"),
        null=True,
        blank=True,
    )
    Amount = models.PositiveIntegerField(
        _("Credit amount in DM (quantitative)"),
        null=True,
        blank=True,
    )
    Savings = models.PositiveIntegerField(
        _("Debtor's savings (categorical)"),
        null=True,
        blank=True,
    )
    EmploymentDuration = models.PositiveIntegerField(
        _("Duration of debtor's employment with current employer (ordinal; discrete quantitative)"),
        null=True,
        blank=True,
    )
    InstallmentRate = models.PositiveIntegerField(
        _("Credit installments as a percentage of debtor's disposable income (ordinal; discrete quantitative)"),
        null=True,
        blank=True,
    )
    PersonalStatusSex = models.PositiveIntegerField(
        _("Combined information on sex and marital status; categorical"),
        null=True,
        blank=True,
    )
    OtherDebtors = models.PositiveIntegerField(
        _("Is there another debtor or a guarantor for the credit? (categorical)"),
        null=True,
        blank=True,
    )
    PresentResidence = models.PositiveIntegerField(
        _("Length of time (in years) the debtor lives in the present residence (ordinal)"),
        null=True,
        blank=True,
    )
    MostValuableProperty = models.PositiveIntegerField(
        _("The debtor's most valuable property (choices)"),
        null=True,
        blank=True,
    )
    Age = models.PositiveIntegerField(
        _("Age in years (quantitative)"),
        null=True,
        blank=True,
    )
    OtherInstallmentPlans = models.PositiveIntegerField(
        _("Installment plans from providers other than the credit-giving bank (categorical)"),
        null=True,
        blank=True,
    )
    Housing = models.PositiveIntegerField(
        _("Type of housing the debtor lives in (categorical)"),
        null=True,
        blank=True,
    )
    NumberCredits = models.PositiveIntegerField(
        _("Number of credits including the current one the debtor has (or had) at this bank (ordinal, discrete"
          "quantitative)"),
        null=True,
        blank=True,
    )
    Job = models.PositiveIntegerField(
        _("Quality of debtor's job (ordinal)"),
        null=True,
        blank=True,
    )
    PeopleLiable = models.PositiveIntegerField(
        _("Number of persons who financially depend on the debtor (i.e., are entitled to maintenance) "
          "(binary,discrete quantitative)"),
        null=True,
        blank=True,
    )
    HasTelephone = models.BooleanField(
        _("Is there a telephone landline registered on the debtor's name?"),
        null=True,
        blank=True,
    )
    IsForeignWorker = models.PositiveIntegerField(
        _("Is the debtor a foreign worker?"),
        null=True,
        blank=True,
    )

    def credit_risk_status(self):
        if self.IsGoodCreditRisk:
            return "High Credit Risk"
        elif not self.IsGoodCredit:
            return "Low Credit Risk"

    def get_customer(self):
        return self.CustomerId

    def __str__(self):
        return f"{self.CustomerId} {self.credit_risk_status()}"


    class Meta:
        verbose_name = _("Customer Parameter")
        verbose_name_plural = _("Customer Parameters")
        db_table = "CustomerParameters"


class CustomerInformation(BaseModel):
    Customer = models.OneToOneField(
        "customers.CustomerCreditRiskParameters",
        on_delete=models.CASCADE,
        primary_key=True,
    )
    Name = models.CharField(
        _("Name"),
        max_length=225,
        null=True,
        blank=True,
        default='',
    )
    Telephone = models.CharField(
        _("Phone number"),
        max_length=20,
        null=True,
        blank=True,
        default='',
    )
    Email = models.EmailField(
        _("Email address"),
        max_length=250,
        null=True,
        blank=True,
        default='',
    )
    SocialMediaLink = models.CharField(
        _("Social media link"),
        max_length=155,
        null=True,
        blank=True,
        default='',
    )
    HighestEducation = models.CharField(
        _("Highest education"),
        null=True,
        blank=True,
        max_length=150,
        default='',
    )

    def __str__(self):
        return f"{self.Name}"

    class Meta:
        verbose_name = _("Customer Information")
        verbose_name_plural = _("Customers Information")
        db_table = "CustomerInformation"
