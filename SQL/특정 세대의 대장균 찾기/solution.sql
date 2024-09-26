select c.ID
from (
    select parent.ID
    from (
        select ID
        from ECOLI_DATA
        where PARENT_ID is NULL
    ) as pparent, ECOLI_DATA as parent
    where pparent.ID = parent.PARENT_ID
) as p, ECOLI_DATA as c
where c.PARENT_ID = p.ID
order by c.ID;