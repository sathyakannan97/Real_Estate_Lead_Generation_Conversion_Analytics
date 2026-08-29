CREATE DATABASE real_estate;
USE real_estate;
CREATE TABLE leads (
    Lead_ID INT PRIMARY KEY,
    Lead_Date DATE,
    Lead_Source VARCHAR(50),
    Location VARCHAR(100),
    Property_Type VARCHAR(50),
    Budget DECIMAL(12,2),
    Call_Attempts INT,
    Call_Status VARCHAR(50),
    Followup_Status VARCHAR(50),
    Site_Visit VARCHAR(20),
    Lead_Status VARCHAR(50),
    Sales_Value DECIMAL(12,2)
);
SHOW TABLES;
DESCRIBE leads;

SELECT * FROM Real_Estate_Leads_Raw LIMIT 5;

SHOW TABLES;
SELECT COUNT(*) AS Total_Records
FROM Real_Estate_Leads_Raw;

SELECT COUNT(*) AS Total_Leads
FROM Real_Estate_Leads_Raw;

SELECT Lead_Source,
       COUNT(*) AS Total_Leads
FROM Real_Estate_Leads_Raw
GROUP BY Lead_Source;

SELECT Property_Type,
       COUNT(*) AS Total_Leads
FROM Real_Estate_Leads_Raw
GROUP BY Property_Type;

SELECT Lead_Source,
       SUM(Sales_Value) AS Total_Sales
FROM Real_Estate_Leads_Raw
GROUP BY Lead_Source;

SELECT COUNT(*) AS Converted_Leads
FROM Real_Estate_Leads_Raw
WHERE Lead_Status = 'Converted';

#STATISTICS QUERY
SELECT COUNT(*) AS Total_Leads
FROM Real_Estate_Leads_Raw;

SELECT COUNT(*) AS Converted_Leads
FROM Real_Estate_Leads_Raw
WHERE Lead_Status = 'Converted';

SELECT AVG(Budget) AS Average_Budget
FROM Real_Estate_Leads_Raw;

SELECT AVG(Sales_Value) AS Average_Sales_Value
FROM Real_Estate_Leads_Raw;

SELECT Lead_Source,
       COUNT(*) AS Total_Leads
FROM Real_Estate_Leads_Raw
GROUP BY Lead_Source
ORDER BY Total_Leads DESC;

SELECT COUNT(*) AS Site_Visits
FROM Real_Estate_Leads_Raw
WHERE Site_Visit = 'Yes';

SELECT
(
    COUNT(CASE WHEN Lead_Status = 'Converted' THEN 1 END)
    * 100.0
    / COUNT(*)
) AS Conversion_Rate
FROM Real_Estate_Leads_Raw;