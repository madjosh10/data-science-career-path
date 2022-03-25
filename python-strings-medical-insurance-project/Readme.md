# Python String: Medical Insurance Project

You are a doctor who needs to clean up medical patient records, which are currently stored in one large string.

In this project, you will use your new knowledge of Python strings to obtain and clean up medical data so that it is easier to read and analyze.

### Task 1
First, take a look at the code in `script.py`.

The string `medical_data` stores the medical records for ten individuals. Each record is separated by a `;` and contains the name, age, BMI (body mass index), and insurance cost for an individual, in that order.

Print `medical_data` to see the output in the terminal

### Task 2
We want the insurance costs to be represented in US dollars.

Replace all instances of `#` in `medical_data` with `$`. Store the result in a variable called `updated_medical_data`.

Print `updated_medical_data`.

### Task 3
We want to calculate the number of medical records in our data.

Create a variable called `num_records` and initialize it at 0.

### Task 4

Next, write a `for` loop to iterate through the `updated_medical_data` string. Inside of the loop, add `1` to `num_records` when the current character is equal to `$`.

### Task 5
Outside of the loop, print `num_records` with the following message:
```
There are {num_records} medical records in the data.
```

## Splitting Strings

### Task 6
The medical data in its current form is difficult to analyze. An essential job for a data scientist is to clean up data so that it’s easy to work with.

Let’s start off by splitting the `updated_medical_data` string into a list of each medical record. Remember that each medical record is separated by a `;` in the string.

Store the result in a variable called `medical_data_split` and print this variable.

### Task 7
Our data is now stored in a list, but it is still hard to read. Let's split each medical record into its own list. 
First, define an empty list called `medical_records`

### Task 8
Next, iterate through `medical_data_split` and for each record, split the string after each comma (`,`) and append the split string to `medical_records`.

Print `medical_records` after the loop.

## Cleaning Data
### Task 9
Our data is now slightly more readable. Hoever, it is not properly formatted - it contains unnecassary whitespace.
To fix this, let's start by creating an empty list called `medical_records_clean`.

### Task 10
Next, use a `for` loop to iterate through `medical_records`.

Inside of the loop, create an empty list called `record_clean`. We’ll use this list to store a formatted version of each medical record.

### Task 11
After the `record_clean` variable, create a nested `for` loop that goes through each `record`:
```
for item in record:
```
Inside of this loop, append `item.strip()` to `record_clean` to remove any whitespace from the string.

### Task 12
Finally, we need to add each cleaned up record to `medical_records_clean`.

Outside of the nested `for` loop, append `record_clean` to `medical_records_clean`.

### Task 13
Print `medical_records_clean` outside of the `for` loops to see the output.

You should see output that is formatted and much easier to read.

## Analyzing Data 
### Task 14
Our data is now clean and ready for analysis.
For example, to print out the names of each of the ten individuals, we can use the following loop:
```
for record in medical_records_clean:
    print(record[0])
```


### Task 15
You want all of the names in the medical records to be in uppercase characters.

In the `for` loop, update `records[0]` before the `print` statement so that all of the characters are uppercase.

### Task 16
Let’s store each name, age, BMI, and insurance cost in separate lists.

To start, create four empty lists:

- `names`
- `ages`
- `bmis`
- `insurance_costs`

### Task 17
Next, iterate through `medical_records_clean` and for each record:

- Append the name to `names`.
- Append the age to `ages`.
- Append the BMI to `bmis`.
- Append the insurance cost to `insurance_costs`.

### Task 18
Print `names`, `ages`, `bmis`, and `insurance_costs` outside of the loop.

Make sure the output is what you expect.

### Task 19
Now that all of our data is in separate lists, we can easily perform analysis on that data. Let’s calculate the average BMI in our dataset.

First, create a variable called `total_bmi` and set it equal to 0.

### Task 20
Next, use a `for` loop to iterate through `bmis` and add each `bmi` to `total_bmi`.

Remember to convert `bmi` to a float.

### Task 21
After the loop, create a variable called `average_bmi` that stores the `total_bmi` divided by the length of the `bmis` list.

Print out `average_bmi` with the following message:
```
Average BMI: {average_bmi}
```
