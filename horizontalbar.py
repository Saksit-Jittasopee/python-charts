import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("movies.csv")

df['Rotten Tomatoes %'] = pd.to_numeric(df['Rotten Tomatoes %'])
df_sorted = df.sort_values(by="Rotten Tomatoes %", ascending=False).head(10).drop_duplicates()
plt.barh(y=df_sorted['Genre'], width=df_sorted['Rotten Tomatoes %'])

plt.title('Highest Rotten Tomatoes Score in Each Genre')
plt.xlabel('Rotten Tomatoes %')
plt.ylabel('Genre')

plt.show()