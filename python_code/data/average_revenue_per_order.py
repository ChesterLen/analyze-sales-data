from data import df

avg_revenue = df['Total Sales'].mean()

print(f"Average Revenue Per Order: ${avg_revenue:.2f}")