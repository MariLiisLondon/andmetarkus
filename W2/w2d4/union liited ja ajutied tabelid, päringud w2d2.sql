-- 11. ALAMPÄRINGUD - viide teisele päringule:
-- Millised töötajad on keskmiselt andnud allahindlust üle 7,5%?
--ajutise päringu loomine
select sales_rep_name -- vaatan, nende nimesid teisest tabelist
from salesreptable 
where sales_rep_id in ( --iniga kontrollin listi
	select sales_rep_id -- siin osas teed listi salesreppidest ja nende discount on suurem kui 0.75
	from salestable 
	group by sales_rep_id 
	having avg (discount) > 0.075);


-- 12. AJUTISED PÄRINGUTULEMUSED (Common Table Expressions - CTEs): : 
--Millised töötajad on keskmiselt andnud allahindlust üle 7,5% ja kui suur on keskmine antud allahindlus?
-- ajutise tabeli loomine
with salesrepdiscount as (
	select sales_rep_id, avg (discount ) as avg_discount
	from salestable 
	group by sales_rep_id
	having avg (discount ) > 0.075
)
select salesreptable.sales_rep_name,  salesrepdiscount.sales_rep_id, salesrepdiscount.avg_discount
from salesrepdiscount
left join salesreptable on salesrepdiscount.sales_rep_id = salesreptable.sales_rep_id; 


---
--Harjutamiseks: Tegelikud müügid vs eelarve müügiesindaja kaupa.

WITH esindaja_tegelik AS (
    SELECT sales_rep_id, round(SUM(quantity * unit_price*(1-discount)):: numeric,0) AS tegelikud_muugid
    FROM salestable
    GROUP BY sales_rep_id
)
SELECT e.sales_rep_id , budget_sum, e.tegelikud_muugid 
FROM budgettable b
full outer JOIN esindaja_tegelik e 
    ON e.sales_rep_id = b.sales_rep_id;


-- 13. TABELITE KOMBINEERIMINE
-- 13.1. Leia tabelite pealt unikaalsed väärtused: Leia kliendid, kellel oli müüke 2025. aastal või enne 2021. aastat
 -- UNION

select s.customer_id, s.product_id, sum(s.quantity ) 
from salestable s 
where s.sale_date >='2025-01-01'
group by customer_id, product_id  
union  -- näitab1x
select s.customer_id, s.product_id, sum(s.quantity )  
from salestable s 
where s.sale_date < '2021-12-31'
group by customer_id, product_id;



-- 13.2. Leia kõik väärtused mitmest tabelist: Leia kõik müügid 2025. aastal või enne 2021. aastat 
-- UNION ALL

select *
from salestable s 
where s.sale_date >='2025-01-01' 
union all --paneb korduma
select * 
from salestable s 
where s.sale_date < '2021-12-31';



