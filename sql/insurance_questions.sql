-- 1. What is the average charge for insurance?
SELECT
    ROUND(AVG(charges), 2) AS average_charge
FROM insurance_customers;

-- 2. Do smokers have higher average insurance charges than non-smokers?
SELECT
    smoker,
    COUNT(*) AS customer_count,
    ROUND(AVG(charges), 2) AS average_charge
FROM insurance_customers
GROUP BY smoker
ORDER BY average_charge DESC;

-- 3. How do the charges differ by BMI catgeory?
SELECT
    bmi_category,
    COUNT(*) AS customer_count,
    ROUND(AVG(charges), 2) AS average_charge
    FROM insurance_customers
    GROUP BY bmi_catgeory
    ORDER BY average_charge DESC;

-- 4. How do the charges differ by age group, does it cost less for younger people?
SELECT
    age_group,
    COUNT(*) AS customer_count,
    ROUND(AVG(charges), 2) AS average_charge
FROM insurance_customers
GROUP BY age_group
ORDER BY average_charge DESC;

-- 5. How do charges differ by region?

SELECT 
    region,
    COUNT(*) AS customer_count,
    ROUND(AVG(charges), 2) AS average_charge
FROM insurance_customers
GROUP BY region
ORDER BY average_charge DESC;

-- 6. Which group has the highest risk profile?

SELECT 
    smoker,
    bmi_category,
    age_group,
    COUNT(*) AS customer_count,
    ROUND(AVG(charges), 2) AS average_charge
FROM insurance_customers
GROUP BY smoker, bmi_category, age_group
HAVING customer_count >= 5
ORDER BY average_charge DESC;