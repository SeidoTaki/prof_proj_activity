select pr.name, sum(pod.orderqty * pod.unitprice)
from "purchasing".purchaseorderdetail as pod
inner join "production".product as pr
on pod.productid = pr.productid
group by pr.name
having sum(pod.orderqty * pod.unitprice) < 5000;