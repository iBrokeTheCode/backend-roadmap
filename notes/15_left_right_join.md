# `LEFT JOIN` and `RIGHT JOIN` in SQL

While `INNER JOIN` (or just `JOIN`) returns only matching rows from both tables, `LEFT JOIN` and `RIGHT JOIN` allow you to retrieve all rows from one table, even if there are no matching rows in the other table. This is crucial for scenarios where you want to see all entries from one side of the relationship, along with any related data from the other side.

## Understanding `LEFT JOIN`

- **Purpose**: `LEFT JOIN` (also known as `LEFT OUTER JOIN`) returns **all records from the left table** (the first table mentioned in the `FROM` clause) and the matching records from the right table. If there's no match in the right table, the columns from the right table will appear as `NULL` in the result.
- **Priority**: The "left" table has priority; all its rows will be included.
- **Syntax**:
  ```sql
  SELECT columns
  FROM LeftTable
  LEFT JOIN RightTable ON LeftTable.common_column = RightTable.common_column;
  ```

**Example**: Displaying all products, along with their sales details if they exist.

Let's adapt the previous `INNER JOIN` example to a `LEFT JOIN`:

```sql
SELECT
    P.prod_ID,
    P.description,
    SUM(BD.quantity) AS units_sold -- Sums quantities from sales_detail
FROM
    products P -- This is the LEFT table (priority table)
LEFT JOIN sales_detail BD ON BD.prod_ID = P.prod_ID -- Join with sales_detail
GROUP BY
    P.prod_ID, P.description -- Group by product ID and description
ORDER BY
    P.prod_ID;
```

- **Result**: This query will list **every product** from the `products` table (ID, description). If a product has sales, its `units_sold` will be shown. If a product has no sales, `units_sold` will be `NULL`. This is useful for identifying unsold products.

## Understanding `RIGHT JOIN`

- **Purpose**: `RIGHT JOIN` (also known as `RIGHT OUTER JOIN`) returns **all records from the right table** (the second table mentioned in the `FROM` clause) and the matching records from the left table. If there's no match in the left table, the columns from the left table will appear as `NULL` in the result.
- **Priority**: The "right" table has priority; all its rows will be included.
- **Syntax**:
  ```sql
  SELECT columns
  FROM LeftTable
  RIGHT JOIN RightTable ON LeftTable.common_column = RightTable.common_column;
  ```

**Example**: Displaying all sales details, along with their product information if the product exists.

```sql
SELECT
    P.prod_ID,
    P.description,
    SUM(BD.quantity) AS units_sold
FROM
    products P -- This is the LEFT table
RIGHT JOIN sales_detail BD ON P.prod_ID = BD.prod_ID -- sales_detail is the RIGHT table (priority table)
GROUP BY
    P.prod_ID, P.description -- Group by product ID and description
ORDER BY
    P.prod_ID;
```

- **Result**: This query will list **every sales detail record** (and aggregate its quantity). If a sales detail record refers to a `prod_ID` that does not exist in the `products` table, then `P.prod_ID` and `P.description` will appear as `NULL`. This is useful for identifying "orphan" sales records that don't link to existing product master data. In the provided example, the instructor demonstrated how this can reveal `prod_ID` values in `sales_detail` (like `10502` or `65535`) that don't exist in the `products` table, resulting in `NULL` for the product description and ID from the left table.

## Key Takeaways

- **Choosing the Right Join**:
  - Use **`INNER JOIN`** when you only want records that have a match in _both_ tables.
  - Use **`LEFT JOIN`** when you want _all records from the left table_, plus matching records from the right table (with `NULL` for non-matches on the right).
  - Use **`RIGHT JOIN`** when you want _all records from the right table_, plus matching records from the left table (with `NULL` for non-matches on the left).
- **Logical Order**: The order of tables in your `FROM` and `JOIN` clauses determines what is "left" and "right."
