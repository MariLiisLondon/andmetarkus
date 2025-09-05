-- 10. TABELITE ÜHENDAMINE

-- 10.1. Kõik eelarveread eelarve tabelist ja nendega seotud müügiesindaja nimi müügiesindajate tabelist.

select *   -- AS iga saad, ntx täpsutada tulba pealkirja, kui mingit tulba pealkirja on 2 tk ntc nagu sales_rep_id
from budgettable 
left join salesreptable 
	on budgettable.sales_rep_id = salesreptable.sales_rep_id; 


-- 10.3. Kõik müügiesindajad müügiesindajate tabelist ja nendega seotud eelarveread eelarve tabelist.


select *      --NB! read, mitte veerud
from budgettable b 
right join salesreptable s 
on s.sales_rep_id =b.sales_rep_id; 


-- 10.4. Näita ainult ridu, millel on müügiesindaja nii eelarve tabelis kui ka väärtus müügiesindajate tabelis.

select *
from budgettable b 
inner join salesreptable s 
on s.sales_rep_id = b.sales_rep_id; 


-- 10.5. Näita kõiki ridu eelarve tabelist ja kõiki ridu müügiesindaja tabelist.

select *  
from budgettable b 
full outer join salesreptable s 
on s.sales_rep_id = b.sales_rep_id; 

-- 10.6. Näita ridu eelarve tabelist, millele pole müügiesindaja tabelis müügiesindajat kirjeldatud.

select * -- s.sales_rep_id, b.sales_rep_id, b.budget_sum  
from budgettable b 
left join salesreptable s 
on s.sales_rep_id = b.sales_rep_id 
where s.sales_rep_id is null;

-- 10.7. Näita ridu müügiesindaja tabelist, millele pole kirjeldatud ridu eelarve tabelis.

select *  
from salesreptable s
left join budgettable b 
on s.sales_rep_id = b.sales_rep_id 
where b.sales_rep_id  is null; -- kui pole kirjeldatud ridu, siis vaatame key kolumi järgi


-- 10.8. Näita müügiesindajaid, kellel on puudu eelarve või müügiesindaja tabelist rida.!!!!

select *  
from salesreptable s 
full outer join budgettable b 
on s.sales_rep_id = b.sales_rep_id 
where s.sales_rep_id is null or s.sales_rep_name is null;  


-- 10.9. Näita ridu müügitabelist, millel on olemas müügiesindaja info eelarve ja müügiesindaja tabelis.
 select s.*
 from salestable s 
 join salesreptable s2 
 on s.sales_rep_id =s2.sales_rep_id 
 join budgettable b 
 on s.sales_rep_id = b.sales_rep_id;  


