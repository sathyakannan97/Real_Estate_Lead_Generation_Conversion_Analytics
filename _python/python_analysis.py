import pandas as pd

df = pd.read_excel("data/Real_Estate_Leads_Raw.xlsx")

print("Rows and Columns:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nFirst 5 Records:")
print(df.head())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nData Types:")
print(df.dtypes)

# Data Cleaning

print("\nBefore Cleaning:")
print(df.isnull().sum())

# Replace missing Sales_Value with 0
df["Sales_Value"] = df["Sales_Value"].fillna(0)

print("\nAfter Cleaning:")
print(df.isnull().sum())

# KPI Analysis

total_leads = len(df)
converted_leads = len(df[df["Lead_Status"] == "Converted"])
total_sales = df["Sales_Value"].sum()

print("\nKPI RESULTS")
print("Total Leads:", total_leads)
print("Converted Leads:", converted_leads)
print("Total Sales:", total_sales)

import matplotlib.pyplot as plt
import seaborn as sns

# Leads by Source

plt.figure(figsize=(8,5))
sns.countplot(data=df, x="Lead_Source")

plt.title("Leads by Source")
plt.xlabel("Lead Source")
plt.ylabel("Number of Leads")

plt.savefig("charts/leads_by_source.png")
plt.show()

# Chart 2 - Lead Status Distribution

plt.figure(figsize=(8,5))

sns.countplot(data=df, x="Lead_Status")

plt.title("Lead Status Distribution")
plt.xlabel("Lead Status")
plt.ylabel("Number of Leads")

plt.savefig("charts/lead_status_distribution.png")

plt.show()

# Chart 3 - Leads by Property Type

plt.figure(figsize=(8,5))

sns.countplot(data=df, x="Property_Type")

plt.title("Leads by Property Type")
plt.xlabel("Property Type")
plt.ylabel("Number of Leads")

plt.savefig("charts/leads_by_property_type.png")

plt.show()

# Chart 4 - Monthly Lead Trend

df["Month"] = df["Lead_Date"].dt.strftime("%b")

monthly_leads = df.groupby("Month").size().reset_index(name="Leads")

plt.figure(figsize=(10,5))

sns.lineplot(data=monthly_leads, x="Month", y="Leads", marker="o")

plt.title("Monthly Lead Trend")
plt.xlabel("Month")
plt.ylabel("Number of Leads")

plt.savefig("charts/monthly_lead_trend.png")

plt.show()

# Chart 5 - Site Visit Analysis

plt.figure(figsize=(8,5))

sns.countplot(data=df, x="Site_Visit")

plt.title("Site Visit Analysis")
plt.xlabel("Site Visit")
plt.ylabel("Number of Leads")

plt.savefig("charts/site_visit_analysis.png")

plt.show()

# Chart 6 - Sales by Lead Source

sales_by_source = df.groupby("Lead_Source")["Sales_Value"].sum().reset_index()

plt.figure(figsize=(8,5))

sns.barplot(data=sales_by_source,
            x="Lead_Source",
            y="Sales_Value")

plt.title("Sales by Lead Source")
plt.xlabel("Lead Source")
plt.ylabel("Total Sales Value")

plt.savefig("charts/sales_by_source.png")

plt.show()

# Chart 7 - Conversion Rate by Source

converted = df[df["Lead_Status"] == "Converted"]

conversion_rate = (
    converted.groupby("Lead_Source").size()
    / df.groupby("Lead_Source").size()
    * 100
).reset_index(name="Conversion_Rate")

plt.figure(figsize=(8,5))

sns.barplot(data=conversion_rate,
            x="Lead_Source",
            y="Conversion_Rate")

plt.title("Conversion Rate by Source")
plt.xlabel("Lead Source")
plt.ylabel("Conversion Rate (%)")

plt.savefig("charts/conversion_rate_by_source.png")

plt.show()

# Export cleaned dataset
df.to_csv("cleaned_real_estate.csv", index=False)

print("Cleaned dataset exported successfully!")