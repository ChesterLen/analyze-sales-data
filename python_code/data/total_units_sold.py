from data import df

total_units_sold = df['Quantity'].sum()

print(f'Total Units Sold: {total_units_sold}')