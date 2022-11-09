from django import forms


class creditrating_input(forms.Form):

    # credit_risk =forms.IntegerField()
    status =forms.IntegerField()
    duration =forms.IntegerField()
    credit_history =forms.IntegerField()
    purpose =forms.IntegerField()
    amount =forms.IntegerField()
    savings =forms.IntegerField()
    employment_duration =forms.IntegerField()
    installment_rate =forms.IntegerField()
    personal_status_sex=forms.IntegerField()
    other_debtors =forms.IntegerField()
    present_residence =forms.IntegerField()
    property_type =forms.IntegerField()
    age =forms.IntegerField()
    other_installment_plans =forms.IntegerField()
    housing =forms.IntegerField()
    number_credits =forms.IntegerField()
    job =forms.IntegerField()
    people_liable = forms.IntegerField()    
    foreign_worker = forms.IntegerField()
    
    
class customer_enquiry(forms.Form):
    # custid              = forms.CharField(widget = forms.HiddenInput, required=False, label = "Customer ID ", )
    name                = forms.CharField(required=True,initial='Abhilash', label = "Name ")
    telephone           = forms.CharField(required = True, widget=forms.NumberInput(),initial='0123456789', label = "Telephone No. ")
    email               = forms.CharField(required = True, widget=forms.EmailInput, initial= "Abhilash@xact.com", label = "Email Address ")
    socialmedia         = forms.CharField(widget=forms.URLInput, initial="https://www.linkedin.com/in/abhilash23/", label = "Social Media Profile Link ")
    formal_education    = forms.CharField(required=False, label = "Highest Education ")

    
class analyser_dropdown(forms.Form):
    # qualitative
    status = forms.ChoiceField(required=True,
                                    choices=[(1, '... <    0 DM'), 
                                             (2, '0 <= ... <  200 DM'), 
                                             (3, '... >= 200/salary assignments for at least 1 year'),
                                             (4, 'no checking account')])
   
    duration = forms.IntegerField(required=True,)  # num
    
    credit_history = forms.ChoiceField(required=True,
                                    choices=[(0,'No Credits Taken/All Debts Duly Paid'),
                                             (1,'All Credits At This Bank Paid Back Duly'),
                                             (2,'Existing credits paid back duly till now'),
                                             (3,'Delay in paying off in the past'),
                                             (4, 'Critical account/other credits existing(not at this bank)'),
                                            ])  # qualit
    
    purpose = forms.ChoiceField(required=True,
                                    choices=[(0, 'Car (new)'),
                                             (1, 'Car (used)'),
                                             (2, 'Furniture/equipment'),
                                             (3, 'Radio/television'),
                                             (4, 'Domestic appliances'),
                                             (5, 'Repairs'),
                                             (6, 'Education'),
                                             (7, '(Vacation - does not exist?)'),
                                             (8, 'Retraining'),
                                             (9, 'Business'),
                                             (10,' Others'),
                                              ])  # qualit'),
    
    
    amount = forms.IntegerField(required=True,)  # numer

    
    savings = forms.ChoiceField(required=True,
                                    choices=[(1,'Less than 100 DM'),
                                             (2, '100 to 500 DM'),
                                             (3,'500 to 1000 DM'),
                                             (4,'More than 1000 DM'),
                                             (5,'Unknown / no savings account')
                                            ]) #qualitative
    
    employment_duration = forms.ChoiceField(required=True,
                                    choices=[(1,'Unemployed'),
                                             (2,'Less than 1 year'),
                                             (3,'1 to 4 years'),
                                             (4,'4 to 7 years'),
                                             (5,'More than 7 years'),
                                                                ])

    installment_rate = forms.IntegerField(required=True,)
  
    personal_status_sex = forms.ChoiceField(required=True,
                                    choices=[(1,'Male: divorced/separated'),
                                             (2,'Female: divorced/separated/married'),
                                             (3,'Male: single'),
                                             (4,'Male: married/widowed'),
                                             (5,'Female: single'),
                                            ]) #
    
    other_debtors = forms.ChoiceField(required=True,
                                    choices=[(1,'None'),
                                             (2,'Co-applicant'),
                                             (3,'Guarantor'),
                                            ]) #
    
    present_residence = forms.IntegerField(
        required=True, label='Number of years at current residence')
    
    property_type = forms.ChoiceField(required=True,
                                    choices=[(1, 'Real estate'),
                                             (2, 'If not A121: building society savings agreement /life insurance'),
                                             (3, 'If not A121/A122: car or other, not in attribute 6'),
                                             (4, 'Unknown / no property'),
                                            ]) #
    
    age = forms.IntegerField(required=True,)
    
    other_installment_plans = forms.ChoiceField(required=True,
                                    choices=[(1, 'Bank'),
                                             (2, 'Stores'),
                                             (3, 'None'),
                                            ]) #
    
    housing = forms.ChoiceField(required=True,
                                    choices=[(1,'rent'),
                                            (2,'own'),
                                            (3,'for free'),
                                            ]) #
                                
    number_credits = forms.IntegerField(
        required=True, label='Number of credits at this bank')
    
    job = forms.ChoiceField(required=True,
                                    choices=[(1, 'Unemployed / unskilled - non-resident'),
                                            (2, 'Unskilled - resident'),
                                            (3, 'Skilled employee / official'),
                                            (4, 'Management / Self-employed /HQE / Officer'),
                                            ]) #
    
    people_liable = forms.IntegerField(required=True,)
    
    telephone = forms.ChoiceField(required=True,
                                    choices=[(1,'None'),
                                            (2,'Yes, registered under the customers name'),
                                            ])    
    
    foreign_worker = forms.ChoiceField(required=True,
                                    choices=[(1,'Yes'),
                                            (2,'No'),
                                            ]) #
    
    
    
    
class application_selector(forms.Form):
    hiddenkey = forms.UUIDField(required=True,widget=forms.HiddenInput() )
    app = forms.ChoiceField(required=True, choices=[(1,'Analyser'),(2,'CRUD Operations')])




class editform(forms.Form):
    # qualitative
    custid = forms.IntegerField(required=True,
                                label='Customer ID')
    
    status = forms.ChoiceField(
                                    choices=[(-1,'--DO--'),
                                             (1, '... <    0 DM'), 
                                             (2, '0 <= ... <  200 DM'), 
                                             (3, '... >= 200/salary assignments for at least 1 year'),
                                             (4, 'no checking account')])
   
    duration = forms.IntegerField()  # num
    
    credit_history = forms.ChoiceField(
                                    choices=[(-1,'--DO--'),
                                             (0,'No Credits Taken/All Debts Duly Paid'),
                                             (1,'All Credits At This Bank Paid Back Duly'),
                                             (2,'Existing credits paid back duly till now'),
                                             (3,'Delay in paying off in the past'),
                                             (4, 'Critical account/other credits existing(not at this bank)'),
                                            ])  # qualit
    
    purpose = forms.ChoiceField(
                                    choices=[(-1,'--DO--'),
                                             (0, 'Car (new)'),
                                             (1, 'Car (used)'),
                                             (2, 'Furniture/equipment'),
                                             (3, 'Radio/television'),
                                             (4, 'Domestic appliances'),
                                             (5, 'Repairs'),
                                             (6, 'Education'),
                                             (7, '(Vacation - does not exist?)'),
                                             (8, 'Retraining'),
                                             (9, 'Business'),
                                             (10,' Others'),
                                              ])  # qualit'),
    
    
    amount = forms.IntegerField()  # numer

    
    savings = forms.ChoiceField(
                                    choices=[(-1,'--DO--'),
                                             (1,'Less than 100 DM'),
                                             (2, '100 to 500 DM'),
                                             (3,'500 to 1000 DM'),
                                             (4,'More than 1000 DM'),
                                             (5,'Unknown / no savings account')
                                            ]) #qualitative
    
    employment_duration = forms.ChoiceField(
                                    choices=[(-1,'--DO--'),
                                             (1,'Unemployed'),
                                             (2,'Less than 1 year'),
                                             (3,'1 to 4 years'),
                                             (4,'4 to 7 years'),
                                             (5,'More than 7 years'),
                                                                ])

    installment_rate = forms.IntegerField()
  
    personal_status_sex = forms.ChoiceField(
                                    choices=[(-1,'--DO--'),
                                             (1,'Male: divorced/separated'),
                                             (2,'Female: divorced/separated/married'),
                                             (3,'Male: single'),
                                             (4,'Male: married/widowed'),
                                             (5,'Female: single'),
                                            ]) #
    
    other_debtors = forms.ChoiceField(required=True,
                                    choices=[(-1,'--DO--'),
                                             (1,'None'),
                                             (2,'Co-applicant'),
                                             (3,'Guarantor'),
                                            ]) #
    
    present_residence = forms.IntegerField(
        label='Number of years at current residence')
    
    property_type = forms.ChoiceField(
                                    choices=[(-1,'--DO--'),
                                             (1, 'Real estate'),
                                             (2, 'If not A121: building society savings agreement /life insurance'),
                                             (3, 'If not A121/A122: car or other, not in attribute 6'),
                                             (4, 'Unknown / no property'),
                                            ]) #
    
    age = forms.IntegerField()
    
    other_installment_plans = forms.ChoiceField(
                                    choices=[(-1,'--DO--'),
                                             (1, 'Bank'),
                                             (2, 'Stores'),
                                             (3, 'None'),
                                            ]) #
    
    housing = forms.ChoiceField(
                                    choices=[(-1,'--DO--'),
                                             (1,'rent'),
                                            (2,'own'),
                                            (3,'for free'),
                                            ]) #
                                
    number_credits = forms.IntegerField(
         label='Number of credits at this bank')
    
    job = forms.ChoiceField(
                                    choices=[(-1,'--DO--'),
                                             (1, 'Unemployed / unskilled - non-resident'),
                                            (2, 'Unskilled - resident'),
                                            (3, 'Skilled employee / official'),
                                            (4, 'Management / Self-employed /HQE / Officer'),
                                            ]) #
    
    people_liable = forms.IntegerField()
    
    telephone = forms.ChoiceField(
                                    choices=[(-1,'--DO--'),
                                             (1,'None'),
                                            (2,'Yes, registered under the customers name'),
                                            ])    
    
    foreign_worker = forms.ChoiceField(
                                    choices=[(-1,'--DO--'),
                                             (1,'Yes'),
                                            (2,'No'),
                                            ]) #
class addnewform(forms.Form):
    # qualitative
    credit_risk = forms.ChoiceField(required=True, 
                                    choices=[(0,'Low Risk'),
                                             (1,'High Risk')
                                             ])
    
    status = forms.ChoiceField(required=True,
                                    choices=[(1, '... <    0 DM'), 
                                             (2, '0 <= ... <  200 DM'), 
                                             (3, '... >= 200/salary assignments for at least 1 year'),
                                             (4, 'no checking account')])
   
    duration = forms.IntegerField(required=True,)  # num
    
    credit_history = forms.ChoiceField(required=True,
                                    choices=[(0,'No Credits Taken/All Debts Duly Paid'),
                                             (1,'All Credits At This Bank Paid Back Duly'),
                                             (2,'Existing credits paid back duly till now'),
                                             (3,'Delay in paying off in the past'),
                                             (4, 'Critical account/other credits existing(not at this bank)'),
                                            ])  # qualit
    
    purpose = forms.ChoiceField(required=True,
                                    choices=[(0, 'Car (new)'),
                                             (1, 'Car (used)'),
                                             (2, 'Furniture/equipment'),
                                             (3, 'Radio/television'),
                                             (4, 'Domestic appliances'),
                                             (5, 'Repairs'),
                                             (6, 'Education'),
                                             (7, '(Vacation - does not exist?)'),
                                             (8, 'Retraining'),
                                             (9, 'Business'),
                                             (10,' Others'),
                                              ])  # qualit'),
    
    
    amount = forms.IntegerField(required=True,)  # numer

    
    savings = forms.ChoiceField(required=True,
                                    choices=[(1,'Less than 100 DM'),
                                             (2, '100 to 500 DM'),
                                             (3,'500 to 1000 DM'),
                                             (4,'More than 1000 DM'),
                                             (5,'Unknown / no savings account')
                                            ]) #qualitative
    
    employment_duration = forms.ChoiceField(required=True,
                                    choices=[(1,'Unemployed'),
                                             (2,'Less than 1 year'),
                                             (3,'1 to 4 years'),
                                             (4,'4 to 7 years'),
                                             (5,'More than 7 years'),
                                                                ])

    installment_rate = forms.IntegerField(required=True,)
  
    personal_status_sex = forms.ChoiceField(required=True,
                                    choices=[(1,'Male: divorced/separated'),
                                             (2,'Female: divorced/separated/married'),
                                             (3,'Male: single'),
                                             (4,'Male: married/widowed'),
                                             (5,'Female: single'),
                                            ]) #
    
    other_debtors = forms.ChoiceField(required=True,
                                    choices=[(1,'None'),
                                             (2,'Co-applicant'),
                                             (3,'Guarantor'),
                                            ]) #
    
    present_residence = forms.IntegerField(
        required=True, label='Number of years at current residence')
    
    property_type = forms.ChoiceField(required=True,
                                    choices=[(1, 'Real estate'),
                                             (2, 'If not A121: building society savings agreement /life insurance'),
                                             (3, 'If not A121/A122: car or other, not in attribute 6'),
                                             (4, 'Unknown / no property'),
                                            ]) #
    
    age = forms.IntegerField(required=True,)
    
    other_installment_plans = forms.ChoiceField(required=True,
                                    choices=[(1, 'Bank'),
                                             (2, 'Stores'),
                                             (3, 'None'),
                                            ]) #
    
    housing = forms.ChoiceField(required=True,
                                    choices=[(1,'rent'),
                                            (2,'own'),
                                            (3,'for free'),
                                            ]) #
                                
    number_credits = forms.IntegerField(
        required=True, label='Number of credits at this bank')
    
    job = forms.ChoiceField(required=True,
                                    choices=[(1, 'Unemployed / unskilled - non-resident'),
                                            (2, 'Unskilled - resident'),
                                            (3, 'Skilled employee / official'),
                                            (4, 'Management / Self-employed /HQE / Officer'),
                                            ]) #
    
    people_liable = forms.IntegerField(required=True,)
    
    telephone = forms.ChoiceField(required=True,
                                    choices=[(1,'None'),
                                            (2,'Yes, registered under the customers name'),
                                            ])    
    
    foreign_worker = forms.ChoiceField(required=True,
                                    choices=[(1,'Yes'),
                                            (2,'No'),
                                            ]) #
    
    
    
    
class application_selector(forms.Form):
    hiddenkey = forms.UUIDField(required=True,widget=forms.HiddenInput() )
    app = forms.ChoiceField(required=True, choices=[(1,'Analyser'),(2,'CRUD Operations')])




class editform(forms.Form):
    # qualitative
    custid = forms.IntegerField(required=True,
                                label='Customer ID')
    
    credit_risk = forms.ChoiceField(required=False, 
                                    choices=[(-1,'--DO--'),
                                             (0,'Low Risk'),
                                             (1,'High Risk'),
                                             ])
    
    status = forms.ChoiceField(required=False,
                                    choices=[(-1,'--DO--'),
                                             (1, '... <    0 DM'), 
                                             (2, '0 <= ... <  200 DM'), 
                                             (3, '... >= 200/salary assignments for at least 1 year'),
                                             (4, 'no checking account')])
   
    duration = forms.IntegerField(required=False,)  # num
    
    credit_history = forms.ChoiceField(required=False,
                                    choices=[(-1,'--DO--'),
                                             (0,'No Credits Taken/All Debts Duly Paid'),
                                             (1,'All Credits At This Bank Paid Back Duly'),
                                             (2,'Existing credits paid back duly till now'),
                                             (3,'Delay in paying off in the past'),
                                             (4, 'Critical account/other credits existing(not at this bank)'),
                                            ])  # qualit
    
    purpose = forms.ChoiceField(required=False,
                                    choices=[(-1,'--DO--'),
                                             (0, 'Car (new)'),
                                             (1, 'Car (used)'),
                                             (2, 'Furniture/equipment'),
                                             (3, 'Radio/television'),
                                             (4, 'Domestic appliances'),
                                             (5, 'Repairs'),
                                             (6, 'Education'),
                                             (7, '(Vacation - does not exist?)'),
                                             (8, 'Retraining'),
                                             (9, 'Business'),
                                             (10,' Others'),
                                              ])  # qualit'),
    
    
    amount = forms.IntegerField(required=False,)  # numer

    
    savings = forms.ChoiceField(required=False,
                                    choices=[(-1,'--DO--'),
                                             (1,'Less than 100 DM'),
                                             (2, '100 to 500 DM'),
                                             (3,'500 to 1000 DM'),
                                             (4,'More than 1000 DM'),
                                             (5,'Unknown / no savings account')
                                            ]) #qualitative
    
    employment_duration = forms.ChoiceField(required=False,
                                    choices=[(-1,'--DO--'),
                                             (1,'Unemployed'),
                                             (2,'Less than 1 year'),
                                             (3,'1 to 4 years'),
                                             (4,'4 to 7 years'),
                                             (5,'More than 7 years'),
                                                                ])

    installment_rate = forms.IntegerField(required=False,)
  
    personal_status_sex = forms.ChoiceField(required=False,
                                    choices=[(-1,'--DO--'),
                                             (1,'Male: divorced/separated'),
                                             (2,'Female: divorced/separated/married'),
                                             (3,'Male: single'),
                                             (4,'Male: married/widowed'),
                                             (5,'Female: single'),
                                            ]) #
    
    other_debtors = forms.ChoiceField(required=False,
                                    choices=[(-1,'--DO--'),
                                             (1,'None'),
                                             (2,'Co-applicant'),
                                             (3,'Guarantor'),
                                            ]) #
    
    present_residence = forms.IntegerField(required=False,
        label='Number of years at current residence')
    
    property_type = forms.ChoiceField(required=False,
                                    choices=[(-1,'--DO--'),
                                             (1, 'Real estate'),
                                             (2, 'If not A121: building society savings agreement /life insurance'),
                                             (3, 'If not A121/A122: car or other, not in attribute 6'),
                                             (4, 'Unknown / no property'),
                                            ]) #
    
    age = forms.IntegerField(required=False,)
    
    other_installment_plans = forms.ChoiceField(required=False,
                                    choices=[(-1,'--DO--'),
                                             (1, 'Bank'),
                                             (2, 'Stores'),
                                             (3, 'None'),
                                            ]) #
    
    housing = forms.ChoiceField(required=False,
                                    choices=[(-1,'--DO--'),
                                             (1,'rent'),
                                            (2,'own'),
                                            (3,'for free'),
                                            ]) #
                                
    number_credits = forms.IntegerField(required=False,
         label='Number of credits at this bank')
    
    job = forms.ChoiceField(required=False,
                                    choices=[(-1,'--DO--'),
                                             (1, 'Unemployed / unskilled - non-resident'),
                                            (2, 'Unskilled - resident'),
                                            (3, 'Skilled employee / official'),
                                            (4, 'Management / Self-employed /HQE / Officer'),
                                            ]) #
    
    people_liable = forms.IntegerField(required=False,)
    
    telephone = forms.ChoiceField(required=False,
                                    choices=[(-1,'--DO--'),
                                             (1,'None'),
                                            (2,'Yes, registered under the customers name'),
                                            ])    
    
    foreign_worker = forms.ChoiceField(required=False,
                                    choices=[(-1,'--DO--'),
                                             (1,'Yes'),
                                            (2,'No'),
                                            ]) #
    
    
    
class delform(forms.Form):
    # qualitative
    custid = forms.IntegerField(required=True,
                                label='Customer ID')