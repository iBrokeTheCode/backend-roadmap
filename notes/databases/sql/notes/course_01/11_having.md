# The `HAVING` Clause in SQL: Filtering Aggregated Data

You're already familiar with the `WHERE` clause for filtering individual rows based on conditions. However, the `WHERE` clause operates _before_ aggregation (before `GROUP BY` is applied). This means you **cannot** use `WHERE` to filter results based on the output of aggregate functions (like `SUM`, `COUNT`, `AVG`, `MIN`, or `MAX`).

This is where the **`HAVING` clause** comes in. The `HAVING` clause is specifically designed to filter groups of data **after** the `GROUP BY` clause has processed and aggregated the rows. It's often referred to as the "WHERE for `GROUP BY`."

## `WHERE` vs. `HAVING`

It's crucial to understand the difference in their execution order:

- **`WHERE`**: Filters individual rows _before_ aggregation. It works directly on the raw data columns from your tables.
- **`HAVING`**: Filters _groups_ of rows _after_ aggregation. It works on the results of aggregate functions or on the grouping columns themselves.

### Basic Syntax

The `HAVING` clause always comes **after** the `GROUP BY` clause:

```sql
SELECT
    column_to_group_by,
    aggregate_function(column_to_aggregate) AS calculated_field
FROM
    TableName
WHERE
    condition_for_individual_rows -- Optional: filters rows before grouping
GROUP BY
    column_to_group_by
HAVING
    condition_on_calculated_field; -- Filters groups based on aggregate results
```

## Examples of `HAVING`

### 1. Filtering Groups Based on a Summed Total

Let's say you have monthly sales totals grouped by year and month, and you only want to see months where the total sales exceed $1,000,000.

```sql
SELECT
    YEAR(B.sale_date) AS sales_year,
    MONTH(B.sale_date) AS sales_month,
    SUM(B.total_amount) AS monthly_total_sales
FROM
    sales B
GROUP BY
    sales_year, sales_month
HAVING
    monthly_total_sales > 1000000; -- Filters groups where the sum is > 1,000,000
```

Alternative version for SQLite:

```sql
SELECT
	strftime('%Y', Ventas_Fecha) AS Year,
	strftime('%m', Ventas_Fecha) AS Month,
	sum(Ventas_Total) AS Total
FROM ventas
WHERE Year = '2024'
GROUP BY Year, Month
HAVING Total > 230000
ORDER BY Month DESC
```

- **Why `HAVING`?**: If you tried `WHERE monthly_total_sales > 1000000`, it would fail because `monthly_total_sales` is a calculated field that doesn't exist before the `GROUP BY` operation.

### 2. Filtering Groups Based on a Count

Imagine you want to see products that have been sold more than 100 times.

```sql
SELECT
    BD.prod_ID,
    P.description AS product_description,
    COUNT(*) AS sales_count -- Counts how many times each product appears
FROM
    sales_detail BD,
    products P
WHERE
    BD.prod_ID = P.prod_ID -- Join condition
GROUP BY
    BD.prod_ID, P.description
HAVING
    sales_count > 100 -- Filters groups where the count is > 100
ORDER BY
    sales_count DESC; -- Orders the filtered groups by sales count
```

Alternative version for SQLite:

```sql
SELECT
	p.Prod_Id,
	p.Prod_Descripcion,
	count(*) AS Sold_Items
FROM
	ventas_detalle v,
	productos p
WHERE
	v.VD_ProdId = p.Prod_Id
GROUP BY
	p.Prod_Id, p.Prod_Descripcion
HAVING
	Sold_Items > 27
ORDER BY
	Sold_Items DESC
```

- **Building a Ranking**: By combining `GROUP BY`, `HAVING`, and `ORDER BY`, you can easily create rankings (e.g., a ranking of your best-selling products). The `ORDER BY` clause works on the final result set, which includes the calculated fields from the aggregate functions.

## Execution Order of Clauses

It's helpful to visualize the typical processing order of SQL clauses:

1.  **`FROM`**: Determines the tables involved.
2.  **`WHERE`**: Filters individual rows from the tables.
3.  **`GROUP BY`**: Groups the filtered rows based on specified columns.
4.  **Aggregate Functions (in `SELECT`)**: Perform calculations on each group.
5.  **`HAVING`**: Filters the _groups_ based on conditions, often involving aggregate results.
6.  **`SELECT` (final projection)**: Chooses which columns (including calculated ones) to display.
7.  **`ORDER BY`**: Sorts the final result set.
8.  **`LIMIT`/`OFFSET`**: (To be covered next) Restricts the number of rows returned.

Understanding the interaction between `WHERE`, `GROUP BY`, and `HAVING` is key to writing sophisticated SQL queries for data analysis and reporting.
