from data import df

revenue_by_region = df.groupby('Region')['Total Sales'].sum().sort_values(ascending=False)

print(revenue_by_region)