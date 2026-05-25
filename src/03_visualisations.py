import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path

# Load the cleaned data from the CSV file
df = pd.read_csv(Path("data/cleaned_insurance.csv"))

Path("visuals").mkdir(exist_ok=True)

#Chart 1: distribution of insurance charges
plt.figure(figsize=(8, 5))
sns.histplot(df["charges"], bins=30, kde=True)
plt.title("Distribution of Insurance Charges")
plt.xlabel("Insurance Charges")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.savefig("visuals/charges_distribution.png")
plt.close()

#Chart 2: charges by smoking status
plt.figure(figsize=(7, 5))
sns.boxplot(x="smoker", y="charges", data=df)
plt.title("Insurance Charges by Smoking Status")
plt.xlabel("Smoker")
plt.ylabel("Insurance Charges")
plt.tight_layout()
plt.savefig("visuals/charges_by_smoking_status.png")
plt.close()

#Chart 3: charges by BMI category
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="bmi", y="charges", hue="smoker")
plt.title("Insurance Charges by BMI and Smoking Status")
plt.xlabel("BMI")
plt.ylabel("Insurance Charges")
plt.legend(title="Smoker")
plt.tight_layout()
plt.savefig("visuals/charges_by_bmi_and_smoking_status.png")
plt.close()

print("Visualizations saved successfully in the visuals directory.")