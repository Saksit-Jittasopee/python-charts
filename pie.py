import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("movies.csv")

genre_data = df.groupby('Genre')['Rotten Tomatoes %'].mean()

plt.figure(figsize=(7, 7))
plt.pie(genre_data, labels=genre_data.index, autopct='%1.1f%%', startangle=90)

plt.title('Rotten Tomatoes Score per Genre in 100%')
plt.ylabel('')
plt.show()