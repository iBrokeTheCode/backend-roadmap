# `SELECT` Exercises

1. Retrieve the dates, invoice numbers and total amount of my Ventas_CliId

   ```sql
   SELECT Ventas_Fecha, Ventas_NroFactura, Ventas_Total
   FROM ventas;
   ```

2. Retrieve the product IDs, quantity and price from my ventas_detalle table where the price is greater than 0

   ```sql
   SELECT VD_ProdId, VD_Cantidad, VD_Precio
   FROM ventas_detalle
   WHERE VD_Precio > 0;
   ```

3. Retrieve the total amount for each invoice date

   ```sql
   SELECT
   Ventas_Fecha,
   SUM(Ventas_Total) AS Total
   FROM ventas
   GROUP BY Ventas_Fecha
   ORDER BY Ventas_Fecha DESC;
   ```

4. Retrieve the total amount for each year and month for invoice number 4

   ```sql
   SELECT
   strftime('%Y', Ventas_Fecha) AS Year,
   strftime('%m', Ventas_Fecha) AS Month,
   SUM(Ventas_Total) AS Total
   FROM ventas
   GROUP BY Year, Month;
   ```

5. Retrieve the products from the products table that belong to the supplier 28

   ```sql
   SELECT _
   FROM productos
   WHERE Prod_ProvId = 28;
   ```

6. Retrieve the product IDs and total amount for each invoice

   ```sql
   SELECT
   VD_ProdId,
   SUM((VD_Cantidad _ VD_Precio)) AS Total
   FROM ventas_detalle
   ORDER BY VD_ProdId;
   ```

---
