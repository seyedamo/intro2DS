select value from (
select a.docid, b.docid, sum(a.count * b.count) as value
from frequency a, frequency b
where a.term = b.term
and a.docid = '10080_txt_crude' and b.docid = '17035_txt_earn'
group by a.docid, b.docid) temp
;