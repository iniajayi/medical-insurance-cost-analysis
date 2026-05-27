# Medical Insurance Cost Analysis and Prediction

## Live Dashboard

https://medical-insurance-cost-analysis.streamlit.app

This project analyses medical insurance costs using a Kaggle dataset containing customer demographic and health-related information.

The aim is to understand which factors are associated with higher insurance charges and to build a simple regression model that predicts estimated insurance costs. 

I wanted to try implementing a few new things I learnt so I hope you like it 💕

## Dataset

The dataset contains the following columns:

- Age
- Sex
- BMI
- Children
- Smoker
- Region
- Charges

The target variable is `charges`, which represents medical insurance cost for each individual.

## Machine Learning Model

A Linear Regression model was trained using scikit-learn to predict medical insurance charges.

The model used features such as:

- age
- sex
- BMI
- number of children
- smoking status
- region
- BMI category
- age group

The model was evaluated using a train-test split.

### Evaluation Metrics

- **Mean Absolute Error:** £4,283.36
- **R² Score:** 0.782

The Linear Regression model demonstrated reasonably strong predictive performance for a baseline regression model. The R² score indicates that the model explained approximately 78% of the variation in insurance charges.

The Mean Absolute Error shows that predictions were typically within a few thousand pounds of the actual insurance cost. Variables such as smoking status, BMI and age appeared to have a strong relationship with insurance charges.

# In terms of the tools that I used they are as follows:

- Python
- pandas
- NumPy
- SQL / SQLite
- Matplotlib
- Seaborn
- Plotly
- Streamlit
- scikit-learn
- Git and GitHub

# I based my visualisations around the following business questions:

1. What is the average insurance charge?
2. Do smokers have higher insurance charges?
3. How do insurance charges differ by BMI category?
4. How do charges differ by age group?
5. How do charges differ by region?
6. Which customer groups appear to have the highest cost profile?

## And last but not least, here's my project structure

dashboard/
data/
models/
sql/
src/
visuals/
.gitignore
README.md
requirements.txt


