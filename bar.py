import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("movies.csv")
#drop null values
#new_df = df.dropna() 
df['Worldwide Gross'] = df['Worldwide Gross'].astype(str).str.replace('$', '', regex=False).str.replace(',', '', regex=False)
df['Worldwide Gross'] = pd.to_numeric(df['Worldwide Gross'])
df_sorted = df.sort_values(by="Worldwide Gross", ascending=False).head(30)

plt.figure(figsize=(10, 7))
plt.bar(df_sorted['Movie Title'], df_sorted['Worldwide Gross'], color='red', width=0.6)

#แก้ปัญหาตัวหนังสือทับกัน - หมุนชื่อหนัง 45 องศา
plt.xticks(rotation=45, ha='right')

#จัดระยะขอบให้อัตโนมัติป้องกันชื่อตกขอบ
plt.tight_layout()

# กำหนดขอบล่างให้เหลือที่ว่าง 30-40% ของความสูงกราฟ
plt.subplots_adjust(bottom=0.4)

plt.xlabel('Movie Title')
plt.ylabel('Worldwide Gross')
plt.title('Top 30 Highest Worldwide Grossing Movies')

plt.show()

print(df_sorted[['Movie Title', 'Worldwide Gross']]) #return table of movies.csv (sorted)
