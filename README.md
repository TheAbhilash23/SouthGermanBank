<h1>South German Bank Project</h1>

This repository contains a project on <b>"Prediction of customer credit risk of South German Bank"</b> whose problem statement and requirement was shared by iNeuron.ai .

I have used HTML, CSS for Frontend development.

For Backend development I have used Python. This includes <b>Django </b> and <b> Django Rest Framework </b>.The data architecture is monolith for the limited scope of the project.

The Data model has been designed in such a way that it makes the project coherent with its  objectives.

I have also used python for AI and ML modelling for <b> Predicting Customer Credit Risk </b>.


<h3>
Customer Application
	</h3> <br>
This application contains data model for customer credit risk parameters, customer personal information.

This application also handles the prediction for a customer's credit risk.
The admin can enter the credit risk parameters and the credit risk of the customer through admin portal. This application is designed keeping in mind that there are people coming every day to the bank and getting themselves registered for the service and the admin is required to note their information.

<h3>
Visitor Application
	</h3><br>
contains data models for containing personal information of visitors who would like to enquire about the service (prediction of their credit risk). 
The Visitor can submit his/her request or any querry regarding the credit risk. 
The admin will then be able to contact the visitor to get their credit risk evaluated.

<h3>
Data Reader Application
	</h3><br>
This application takes input as either a csv file, or json file with cleaned data (since these are 2 of the most commonly used methods for reading the data and using it for preprocessing.

So, the user is only required to upload a file (csv or json) which will then be read by the application and the data can be used to predict the credit risk.

