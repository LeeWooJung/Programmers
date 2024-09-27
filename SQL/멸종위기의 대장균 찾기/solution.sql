-- MySQL

WITH RECURSIVE gen AS (

    select id, parent_id, 1 as generation
    from ecoli_data
    where parent_id is null
    
    union all
    
    select ed.id, ed.parent_id, generation + 1
    from gen, ecoli_data as ed
    where gen.id = ed.parent_id
)

select count(id) as COUNT, generation as GENERATION
from gen
where id not in (
    select distinct parent_id
    from gen
    where parent_id is not null
)
group by generation
order by generation
;