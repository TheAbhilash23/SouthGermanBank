<h1>AbhilashSGBProject</h1>

This repository contains a project on <b>"Prediction of customer credit risk of South German Bank"</b> whose problem statement and requirement was shared by iNeuron.ai .

I have used PYTHON, HTML, CSS for webdevelopment, AI and ML modelling and Django and Django Rest Framework to carry out the tasks.

The project flow is as follows.

An employee signs up on the portal through link on the Navbar (whose data gets stored in the database) The employee then has to log in (using django user model) after logging in, the employee has to choose between the application he/she wishes to use, 1st Choice is Analyser App and the , 2nd Choice is CRUD Operations

<h2>Analyser Application</h2>
To analyse the given data (stored in model Odb) we have to input the independent variables through a form. The application uses Logistic Regression (on 75% of the given data to train the model and 25% for testing accuracy)
Once a valid form is submitted, the application returns a prediction (in our case classification) for the customer whose data has been filled by the employee in the form.

<h2>CRUD Operations</h2>
The employees can add a new customer to the database, Edit the particulars of a specific customer or even delete the data of user from the database.
PS: A customer can enquire about his/her data by submitting his/her details at the customer enquiry page (where his/her data is stored in the database).
