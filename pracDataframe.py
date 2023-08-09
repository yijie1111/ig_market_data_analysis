import pandas as pd

# Read the CSV files into dataframes
financial_df = pd.read_csv('financial.csv')
country_stats_df = pd.read_csv('country_stats.csv')
exchange_df = pd.read_csv('exchange.csv')

# Print the dataframes
print("Financial DataFrame:")
print(financial_df)

print("\nCountry Stats DataFrame:")
print(country_stats_df)

print("\nExchange DataFrame:")
print(exchange_df)
