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