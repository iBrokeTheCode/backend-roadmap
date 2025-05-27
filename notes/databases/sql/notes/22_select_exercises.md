# `SELECT` Exercises

1. Retrieve the dates, invoice numbers and total amount of my Ventas_CliId.

   ```sql
   SELECT Ventas_Fecha, Ventas_NroFactura, Ventas_Total
   FROM ventas;
   ```

2. Retrieve the product IDs, quantity and price from my ventas_detalle table where the price is greater than 0.

   ```sql
   SELECT VD_ProdId, VD_Cantidad, VD_Precio
   FROM ventas_detalle
   WHERE VD_Precio > 0;
   ```

3. Retrieve the total amount for each invoice date.

   ```sql
   SELECT
   Ventas_Fecha,
   SUM(Ventas_Total) AS Total
   FROM ventas
   GROUP BY Ventas_Fecha
   ORDER BY Ventas_Fecha DESC;
   ```

4. Retrieve the total amount for each year and month for invoice number 4.

   ```sql
   SELECT
   strftime('%Y', Ventas_Fecha) AS Year,
   strftime('%m', Ventas_Fecha) AS Month,
   SUM(Ventas_Total) AS Total
   FROM ventas
   GROUP BY Year, Month;
   ```

5. Retrieve the products from the products table that belong to the supplier 28.

   ```sql
   SELECT _
   FROM productos
   WHERE Prod_ProvId = 28;
   ```

6. Retrieve the product IDs and total amount for each invoice.

   ```sql
   SELECT
   VD_ProdId,
   SUM((VD_Cantidad _ VD_Precio)) AS Total
   FROM ventas_detalle
   ORDER BY VD_ProdId;
   ```

---

7. Retrieve the invoice date, invoice number, customer ID, customer name, and total amount sold.

   ```sql
   SELECT
      Ventas_Fecha,
      Ventas_NroFactura,
      Ventas_CliId,
      Ventas_Total,
      Cli_RazonSocial
   FROM ventas
   JOIN clientes ON Cli_Id = Ventas_CliId
   ```

8. Retrieve the invoice date, invoice number, product ID, product description, supplier ID, supplier name, quantity, unit price, and partial price.

   ```sql
   SELECT
      Ventas_Fecha, Ventas_NroFactura,
      VD_Cantidad, VD_Precio, (VD_Cantidad * VD_Precio) AS 'Partial Price',
      Prod_Id, Prod_Descripcion, Prod_ProvId,
      Prov_Nombre
   FROM ventas
   JOIN ventas_detalle ON VD_VentasId = Ventas_Id
   JOIN productos ON Prod_Id = VD_ProdId
   JOIN proveedores ON Prov_Id = Prod_ProvId
   ```

9. Retrieve the product ID, product description, and total quantity sold from all sales between 2024-08-01 and 2024-08-03.

   ```sql
   SELECT
      Prod_Id, Prod_Descripcion,
      SUM(VD_Cantidad) AS Quantity
   FROM ventas_detalle
   JOIN productos ON Prod_Id = VD_ProdId
   JOIN ventas ON Ventas_Id = VD_VentasId
   WHERE Ventas_Fecha BETWEEN '2024-08-01' AND '2024-08-03'
   GROUP BY Prod_Id
   ORDER BY Quantity DESC
   ```

---

10. Retrieve all products whose description starts with the word 'IN'.

```sql
SELECT Prod_Descripcion
FROM productos
WHERE Prod_Descripcion LIKE 'INT%'
```

11. Retrieve all products whose description, color or supplier name contains the word 'RO'.

```sql
SELECT
	Prod_Id, Prod_Descripcion, Prod_Color, Prov_Nombre
FROM productos
JOIN proveedores ON Prov_Id = Prod_ProvId
WHERE concat(Prod_Color, ' ', Prod_Descripcion, ' ', Prov_Nombre) LIKE '%RO%'
```

12. Retrieve all products whose description contains the word 'AS' and has sales.

```sql
SELECT DISTINCT Prod_Id, Prod_Descripcion
FROM productos
JOIN ventas_detalle ON VD_ProdId = Prod_Id
WHERE Prod_Descripcion LIKE '%AS%'
ORDER BY Prod_Id
```

```sql

SELECT Prod_Id, Prod_Descripcion
FROM productos
JOIN ventas_detalle ON VD_ProdId = Prod_Id
WHERE Prod_Descripcion LIKE '%AS%'
GROUP BY Prod_Id
ORDER BY Prod_Id
```

```sql
SELECT Prod_Id, Prod_Descripcion
FROM productos
WHERE Prod_Id IN (SELECT DISTINCT VD_ProdId FROM ventas_detalle) AND Prod_Descripcion LIKE '%AS%'
```
