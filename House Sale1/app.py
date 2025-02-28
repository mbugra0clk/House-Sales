import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

data = '/content/drive/MyDrive/Colab Notebooks/house_sales/house_sales.csv'
df = pd.read_csv(data)
df.head()

print(df.columns)


# Eksik veri kontrolü
missing_values = df.isnull().sum()
missing_values = missing_values[missing_values > 0]  # Sadece eksik değer içeren sütunları göster

missing_values


fig, axes = plt.subplots(2, 2, figsize=(12, 10))

sns.scatterplot(x=df["SqFtTotLiving"], y=df["SalePrice"], alpha=0.5, ax=axes[0, 0])
axes[0, 0].set_title("SqFtTotLiving vs SalePrice")

sns.boxplot(x=df["BldgGrade"], y=df["SalePrice"], ax=axes[0, 1])
axes[0, 1].set_title("BldgGrade vs SalePrice")

sns.scatterplot(x=df["LandVal"], y=df["SalePrice"], alpha=0.5, ax=axes[1, 0])
axes[1, 0].set_title("LandVal vs SalePrice")

sns.boxplot(x=df["Bathrooms"], y=df["SalePrice"], ax=axes[1, 1])
axes[1, 1].set_title("Bathrooms vs SalePrice")

plt.tight_layout()
plt.show()