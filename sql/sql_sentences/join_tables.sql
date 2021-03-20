select name.id, name.name, profit.year, profit.profitability 
from funds.name name
left join funds.profitability profit
on name.id = profit.id;