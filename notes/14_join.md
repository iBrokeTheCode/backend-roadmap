# Table Joins with `JOIN` (or `INNER JOIN`) in SQL

While you can technically join tables using the `WHERE` clause, the professional and standard way to combine data from multiple tables in SQL is by using the `JOIN` clause (often synonymous with `INNER JOIN`). This method provides a cleaner, more organized, and often more optimized approach to connecting related data.

## Why Use `JOIN` Instead of `WHERE` for Joins?

- **Professional Standard**: All SQL professionals use `JOIN` syntax for combining tables.
- **Clarity and Readability**: `JOIN` statements explicitly define the relationship between tables, making complex queries easier to read and understand.
- **Optimization**: Database engines are highly optimized to process `JOIN` clauses efficiently, potentially leading to better performance than `WHERE`-based joins, especially in complex scenarios.
- **Flexibility**: The `JOIN` syntax naturally extends to other types of joins (like `LEFT JOIN`, `RIGHT JOIN`, `FULL JOIN`), which offer more control over how records are matched and included in the result.

## Basic Syntax: `JOIN` (or `INNER JOIN`)

The `JOIN` keyword is typically placed after the `FROM` clause, followed by the table you want to join and the `ON` clause, which specifies the join condition.

```sql
SELECT columns_to_retrieve
FROM Table1 Alias1
JOIN Table2 Alias2 ON Alias1.common_column = Alias2.common_column;
```

- **`JOIN` (or `INNER JOIN`)**: These two keywords are synonyms. `INNER JOIN` is more explicit, but `JOIN` by itself defaults to an inner join. An **`INNER JOIN`** returns only the rows where there's a match in _both_ tables based on the `ON` condition. Rows that don't have a match in either table are excluded from the result.
- **`ON`**: This clause specifies the join condition, which defines how the rows from one table relate to the rows from another. It's usually based on matching primary key/foreign key columns.

**Example**: Joining `products` with `sales_detail` to see which products were sold in which detail lines.

```sql
SELECT *
FROM products P -- Alias 'P' for products
JOIN sales_detail BD ON BD.prod_ID = P.prod_ID; -- Alias 'BD' for sales_detail
```

This will retrieve all columns from both tables, showing only product records that have corresponding entries in `sales_detail`.

## Joining Multiple Tables

You can chain multiple `JOIN` clauses to connect more than two tables in your query.

**Example**: Building a comprehensive sales report by joining `sales`, `clients`, `sales_detail`, `products`, and `suppliers`:

```sql
SELECT
    V.invoice_number,
    C.social_reason AS client_name,
    V.sale_date,
    BD.prod_ID,
    P.description AS product_description,
    PR.supplier_name AS supplier_name
FROM
    sales V -- Sales table with alias 'V'
JOIN clients C ON V.cli_ID = C.cli_ID -- Join Sales to Clients
JOIN sales_detail BD ON BD.sale_ID = V.sale_ID -- Join Sales to Sales_Detail
JOIN products P ON BD.prod_ID = P.prod_ID -- Join Sales_Detail to Products
JOIN suppliers PR ON P.supplier_ID = PR.supplier_ID; -- Join Products to Suppliers
```

## Adding Conditions to `JOIN` Clauses

A powerful feature of `JOIN` is that you can include additional filtering conditions directly within the `ON` clause using `AND`. This allows you to apply specific filters for each table as part of the join process, making the query very organized and efficient.

**Example**: Filtering the combined sales data by specific criteria within the joins:

```sql
SELECT
    V.invoice_number,
    C.social_reason AS client_name,
    V.sale_date,
    BD.prod_ID,
    P.description AS product_description,
    PR.supplier_name AS supplier_name
FROM
    sales V
JOIN clients C ON V.cli_ID = C.cli_ID
JOIN sales_detail BD ON BD.sale_ID = V.sale_ID AND BD.cost > 1000 -- Filter sales details where cost > 1000
JOIN products P ON BD.prod_ID = P.prod_ID
JOIN suppliers PR ON P.supplier_ID = PR.supplier_ID AND PR.status = 1 -- Filter suppliers with status = 1
WHERE
    V.sale_date BETWEEN '2018-01-22' AND '2018-01-24'; -- General filter for sales date
```

- **Benefit**: This structure keeps the join conditions and specific table filters logically grouped, enhancing readability and maintainability. It effectively filters the rows _during_ the join process, potentially reducing the number of rows that need to be processed further.
