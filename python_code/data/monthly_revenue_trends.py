from data import df
import matplotlib.pyplot as plt

df['Monthly Revenue'] = df['Order Date'].dt.to_period('M')

monthly_revenue = df.groupby('Monthly Revenue')['Total Sales'].sum()

plt.figure(figsize=(10, 6))
monthly_revenue.plot(kind='line', marker='o')
plt.title('Monthly Revenue Trend')
plt.xlabel('Month')
plt.ylabel('Total Revenue')
plt.grid()
plt.show()