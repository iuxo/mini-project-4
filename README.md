# Mini-project IV

### [Assignment](assignment.md)

## Project/Goals
Use Machine Learning to predict whether or not an applicant will be approved for a loan based on questionnaire they fill out.
Questionnaire asks basic information like Gender, Marital Status, Education, Income, etc...
Deploy the model to a Flask webpage where the applicants can fill out the questionnaire and get a prediction to their loan approval.

## Hypothesis
Applicants who have a credit score previously are more likely to get their loan approved.
Applicants with a higher income (Applicant + Coapplicant) are more likely to get their loan approved.
Applicants who have higher education are more likely to get their loan approved.
Applicants who live in urban areas are more likely to get their loan approved.
Some other hypothesis: the use case of the loan, applicants who want to use the loan for business or learning
are more likely to get their loan approved compared to a loan for personal.

To test my hypotheses, I graphed out the different features against whether or not the loan status was approved. For example, I seperated
the data based on education levels. I saw that applicants who have higher education are more likely to get their loan approved.

## EDA 
While working with the data I noticed that there were columns that had multiple null values (Gender, Dependents, Self_Employed, LoanAmount etc..). Some of these columns would require different imputations to be correctly filled out. I also noticed the data was highly imbalanced based on gender. So I thought the model could be influenced by this imbalance and there may be some bias (sexism) when the model is fit to the data.


## Process
### Data Exploration
The first step was to just look at the data and kind of explore it to see how much data I was working with and what kind of features were provided and can be engineered.
### Data Cleaning
After working with the data, I had to deal with missing values via imputation and log transform some of the more extreme values.
### Modelling
After dealing with the extremities, I worked on creating a model using Random Forest as a baseline. Then further tuning it using GridSearch.
### Pipelining
Then I redid the modelling, using a pipeline so that it would be easier to deploy into the cloud.
### Deployment
After pipelining and pickling the model I created. I deployed it to an AWS instance. To get predictions requires sending a JSON request via the request library in python or using Postman.

## Results/Demo
To get a prediction, you have to send a JSON payload via the request library or using Postman. Here is an example with the predicition.
![Screenshot](images/request_proj_4.png)
![Screenshot](images/predict_proj_4.png)

## Challanges 
It was difficult trying to use the pipeline as there were multiple transformers and trying to figure out exactly in exactly what process should the transforms happen took a good chunk of time.
Another challenge I faced was working with the AWS instance, the initial instance I was working with had an old version of sklearn, so when I tried to run the model on the cloud, it gave back a lot of errors and didn't work.

## Future Goals
Refactoring my code to make it more legible, right now the instruction notebook is a mess because of all the tinkering I had to do.

I would also try to balance the data using under/over sampling somehow to get rid of some of the gender imbalances as right now there could be some bias based on gender.

Another goal would be to try to make an html page, so instead of sending a json payload via request or Postman, you would be able to go to the page and a questionnaire would pop up that has all the fields to fill and it would send back a prediction.
