import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("movies.csv")

df.plot.scatter(x='Year', y='Audience Score %', c='Year', colormap='viridis', alpha=0.7)

plt.title('Movies Audience Score per Year')
plt.xlabel('Year')
plt.ylabel('Audience Score %')

#กำหนดให้แกน X แสดงเฉพาะเลขปีที่มีอยู่ในตารางเท่านั้น
plt.xticks(df['Year'].unique())

plt.show()