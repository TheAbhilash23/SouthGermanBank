from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, QueryDict
from django.views.generic.base import TemplateView, RedirectView
from django.views.decorators.csrf import csrf_protect

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from visitors import serializers, models

# import datetime
#
# import pandas as pd
# import numpy as np
# Create your views here.


class VisitorView(ModelViewSet):
    queryset = models.Visitor.objects.all()
    serializer_class = serializers.VisitorSerializer
    # permission_classes = (IsAuthenticated,)

    @action(
        methods=['get', 'post'],
        detail=True,
        serializers=serializers.VisitorSerializer
    )
    def visitor(self, request):
        if request.method == 'POST':
            pass
        else:
            pass
        return Response("Well Done", status=200)



        # queryset = Post.objects.none()
        # serializer_class = PostSerializer
        # permission_classes = (IsAuthenticated,)
        # http_method_names = ['get', ]
        #
        # def list(self, request):
        #     query = request.GET.get('query', None)
        #     query_set = Post.objects.filter(title__icontains=query)
        #     return Response(self.serializer_class(query_set, many=True).data,
        #                     status=status.HTTP_200_OK)

# @csrf_protect
# def customer_enquiry(request):
#     if request.method == 'GET':
#         fm = entryform.customer_enquiry()
#         return render(request, 'visitors/personalinformation.html',
#                       {"pform": fm})
#
#
#     elif request.method == 'POST':
#         fm = entryform.customer_enquiry(request.POST)
#         if fm.is_valid():
#
#             name                = fm.cleaned_data['name']
#             telephone           = fm.cleaned_data['telephone']
#             email               = fm.cleaned_data['email']
#             socialmedia         = fm.cleaned_data['socialmedia']
#             formal_education    = fm.cleaned_data['formal_education']
#
#
#             var = {
#
#                 'name'             :name,
#                 'telephone'        :telephone,
#                 'email'            :email,
#                 'socialmedia'      :socialmedia,
#                 'formal_education' :formal_education,
#             }
#             instance = CustEnquiry(
#                                   name=name,
#                                   telephone=telephone,
#                                   email=email,
#                                   socialmedia=socialmedia,
#                                   formal_education=formal_education,
#
#                                   )
#             instance.save()
#             return render(request, 'visitors/success.html',{"form": fm,'variables':var})
#         else:
#             fm = entryform.customer_personal_data()
#             print("The data is invalid???")
#             return render(request, 'visitors/personalinformation.html',{'pform':fm})
#
#
# class AuthenticationView(View):
#
#     def get(self, request):
#         self.fm = AuthenticationForm()
#
#         return render(request, 'classlogin.html', {'form': self.fm})
#
#
#
#     def post(self, request):
#         self.fm = AuthenticationForm(request=request, data=request.POST)
#
#         if self.fm.is_valid():
#             uname = self.fm.cleaned_data['username']
#             upass = self.fm.cleaned_data['password']
#
#             user = authenticate(username=uname, password=upass)
#             if user is not None:
#
#                 self.var = {'uname': uname}
#                 login(request, user)
#                 global authreq, fm, unameglobal
#                 authreq,fm,unameglobal = request,self.fm,self.var
#
#                 # render(request, 'firstpage_profile.html',{'form': fm, 'var': unameglobal})
#
#                 return HttpResponseRedirect('firstpage_login/')
#
# # class FirstPageProfile(AuthenticationView):
# # def directtoanalyser(request):
# #     if request.method == "POST":
#
#
# class ApplicationSelector(AuthenticationView):
#
#     def get(self,request):
#         sy=entryform.application_selector()
#         # self.oldreq = authreq
#
#         return render(request, 'firstpage_profile.html', {'form':fm, 'var': unameglobal,'sy':sy})
#
#
#     def post(self, request):
#
#         sy = entryform.application_selector(data=request.POST)
#         print('sy app is....: \n\n',request.POST['app'])
#         # render(request, 'firstpage_profile.html', {'form': fm, 'var': unameglobal, 'sy': sy})
#         # print('The sy data is as follows:\n\n\n',sy)
#         if request.POST['app'] == '1':
#             return HttpResponseRedirect('analyser/')
#         elif request.POST['app'] == '2':
#             return HttpResponseRedirect('CRUDOperations/')
#
#
#
#
# class Analyser(AuthenticationView):
#
#
#     def get(self, request):
#
#
#         self.form = entryform.analyser_dropdown(auto_id='form_%s')
#         return render(request, 'visitors/analyser.html',{'form':self.form})
#
#
#
#     def post(self, request):
#
#         self.form = entryform.analyser_dropdown( data = request.POST)
#
#         self.vars = Odb.objects.values()
#         print("The vars are: ", self.vars)
#         print("The formvars are: ",self.form)
#
#
#         #Importing basic libraries of data analysis.
#
#         df = pd.DataFrame(self.vars)
#
#         print("Before dropping custid \n\n",df.head())
#         #We dont need the customerid
#         df=df.drop(columns='custid')
#         print("After dropping custid \n\n",df.head())
#
#         #The data collected from the user ie the attributes of new customer enquiry
#         a = self.form.cleaned_data.values()
#         print("\n\n\n\n\n\n\n\n\n a=",a,type(a))
#         #To make it useable in dataframe
#         b = pd.DataFrame(a)
#         print("\n\n\n\n\n b= ",b.head())
#         #Getting its values only
#         X_predict = b.iloc[:,0]
#         X_predict = [X_predict]
#
#         print("\n\n\n\n\n X_predict=\n\n\n\n\n",X_predict,type(X_predict))
#
#
#
#         #Data from the database for training testing model and prediction purposes
#
#         X = df.iloc[:,1:]
#         Y = df.iloc[:,0]
#
#         print("X:",X,"Y:",Y)
#         #Importing train test split and logistic regression
#         from sklearn.model_selection import train_test_split
#         from sklearn.linear_model import LogisticRegression
#         #Carrying out tts
#         X_train, X_test, Y_train , Y_test = train_test_split(X,Y,train_size=.75,stratify=Y )
#         print("Xtrain:\n",X_train.head(),"\nYtrain\n",Y_train)
#         #Carrying out LogisticRegression on training dataset
#         LR = LogisticRegression(random_state=0,solver='liblinear').fit(X_train, Y_train)
#
#         #Predicting the credit risk (dependent variable) using the data from the FORM (analyser_dropdown)
#         self.prediction = LR.predict(X_predict)
#
#         #For evaluation and testing we need to find Y_predicted
#         self.Y_predicted = LR.predict(X_test)
#
#         #Now we need to calculate confusion matrix
#         #Importing Libraries for confusion matrix
#         from sklearn.metrics import confusion_matrix
#         print('\n\n\n\n\n Confusion Matrix\n\n\n',confusion_matrix(Y_test,self.Y_predicted))
#         self.confusion_matrix = confusion_matrix(Y_test,self.Y_predicted)
#
#         #Importing seaborn library for visualizing
#         # from seaborn import heatmap as sns
#         # #Building confusion matrix as heatmap
#         # plot = sns(self.confusion_matrix/np.sum(self.confusion_matrix), annot=True, fmt='.2%', cmap='Blues')
#
#
#         return render(request, 'visitors/result.html',{'form':self.form,'vars':self.vars,'result':self.prediction})
#
#
#
# class CrudOperations(AuthenticationView):
#
#     form = entryform.editform()
#     var = Odb.objects.all()
#     nform = entryform.addnewform()
#     delform = entryform.delform()
#
#
#     def get(self,request):
#
#         print(request)
#         return render(request,'visitors/crudoperations.html',
#         {'form':self.form,'vars':self.var,'nform':self.nform,'delform':self.delform})
#
#
#     @csrf_protect
#     def post(self, request):
#
#         print(request.POST)
#
#         return render(request,'visitors/crudoperations.html',{'form':self.form,'vars':self.var,'nform':self.nform})
#
#
#
# class AddNewEntry(CrudOperations):
#
#
#     def post(self,request):
#         addfm = entryform.addnewform(auto_id='form_%i',data = request.POST)
#         if addfm.is_valid():
#             print(addfm.data)
#
#             ncredit_risk =addfm.cleaned_data['credit_risk']
#             nstatus =addfm.cleaned_data['status']
#             nduration =addfm.cleaned_data['duration']
#             ncredit_history =addfm.cleaned_data['credit_history']
#             npurpose =addfm.cleaned_data['purpose']
#             namount =addfm.cleaned_data['amount']
#             nsavings =addfm.cleaned_data['savings']
#             nemployment_duration =addfm.cleaned_data['employment_duration']
#             ninstallment_rate =addfm.cleaned_data['installment_rate']
#             npersonal_status_sex =addfm.cleaned_data['personal_status_sex']
#             nother_debtors =addfm.cleaned_data['other_debtors']
#             npresent_residence =addfm.cleaned_data['present_residence']
#             nproperty_type =addfm.cleaned_data['property_type']
#             nage =addfm.cleaned_data ['age']
#             nother_installment_plans =addfm.cleaned_data['other_installment_plans']
#             nhousing =addfm.cleaned_data['housing']
#             nnumber_credits =addfm.cleaned_data['number_credits']
#             njob =addfm.cleaned_data['job']
#             npeople_liable =addfm.cleaned_data['people_liable']
#             ntelephone =addfm.cleaned_data['telephone']
#             nforeign_worker =addfm.cleaned_data['foreign_worker']
#
#             ado = Odb(  credit_risk=ncredit_risk,
#                         status=nstatus ,
#                         duration=nduration,
#                         credit_history=ncredit_history,
#                         purpose=npurpose,
#                         amount=namount,
#                         savings=nsavings,
#                         employment_duration=nemployment_duration,
#                         installment_rate=ninstallment_rate,
#                         personal_status_sex=npersonal_status_sex,
#                         other_debtors=nother_debtors,
#                         present_residence=npresent_residence,
#                         property_type=nproperty_type,
#                         age=nage,
#                         other_installment_plans=nother_installment_plans,
#                         housing=nhousing,
#                         number_credits=nnumber_credits,
#                         job=njob,
#                         people_liable=npeople_liable,
#                         telephone=ntelephone,
#                         foreign_worker=nforeign_worker,)
#
#             ado.save()
#             res={'msg':'Successfully added the new entry'}
#         return HttpResponseRedirect('http://127.0.0.1:8000/crudding/login/firstpage_login/CRUDOperations/')
#
# class DeleteAction(CrudOperations):
#
#
#     def post(self, request):
#         delfm = entryform.delform(data = request.POST)
#         print(delfm['custid'].value())
#         delid = delfm['custid'].value()
#         Odb.objects.get(custid=delid).delete()
#
#         return HttpResponseRedirect('http://127.0.0.1:8000/crudding/login/firstpage_login/CRUDOperations/')
#
#
# class EditAction(CrudOperations):
#
#     def post(self, request):
#         form = entryform.editform(data = request.POST)
#         if form.is_valid():
#             a=[]
#             for i in form.cleaned_data.values():
#                 # print(type(i))
#                 if i != '-1' or i != None:
#                     a.append(form.cleaned_data)
#
#                 else:
#                     continue
#
#             print(a)
#
#
#         return HttpResponseRedirect('http://127.0.0.1:8000/crudding/login/firstpage_login/CRUDOperations/')
#
