select name.id, name.name, profit.year, profit.profitability_max
from funds.name name
inner join
(
  select profit_normal.id, profit_normal.year, profit_max.profitability_max
  from funds.profitability profit_normal
  inner join
  (
    select id, max(profitability) profitability_max
    from funds.profitability
    group by id
  ) profit_max
  on profit_normal.id = profit_max.id
  and profit_normal.profitability = profit_max.profitability_max
) profit
on name.id = profit.id;