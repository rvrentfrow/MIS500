"""
MIS-500 WEEK 1 CTA, OPTION 1
Enter sample code into PyCharm to ensure setup
is functioning properly, and file is loading to GitHub
"""
#PROGRAM START

import pandas as pd   #import analytical module package


data_frame = pd.DataFrame({
    'name':['matt','lisa','richard','john','Julia','jane','marlon'],
    'age':[23,78,22,19,45,33,20],
    'gender':['M','F','M','M','M','F','M'],
    'state':['DC','CO','DE','VA','MD','DE','NY'],
    'years_of_service':[10,0,2,0,2,1,5],
    'iq':[300,100,110,200,300,10,40]
})
#SUB BEGIN:  function extracts 25% of sample of data array
rows = data_frame.sample(frac=.25)

"""
if statement compares 25% of length of array
to 25% length of sample to ensure it is a valid sample;
the validation statement is TRUE whenever the difference 
between 25% of the array and the sample is less than or 
equal to zero.  If TRUE, prints total rows and sample rows.
If FALSE, prints that there is sampling error.  
"""

total_rows = len(data_frame)

if ((0.25*total_rows) - len(rows)) <= 0:
    print("TOTAL ROWS=",len(data_frame), "\nSAMPLE ROWS=",len(rows))
else:  print("***SAMPLING ERROR***")

print('\n25% SAMPLE:\n',rows,"\n")
#SUB END:  sample extraction

"""split categorical values in array by gender;
display statistical data (Sum, Mean, Count) and describe data
"""
#SUB BEGIN:  Group Mean IQ by Gender
groupby_gender=data_frame.groupby('gender')  #define gender as grouping

print("AVERAGE IQ BY GENDER:")
for gender,value in groupby_gender['iq']:  #loads the list of IQs into value for each gender type
    print(gender,value.mean())  #prints the mean IQ for each group (gender)
#SUB END: Group Mean IQ by Gender

#SUB BEGIN:  Sum of Ages
sum_of_age = data_frame['age'].sum()
print ('\nSUM OF AGES:', sum_of_age)
#SUB END:  Sum of Ages

#SUB BEGIN:  Average Age
mean_age = data_frame['age'].mean()
#SUB END:  Average Age

#SUB BEGIN:  Column Means
print('\nMEANS OF EACH COLUMN:')
print(data_frame.mean(axis=0))
#SUB END:  Column Means

#SUB BEGIN:  Describe Data
print("\nDESCRIBE IQ DATA:")
print(data_frame['iq'].describe())
#SUB END:  Describe Data

#PROGRAM END
