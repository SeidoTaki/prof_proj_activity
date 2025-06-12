-- 2) list of products
select pr.productid, pr.name, pr.listprice
from "production".product as pr
where pr.listprice > 200
order by pr.listprice asc;
