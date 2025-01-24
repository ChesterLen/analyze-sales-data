from data import df

avg_orders = df['Customer ID'].value_counts().mean()

print(f"Average Orders Per Customer: {avg_orders:.2f}")