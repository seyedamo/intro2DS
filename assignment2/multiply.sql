select value from (
select A.row_num, B.col_num, sum(A.value * B.value) as value
from A,B
where A.col_num = B.row_num
group by 1,2
) temp
where row_num = 2 and col_num = 3;
