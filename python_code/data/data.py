from python_code.common.data_framer import data_framer

data = {
    'Order ID': [1, 2, 3],
    'Order Date': ['2023-01-10', '2023-02-15', '2023-02-28'],
    'Customer ID': ['C123', 'C456', 'C123'],
    'Region': ['North', 'South', 'North'],
    'Product Category': ['Smartphone', 'Office Chair', 'Headphones'],
    'Quantity': [2, 1, 3],
    'Unit Price': [500, 150, 50],
    'Total Sales': [1000, 150, 150],
}

df = data_framer(data)