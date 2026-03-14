import pandas as pd

data = {
    "Name": ['Ram', 'Shyam', 'Ghanshyam', 'Dhanshyam', 'Aditi', 'Jagdish', 'Raj', 'Simran'],
    "Age": [28,34,22,30,29,40,25,32],
    "Salary": [50000, 60000, 45000, 52000,49000,70000,48000,58000 ],
    "Performance Score": [85,90,78,92,88,95,80,89]
}

df = pd.DataFrame(data)

high_salary = df[df['Salary']>50000]
print('Employees with salary > 50000')
print(high_salary)

#filtering rows salary > 50k and age > 30

filtered = df[(df['Age']>30) & (df['Salary']>50000)]
print('Employee list Age >30 and Salary > 50000')
print(filtered)
