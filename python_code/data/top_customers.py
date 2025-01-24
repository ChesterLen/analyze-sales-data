from data import df

top_customers = df.groupby('Customer ID')['Total Sales'].sum().nlargest(5)

print("Top 5 Customers by Revenue:")
print(top_customers)