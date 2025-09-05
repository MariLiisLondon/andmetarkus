-- Kuupäevadega seotud funktsioonid PostgreSQL-is

-- 1.1. Leia müügikogused kuude lõikes -- TO_CHAR funktsionaalsus

select to_char(sale_date,'YYYY-MM'), SUM(quantity) --to char teeb kuupäeva tekstiks
from salestable as s
group by to_char(sale_date,'YYYY-MM')
order by TO_CHAR (sale_date, 'YYYY-MM')asc;

--  1.2. HARJUTAMISEKS: Leia müügikogused aastate lõikes

select to_char(sale_date,'YYYY'), SUM(quantity) --to char teeb kuupäeva tekstiks
from salestable as s
group by to_char(sale_date,'YYYY')
order by TO_CHAR (sale_date, 'YYYY')asc;

-- 1.3. Kui palju on viimasest müügist möödas?

-- 1.3.1. I võimalus: age funktsioon, annab tekstilise tulemuse

select AGE(MAX(sale_date)), max(s.sale_date ) -- age arvutab kui palju on siis tänasest kpvast möödas
from salestable s;  

-- 1.3.2. II võimalus: current_date ja lahutustehe - annab päevade arvu numbrilise väärtusena


select current_date, max(sale_date), current_date - max(sale_date) as age_in_date --palju on möödas viimasest müügist
from salestable s;  


-- 1.4. HARJUTAMISEKS: Kui palju aega on esimesest müügist möödas?

select AGE(MIN(sale_date)), min(s.sale_date ), current_date - min(sale_date) as aga_p2evades--
from salestable s;

-- 1.5. Kui palju on tegelikud müügid, eelarve ja nende võrdlus kuude kaupa?

with b as (select TO_CHAR(budget_date, 'YYYY-MM') as yearmonth,
sum(budget_sum) as budget_sum
from budget_monthly_salesrep
group by TO_CHAR(budget_date, 'YYYY-MM')), --kui tahad teise alamtabeli veel luua, siis pead koma siia panema
-- Loome müügitabeli kuude kaupa
s as (select TO_CHAR(sale_date, 'YYYY-MM') as yearmonth,
sum(quantity*unit_price*(1-discount)) as sales_sum
from salestable as s
group by TO_CHAR(sale_date, 'YYYY-MM'))
-- Ühendame loodud tabelid
select b.yearmonth, b.budget_sum, s.sales_sum,
s.sales_sum-b.budget_sum as diff_from_budget
from b
left join s on b.yearmonth = s.yearmonth
order by b.yearmonth asc;



-- 1.6. HARJUTAMISEKS: Kui palju on tegelikud müügid, eelarve ja nende võrdlus kuude ja müügiesindaja kaupa?

with b as (select TO_CHAR(budget_date, 'YYYY-MM') as yearmonth,
sum(budget_sum) as budget_sum, sales_rep_id
from budget_monthly_salesrep
group by TO_CHAR(budget_date, 'YYYY-MM'), sales_rep_id), --kui tahad teise alamtabeli veel luua, siis pead koma siia panema
-- Loome müügitabeli kuude kaupa
s as (select TO_CHAR(sale_date, 'YYYY-MM') as yearmonth,
sum(quantity*unit_price*(1-discount)) as sales_sum, sales_rep_id
from salestable as s
group by TO_CHAR(sale_date, 'YYYY-MM'),sales_rep_id)
-- Ühendame loodud tabelid
select b.sales_rep_id,  b.yearmonth, b.budget_sum, s.sales_sum,
s.sales_sum-b.budget_sum as diff_from_budget
from b
left join s on b.yearmonth = s.yearmonth and b.sales_rep_id = s.sales_rep_id
order by b.yearmonth asc
;



 ----Harjutamiseks 
--Leia müügisummad toodete kaupa

select s.product_id, sum(s.sales_sum) 
from salestable s
group by s.product_id
order by s. product_id asc;


--Leia müügisummad klientide kaupa

select s.customer_id,  sum(s.sales_sum) 
from salestable s 
group by s.customer_id 
order by s.customer_id asc;


--Leia müügisummad müügiesindajate kaupa

select s.sales_rep_id ,  sum(s.sales_sum) 
from salestable s 
group by s.sales_rep_id  
order by s.sales_rep_id  asc;

--Leia müügisummad aastate kaupa

select to_char(sale_date,'YYYY'), SUM(s.sales_sum ) --to char teeb kuupäeva tekstiks
from salestable as s
group by to_char(sale_date,'YYYY')
order by TO_CHAR (sale_date, 'YYYY')asc;


--Lisa müükidele müügisumma kategooriad

select s.sales_sum,
 CASE 
	when s.sales_sum < 250 THEN 'Small Sale'
    WHEN s.sales_sum >= 250 and s.sales_sum  <= 500 then 'Medium Sale'
    ELSE 'Large Sale'
      END AS sales_category
from salestable as s
;

--Large Sale > 500
--Medium Sale <= 500 and >= 250
--Small Sale < 250


--Leia müükide arv ja müügisumma müügisumma kategooriate kaupa


with myygisummakategooriad as 
(SELECT s.quantity, s.sales_sum,
	 CASE 
		when s.sales_sum < 250 THEN 'Small Sale'
  		WHEN s.sales_sum >= 250 and s.sales_sum  <= 500 then 'Medium Sale'
   		ELSE 'Large Sale'
      END AS sales_category
from salestale as s)
select  sales_category, sum(quantity), sum(sales_sum)
from myygisummakategooriad 
group by sales_category 
;


SELECT table_schema, table_name
FROM information_schema.tables
WHERE table_name ILIKE '%salestable%';




