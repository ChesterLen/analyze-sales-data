from data import df

category_performance = df.groupby('Product Category').agg({
    'Total Sales': 'sum',
    'Quantity': 'sum',
}).sort_values('Total Sales', ascending=False)

print("Top-Performing Product Categories:")
print(category_performance)