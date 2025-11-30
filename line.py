import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("movies.csv")

genre_data = df.groupby('Year')['Profitability'].mean()

plt.plot(genre_data.index, genre_data, color='green', linestyle='--', marker='o', label='Profitability')

plt.xticks(df['Year'].unique())

plt.xlabel("Year")
plt.ylabel("Profitability")
plt.title("Movies Profitability per Year")
plt.legend()
plt.show()