import pandas as pd

data = {
    "Name": ['Ram', 'Shyam', 'Ghanshyam'],
    "Age": [10,20,30],
    "City": ['Nagpur', 'Mumbai', 'Delhi']
}
df = pd.DataFrame(data)

print("Displaiyng the info of dataset")

print(df.info())