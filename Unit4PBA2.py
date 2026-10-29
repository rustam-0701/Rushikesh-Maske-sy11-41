import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("employee.csv")

# Display employee details
print(df[['Name', 'Department', 'Salary']])

# Average salary by department
avg = df.groupby('Department')['Salary'].mean()
print(avg)

# Bar chart
avg.plot(kind='bar')
plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.show()