CREATE DATABASE IF NOT EXISTS analytic;
USE analytic;

CREATE TABLE IF NOT EXISTS analytic.fact_merchant_kpi (
  date DATE,
  id_merchant VARCHAR(50),
  tpv FLOAT,
  total_transactions FLOAT
);

CREATE TABLE IF NOT EXISTS analytic.fact_customer_kpi (
  date DATE,
  id_customer VARCHAR(50),
  tpv FLOAT,
  total_transactions FLOAT
);

CREATE TABLE IF NOT EXISTS analytic.dim_merchant_category (
  id_merchant VARCHAR(50),
  category VARCHAR(50)
);

INSERT INTO analytic.fact_merchant_kpi 
	SELECT STR_TO_DATE(CONCAT(day, ',', month, ',', year), '%d,%m,%Y') AS 'date', 
	merchant AS 'id_merchant', 
	ROUND(SUM(amount),2) AS 'tpv', 
    COUNT(id) AS 'total_transactions' 
    FROM db.transactions 
	GROUP BY CONCAT(day, '/', month, '/', year), merchant;
    
INSERT INTO analytic.fact_customer_kpi 
	SELECT STR_TO_DATE(CONCAT(day, ',', month, ',', year), '%d,%m,%Y') AS 'date', 
	customer AS 'id_customer', 
	ROUND(SUM(amount),2) AS 'tpv', 
    COUNT(id) AS 'total_transactions' 
    FROM db.transactions  
	GROUP BY CONCAT(day, '/', month, '/', year), customer;
    
INSERT INTO analytic.dim_merchant_category SELECT merchant AS 'id_merchant', category FROM db.transactions  GROUP BY merchant; 
    
 