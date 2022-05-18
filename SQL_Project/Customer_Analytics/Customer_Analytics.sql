SELECT * FROM orders_1 limit 5;
SELECT * FROM orders_2 limit 5;
SELECT * FROM customer limit 5;

#Total Penjualan dan Revenue pada Quarter-1 (Jan, Feb, Mar) dan Quarter-2 (Apr,Mei,Jun)
SELECT quarter, sum(quantity) as total_penjualan, sum(quantity*priceEach) as revenue FROM (SELECT orderNumber, status, quantity, priceEach, '1' as quarter FROM orders_1 UNION SELECT orderNumber, status, quantity, priceEach, '2' as quarter FROM orders_2) AS tabel_a WHERE status = "Shipped" GROUP BY quarter

#Jumlah kustomer pada Quarter-1 (Jan, Feb, Mar) dan Quarter-2 (Apr,Mei,Jun)
SELECT quarter, count(distinct customerID) as total_customers FROM (SELECT customerID, createDate, QUARTER(createDate) as quarter FROM customer WHERE createDate BETWEEN "2004-01-1" AND "2004-06-30") AS tabel_b GROUP BY quarter

#Jumlah kustmoer yang sudah melakukan transaksi pada Quarter-1 (Jan, Feb, Mar) dan Quarter-2 (Apr,Mei,Jun)
SELECT quarter, COUNT(DISTINCT customerID) as total_customers FROM (SELECT customerID, createDate, QUARTER(createDate) as quarter FROM customer WHERE createDate BETWEEN '2004-01-01' AND '2004-06-30') as tabel_b WHERE customerID IN(SELECT DISTINCT customerID FROM orders_1 UNION SELECT DISTINCT customerID FROM orders_2) GROUP BY quarter

#Kategori produk yang paling banyak transaksinya
SELECT * FROM (SELECT categoryid, COUNT(DISTINCT orderNumber) as total_order, sum(quantity) as total_penjualan FROM (SELECT productCode, orderNumber, quantity, status, LEFT(productCode,3) as categoryid FROM orders_2 WHERE status = "Shipped") AS tabel_c GROUP BY categoryid) AS a ORDER BY total_order DESC;

#Menghitung retensi
SELECT COUNT(DISTINCT customerID) as total_customers FROM orders_1;
#output = 25
SELECT 1 as quarter, count(DISTINCT customerID)*100/25 as Q2 FROM orders_1 WHERE customerID IN(SELECT DISTINCT customerID FROM orders_2)
