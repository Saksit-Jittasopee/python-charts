import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("movies.csv")

plt.hist(df['Audience Score %'], bins=30, color='orange', edgecolor='black')

plt.xlabel("Audience Score %")
plt.ylabel("Frequency of Movies")
plt.title("Histogram of Movies Audience Score")

plt.show()