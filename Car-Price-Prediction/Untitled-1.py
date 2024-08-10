# %%
import pandas as pd
df = pd.read_csv("laptop_data.csv")

# %%
df.drop('Unnamed: 0', axis=1, inplace=True)

# %%
missing_values = df.isnull().sum()
print(missing_values)

# %%
X = df.drop('Price',axis=1)
Y = df['Price']

# %%
from sklearn.model_selection import train_test_split
X_train,X_test ,Y_train,y_test = train_test_split(X,Y,test_size=0.33,random_state =42)
X_train

# %%
df['ScreenResolution'].unique()

# %%
for col_name in df.columns:
    print(f'{col_name} --> {len(df[col_name].unique())}')


# %%
df['Memory'].unique()

# %%
df['Memory'] = df['Memory'].str.replace('Flash Storage', 'SSD')

# %%
df['Memory'].unique()

# %%
memory_order = [
    '500GB HDD',
    '1TB HDD',
    '2TB HDD',
    '1TB HDD + 1TB HDD',
    '508GB Hybrid',
    '1.0TB Hybrid',
    '8GB SSD',
    '32GB SSD',
    '64GB SSD',
    '128GB SSD',
    '180GB SSD',
    '240GB SSD',
    '256GB SSD',
    '512GB SSD',
      '1TB SSD',
    '256GB SSD +  500GB HDD',
    '128GB SSD +  1TB HDD',
    '128GB SSD +  2TB HDD',
    '256GB SSD +  1TB HDD',
    '512GB SSD +  1TB HDD',
    '1TB SSD +  1TB HDD',
    '512GB SSD +  2TB HDD'
    '256GB SSD +  256GB SSD',
    '512GB SSD +  256GB SSD',
]

# %%
df['Ram'].unique()

# %%
ram_order = ['2GB', '4GB', '6GB', '8GB', '12GB', '16GB', '24GB', '32GB','64GB']

# %%
df['Cpu'].unique()

# %%
cpu_order = [
    'Intel Celeron Dual Core N3350 1.1GHz',
    'Intel Celeron Dual Core N3060 1.6GHz',
    'Intel Atom x5-Z8300 1.44GHz',
    'Intel Atom x5-Z8350 1.44GHz',
    'Intel Atom Z8350 1.92GHz',
    'AMD E-Series E2-9000e 1.5GHz',
    'AMD E-Series 7110 1.8GHz',
    'AMD E-Series E2-6110 1.5GHz',
    'AMD A4-Series 7210 2.2GHz',
    'Intel Pentium Quad Core N3700 1.6GHz',
    'Intel Pentium Dual Core N4200 1.1GHz',
    'Intel Pentium Dual Core 4405U 2.1GHz',
    'Intel Core M M3-6Y30 0.9GHz',
    'Intel Core M M7-6Y75 1.2GHz',
    'Intel Core M m3-7Y30 2.2GHz',
    'Intel Core M m7-6Y75 1.2GHz',
    'Intel Core M 7Y30 1.0GHz',
    'Intel Core M 6Y54 1.1GHz',
    'Intel Core M 6Y75 1.2GHz',
    'Intel Core M 1.2GHz',
    'Intel Core M 1.1GHz',
    'Intel Celeron Quad Core N3160 1.6GHz',
    'Intel Celeron Quad Core N3450 1.1GHz',
    'Intel Core i3 6006U 2GHz',
    'Intel Core i3 6006U 2.2GHz',
    'Intel Core i3 6100U 2.3GHz',
    'Intel Core i3 6100U 2.1GHz',
    'Intel Core i3 7100U 2.4GHz',
    'Intel Core i3 7130U 2.7GHz',
    'AMD A6-Series 7310 2GHz',
    'AMD A6-Series 9220 2.5GHz',
    'AMD A6-Series 9220 2.9GHz',
    'AMD A10-Series 9620P 2.5GHz',
    'AMD A10-Series 9600P 2.4GHz',
    'AMD A12-Series 9720P 2.7GHz',
    'AMD A12-Series 9720P 3.6GHz',
    'AMD FX 8800P 2.1GHz',
    'AMD FX 9830P 3GHz',
    'AMD A8-Series 7410 2.2GHz',
    'Intel Core i5 1.3GHz',
    'Intel Core i5 1.6GHz',
    'Intel Core i5 6200U 2.3GHz',
    'Intel Core i5 6300HQ 2.3GHz',
    'Intel Core i5 6440HQ 2.6GHz',
    'Intel Core i5 7300HQ 2.5GHz',
    'Intel Core i5 7300U 2.6GHz',
    'Intel Core i5 7200U 2.5GHz',
    'Intel Core i5 7200U 2.7GHz',
    'Intel Core i5 7440HQ 2.8GHz',
    'Intel Core i5 7500U 2.7GHz',
    'Intel Core i5 6200U 2.3GHz',
    'Intel Core i5 7300U 2.6GHz',
    'Intel Core i5 7440HQ 2.8GHz',
    'Intel Core i5 7500U 2.7GHz',
    'Intel Core i5 7200U 2.50GHz',
    'Intel Core i5 7200U 2.70GHz',
    'Intel Core i7 7Y75 1.3GHz',
    'Intel Core i7 6500U 2.5GHz',
    'Intel Core i7 7500U 2.7GHz',
    'Intel Core i7 7500U 2.5GHz',
    'Intel Core i7 7700HQ 2.7GHz',
    'Intel Core i7 7700HQ 2.8GHz',
    'Intel Core i7 6700HQ 2.6GHz',
    'Intel Core i7 6920HQ 2.9GHz',
    'Intel Core i7 6820HK 2.7GHz',
    'Intel Core i7 6820HQ 2.7GHz',
    'Intel Core i7 6500U 2.50GHz',
    'Intel Core i7 7600U 2.8GHz',
    'Intel Core i7 7660U 2.5GHz',
    'Intel Core i7 7820HK 2.9GHz',
    'Intel Core i7 7820HQ 2.9GHz',
    'Intel Core i7 7560U 2.4GHz',
    'Intel Core i7 8650U 1.9GHz',
    'Intel Core i7 8550U 1.8GHz',
    'Intel Core i7 8650U 1.9GHz',
    'Intel Core i7 8550U 1.8GHz',
    'Intel Core i7 7560U 2.4GHz',
    'Intel Core i7 8650U 1.9GHz',
    'Intel Core i7 7700HQ 2.8GHz',
    'Intel Core i7 6920HQ 2.9GHz',
    'Intel Core i7 6600U 2.6GHz',
    'Intel Core i7 6700HQ 2.6GHz',
    'Intel Core i7 7600U 2.8GHz',
    'Intel Core i7 7600U 2.8GHz',
    'Intel Core i7 6920HQ 2.9GHz',
    'Intel Core i7 6600U 2.6GHz',
    'Intel Core i7 7660U 2.5GHz',
    'Intel Core i7 6560U 2.2GHz',
    'Intel Core i7 8650U 1.9GHz',
    'Intel Core i7 8650U 1.9GHz',
    'Intel Core i7 8550U 1.8GHz',
    'Intel Core i7 8550U 1.8GHz',
    'Intel Core i7 6560U 2.2GHz',
    'Intel Core i7 8650U 1.9GHz',
    'Intel Core i7 8650U 1.9GHz',
    'Intel Core i7 8550U 1.8GHz',
    'Intel Core i7 8550U 1.8GHz',
    'Intel Core i7 7500U 2.7GHz',
    'Intel Core i7 7500U 2.7GHz',
    'Intel Core i7 7500U 2.7GHz',
    'Intel Core i7 7500U 2.7GHz',
    'Intel Xeon E3-1535M v6 3.1GHz',
    'Intel Xeon E3-1505M V6 3GHz',
    'Intel Xeon E3-1535M v5 2.9GHz',
    'AMD Ryzen 1600 3.2GHz',
    'AMD Ryzen 1700 3GHz',
    'Samsung Cortex A72&A53 2.0GHz',
    'Intel Core i7 6920HQ 2.9GHz',
]

# %%
df["Gpu"].unique()

# %%
df.columns

# %%
from sklearn.preprocessing import OrdinalEncoder

ordinal_categories = {"Ram":ram_order,"Memory":memory_order , "Cpu":cpu_order}

for category , order in ordinal_categories.items():
    # print(category)
    encoder = OrdinalEncoder(categories=[order])
    df[category] = encoder.fit_transform(df[[category]])




# %%


# %%

from sklearn.pipeline import Pipeline



# ordinal_features = ['Ram' , '']
# numerical_transformer = Pipeline(steps=[
#     ('ordinal', OrdinalEncoder(strategy='mean')),  
# ])

# categorical_features = ['city']
# categorical_transformer = Pipeline(steps=[
#     ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),  # Fill missing values
#     ('onehot', OneHotEncoder(handle_unknown='ignore'))  # One-hot encode categorical features
# ])


# %%


# %%


# %%


# %%
from sklearn.compose import ColumnTransformer

# %%



