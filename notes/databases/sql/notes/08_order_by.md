# The `ORDER BY` Clause in SQL

The `ORDER BY` clause in SQL allows you to sort the results of your `SELECT` query. This clause processes the data **after** it has been retrieved and filtered by the `WHERE` clause. This means you can order by any column in your result set, regardless of whether that column has an index or not.

## Basic Syntax

The `ORDER BY` clause comes **after** the `FROM` (and `WHERE`) clause in your SQL statement.

```sql
SELECT column1, column2
FROM TableName
WHERE condition
ORDER BY column_to_sort_by;
```

## Sorting Order

- **Ascending Order (`ASC`)**: This is the default sort order. If you don't specify `ASC` or `DESC`, the results will be sorted in ascending order (A-Z for text, lowest to highest for numbers, oldest to newest for dates).
  ```sql
  SELECT prod_ID, prod_description, prod_price
  FROM products
  ORDER BY prod_description ASC; -- Or simply ORDER BY prod_description;
  ```
- **Descending Order (`DESC`)**: To sort in descending order (Z-A for text, highest to lowest for numbers, newest to oldest for dates), you must explicitly use the `DESC` keyword.
  ```sql
  SELECT prod_ID, prod_description, prod_price
  FROM products
  ORDER BY prod_description DESC;
  ```

## Sorting by Multiple Columns

You can sort your results by more than one column. Simply list the columns in the `ORDER BY` clause, separated by commas. The sorting will occur in the order you list the columns.

- The results will first be sorted by the first column. If there are duplicate values in the first column, those rows will then be sorted by the second column, and so on.
- You can specify `ASC` or `DESC` independently for each column.

**Example**: Sort sales by date in descending order, and then by product description in ascending order for sales on the same date.

```sql
SELECT
    B.invoice_number,
    C.social_reason AS client_name,
    B.sale_date,
    BD.product_ID,
    P.description AS product_description
FROM
    sales B,
    clients C,
    sales_detail BD,
    products P
WHERE
    B.client_ID = C.client_ID
    AND BD.sale_ID = B.sale_ID
    AND BD.product_ID = P.product_ID
ORDER BY
    B.sale_date DESC, -- Sorts dates from newest to oldest
    P.description ASC; -- For same dates, sorts product descriptions alphabetically
```

This ensures that for any given date, the products sold on that date will appear in alphabetical order by their description.
