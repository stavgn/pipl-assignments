import pandas as pd
pd.set_option('precision', 7)

"""Assignment 1 - question number 1:
The following code show the frequency of each email domain by percentages.
I assigned all of the email domains from the data set into a list and then used .value counts to show the frequency of 
each one by percentages """

emails_list = pd.read_excel(r'C:\Users\Green1\Downloads\Data_set1.xlsx', sheet_name='random_fictitious_sample')['email']
domains_list = []
for i, value in emails_list.items():
    domains_list.append(emails_list[i].split('@')[1])
print(pd.Series(domains_list).value_counts(normalize=True) * 100)

"""Assignment 1 - question number 2:
The following code show the frequency of each phone type ( mobile / land-line ) and how many of each type by percentages.
I used two lists to count the different profiles, one for each phone type. Each element in the lists represents the 
numbers of phone numbers the profiles have- the first element represents the numbers of profiles having 0 phone numbers,
the second element represents the numbers of profiles having 1 phone numbers, etc... 
For each profile in the data set I counted the number of mobile numbers and the numbers of land-line numbers, then I 
added 1 for the corresponding element in each list."""

data_set = pd.read_excel(r'C:\Users\Green1\Downloads\Data_set1.xlsx', sheet_name='random_fictitious_sample')
mobile_perfixes = pd.read_excel(r'C:\Users\Green1\Downloads\Data_set1.xlsx', sheet_name='mobile prefixes')['mobile prefixes']
phone_numbers = data_set.columns[pd.Series(data_set.columns).str.startswith('phone')]
moblie_count = [0 for i in range(phone_numbers.shape[0]+1)]
landline_count = [0 for i in range(phone_numbers.shape[0]+1)]

for index, row in data_set[phone_numbers].iterrows():
    mobile_counter = 0
    landline_counter = 0
    for col in phone_numbers:
        try:
            int(str(row[col])[:2])
            if int(str(row[col])[:2]) in mobile_perfixes.values.tolist():
                mobile_counter += 1
            else:
                landline_counter += 1
        except ValueError:
            continue
    moblie_count[mobile_counter] += 1
    landline_count[landline_counter] += 1
for i in range(len(moblie_count)):
    print('{}% of the profiles includes {} mobile numbers        '  
          '{}% of the profiles includes {} landline numbers'.format((moblie_count[i]/sum(moblie_count)*100), i, (landline_count[i]/sum(landline_count)*100), i))
