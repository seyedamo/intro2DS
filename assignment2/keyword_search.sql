--create view vw_frequency as 
--SELECT * FROM frequency
--UNION
--SELECT 'q' as docid, 'washington' as term, 1 as count 
--UNION
--SELECT 'q' as docid, 'taxes' as term, 1 as count
--UNION 
--SELECT 'q' as docid, 'treasury' as term, 1 as count;

select max(score) from (
select b.docid, sum(b.count) as score 
from vw_frequency a, vw_frequency b
where a.docid = 'q' 
and b.docid <> 'q'
and a.term = b.term
group by b.docid
order by score desc) temp;
