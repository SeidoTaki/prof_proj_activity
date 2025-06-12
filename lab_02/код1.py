import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import plotly.express as px

# Загрузка данных из Excel (только нужные столбцы)
cols_to_load = ['Ship Mode', 'Segment', 'Region', 'Category', 'Sub-Category', 'Quantity', 'Discount']

df = pd.read_excel("C:\\Users\\PC\\Desktop\ОСН 2 лабы.xls", usecols=cols_to_load)

# Преобразование Discount в числовой формат (заменяем запятые на точки)
df['Discount'] = (
    df['Discount']
    .astype(str)
    .str.replace(',', '.')
    .replace('nan', '0')  # обработка пустых значений
    .astype(float)
)

# Проверка данных
print(df.head())
print("\nИнформация о типах данных:")
print(df.info())

ship_mode_counts = df['Ship Mode'].value_counts()
plt.figure(figsize=(10, 6))
sns.barplot(x=ship_mode_counts.index, y=ship_mode_counts.values)
plt.title('Распределение заказов по типам доставки')
plt.ylabel('Количество заказов')
plt.xlabel('Тип доставки')
plt.xticks(rotation=45)
plt.show()

segment_counts = df['Segment'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(segment_counts, labels=segment_counts.index, autopct='%1.1f%%')
plt.title('Распределение заказов по сегментам клиентов')
plt.show()



plt.figure(figsize=(8, 6))
sns.heatmap(df[['Quantity', 'Discount']].corr(), annot=True, cmap='coolwarm')
plt.title('Корреляция между Quantity и Discount')
plt.show()


plt.figure(figsize=(12, 6))
sns.barplot(x='Category', y='Quantity', data=df, estimator=sum)
plt.title('Общее количество товаров по категориям')
plt.ylabel('Общее количество')
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(x='Category', y='Discount', data=df)
plt.title('Распределение скидок по категориям')
plt.ylabel('Скидка')
plt.xticks(rotation=45)
plt.show()

top_subcats = df['Sub-Category'].value_counts().head(10)
plt.figure(figsize=(12, 6))
sns.barplot(x=top_subcats.index, y=top_subcats.values)
plt.title('Топ 10 подкатегорий по количеству заказов')
plt.ylabel('Количество заказов')
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(10, 6))
sns.barplot(x='Region', y='Discount', data=df, estimator=np.mean)
plt.title('Средний Discount по регионам')
plt.ylabel('Средний Discount')
plt.show()

fig = px.pie(df, names='Category', title='Распределение заказов по категориям')
fig.show()

fig = px.bar(df.groupby('Sub-Category')['Quantity'].sum().reset_index(), 
             x='Sub-Category', y='Quantity',
             title='Общее количество товаров по подкатегориям')
fig.show()


plt.figure(figsize=(10, 6))
sns.histplot(df['Quantity'], bins=20, kde=True)
plt.title('Распределение количества товаров в заказах')
plt.xlabel('Количество товаров')
plt.show()