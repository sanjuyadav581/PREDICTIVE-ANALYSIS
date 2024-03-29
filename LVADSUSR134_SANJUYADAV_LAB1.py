# -*- coding: utf-8 -*-
"""SANJU_YADAV_LAB2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19c-ZW0mzGvjejj0pYvvN8SgoXTpuBf_e
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

booking_data = pd.read_csv('/content/booking.csv')
booking_data.head()

missing_values_booking = booking_data.isnull().sum()
missing_values_booking

duplicates_booking = booking_data.duplicated().sum()

duplicates_booking

import seaborn as sns
import matplotlib.pyplot as plt
fig, axs = plt.subplots(4, figsize=(5, 10))

sns.boxplot(booking_data['number of adults'], ax=axs[0]).set_title('Number of Adults Distribution')
sns.boxplot(booking_data['number of children'], ax=axs[1]).set_title('Number of Children Distribution')
sns.boxplot(booking_data['lead time'], ax=axs[2]).set_title('Lead Time Distribution')
sns.boxplot(booking_data['average price'], ax=axs[3]).set_title('Average Price Distribution')

plt.tight_layout()
plt.show()

# encodding
booking_data_encoded = pd.get_dummies(booking_data,
                        columns=['type of meal', 'room type', 'market segment type', 'booking status'], drop_first=True)
booking_data_encoded.drop(['Booking_ID', 'date of reservation'], axis=1, inplace=True)
booking_data_encoded

# Dividing the data
X_booking = booking_data_encoded.drop('booking status_Not_Canceled', axis=1)
y_booking = booking_data_encoded['booking status_Not_Canceled']
X_train_booking, X_test_booking, y_train_booking, y_test_booking = train_test_split(X_booking, y_booking, test_size=0.2, random_state=42)

X_booking.shape

y_booking.shape

model_booking = LogisticRegression(max_iter=10000)
model_booking.fit(X_train_booking, y_train_booking)

y_pred_booking = model_booking.predict(X_test_booking)

# Model Evaluation
accuracy = accuracy_score(y_test_booking, y_pred_booking)
precision = precision_score(y_test_booking, y_pred_booking)
recall = recall_score(y_test_booking, y_pred_booking)
f1 = f1_score(y_test_booking, y_pred_booking)
conf_matrix = confusion_matrix(y_test_booking, y_pred_booking)

print(f'Accuracy: {accuracy}\nPrecision: {precision}\nRecall: {recall}\nF1-Score: {f1}\nConfusion Matrix: \n{conf_matrix}')

#EDA
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
print("Summary statistics:")
print(data.describe())
plt.figure(figsize=(8, 6))
sns.countplot(x='booking status', data=data)
plt.title('Distribution of Booking Status')
plt.xlabel('Booking Status')
plt.ylabel('Count')
plt.show()
plt.figure(figsize=(10, 8))
sns.heatmap(data.corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Pairwise Correlation Heatmap')
plt.show()
numerical_features = ['number of adults', 'number of children', 'number of weekend nights', 'number of week nights', 'lead time', 'average price']
plt.figure(figsize=(12, 8))
for i, feature in enumerate(numerical_features, 1):
    plt.subplot(2, 3, i)
    sns.histplot(data[feature], kde=True)
    plt.title(f'Distribution of {feature}')
    plt.xlabel(feature)
    plt.ylabel('Frequency')
plt.tight_layout()
plt.show()
plt.figure(figsize=(12, 8))
for i, feature in enumerate(numerical_features, 1):
    plt.subplot(2, 3, i)
    sns.boxplot(x='booking status', y=feature, data=data)
    plt.title(f'Boxplot of {feature} by Booking Status')
    plt.xlabel('Booking Status')
    plt.ylabel(feature)
plt.tight_layout()
plt.show()
categorical_features = ['type of meal', 'room type', 'market segment type']
plt.figure(figsize=(12, 8))
for i, feature in enumerate(categorical_features, 1):
    plt.subplot(2, 2, i)
    sns.countplot(x=feature, data=data, hue='booking status')
    plt.title(f'Distribution of {feature} by booking Status')
    plt.xlabel(feature)
    plt.ylabel('Count')
plt.tight_layout()
plt.show()