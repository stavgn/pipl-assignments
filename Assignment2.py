import pandas as pd
from validate_email import validate_email

"""Assignment 2 - question number 1:
The following code shows the data fill rate for every field. """

data_set = pd.read_excel(r'C:\Users\Green1\Downloads\DataSet7734_USA_Consumers_test-ver2.xls', sheet_name='NewSource-07734ZipCode')
fields = data_set.columns.values.tolist()
for i in range(len(fields)):
    print('fill rate for {} is: {}%'.format(fields[i], data_set[fields[i]].count()/data_set.shape[0]*100))

"""Assignment 2 - question number 2:
To check the reliability of the data i would perform all sorts of tests. Example for some tests: 
The tests goal is to make sure that the data is in fact valid and true.
Make sure the email addresses's syntax is valid and the addresses actually exists.
Check that the living addresses that were given do exists and match the cities in which the profiles claim to live. 
Check that the phone numbers are real and do exists.
All of those test you can perform using different services and libraries like validate_email, pygeocoder, phonenumbers, etc...
Another way to check the reliability is to take a random sample of a few profiles from the data base and check
their properties manually. This could give a general idea of the reliability of the data set.
The following code is an example for a test that checks the percentage of valid emails in the data."""

valid_emails = data_set['EMail'].apply(lambda x: validate_email(x)).count()/data_set['EMail'].count()*100
print('{}% of the emails are valid'.format(valid_emails))



"""Assignment 2 - question number 3:
Another criteria that I can evaluate in order to determine the value of the data set is the correlation between the new data set 
to Pipl's one. That way I can see how much of the new data the company already has. If most of the new data is already known 
by Pipl then I can determine that the value of the data set is poor and the company probably should'nt purchase it.
The following code is checks the correlation between the two data sets in the emails and phone numbers. The correlation
is represented by percentages. The greater the percent, the better the correlation."""

Pipl_data_set = pd.read_excel(r'C:\Users\Green1\Downloads\DataSet7734_USA_Consumers_test-ver2.xls', sheet_name='PiplCurrent-07734ZipCode')

Pipl_data_set['email'] = Pipl_data_set['email'].str.upper()
num_old_emails = pd.merge(data_set, Pipl_data_set, left_on='EMail', right_on='email', how='inner')['email'].nunique()
emails_corr = num_old_emails / data_set['EMail'].count()*100
print("{}% of the emails from the new data set are already in Pipl's database".format(emails_corr))

num_old_phones = pd.merge(data_set, Pipl_data_set, left_on='Phone Number', right_on='phone number', how='inner')['phone number'].nunique()
phones_corr = num_old_phones / data_set['Phone Number'].count()*100
print("{}% of the phone numbers from the new data set are already in Pipl's database".format(phones_corr))
