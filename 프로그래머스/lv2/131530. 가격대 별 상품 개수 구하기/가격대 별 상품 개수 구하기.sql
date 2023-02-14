SELECT floor(price / 10000) * 10000 as price_group,
count(*) as products

from product
group by PRICE_GROUP
order by PRICE_GROUP