select od.salesorderid, pr.name, pr.safetystocklevel, od.orderqty, od.unitprice
from "sales".salesorderdetail as od
inner join "production".product as pr
on od.productid = pr.productid
where od.orderqty > 10