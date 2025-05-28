# The `WHERE` Clause in SQL

The `WHERE` clause is a fundamental part of SQL DML (Data Manipulation Language) statements, allowing you to filter records based on specified conditions. While commonly used with `SELECT`, it's also applicable to `UPDATE` and `DELETE` statements to target specific rows.

## Basic Syntax

The basic structure for using `WHERE` is:

```sql
SELECT column1, column2
FROM TableName
WHERE condition;
```

## Filtering Data with `WHERE`

You can use various operators within the `WHERE` clause to define your conditions:

- **Comparison Operators**:
  - `=` (Equal to)
  - `>` (Greater than)
  - `<` (Less than)
  - `>=` (Greater than or equal to)
  - `<=` (Less than or equal to)
  - `!=` or `<>` (Not equal to)
  - **Example**: To find products with a price greater than zero:
    ```sql
    SELECT *
    FROM products
    WHERE prod_price > 0;
    ```

## Combining Conditions with Logical Operators

You can combine multiple conditions using logical operators:

- **`AND`**: Returns true if all conditions are true.
- **`OR`**: Returns true if at least one condition is true.
- **Parentheses `()`**: Use parentheses to group conditions and control the order of evaluation, just like in mathematical expressions.
  - **Example**: To find products where the price is greater than 0 **OR** the product ID is greater than 10:
    ```sql
    SELECT prod_price, prod_prod_ID
    FROM products
    WHERE prod_price > 0 OR prod_ID > 10;
    ```
  - **Example**: To find products where the price is greater than 0 **AND** the product ID is greater than 10 **AND** the provider ID is between 10 and 50:
    ```sql
    SELECT prod_price, prod_ID, prod_prob_ID
    FROM products
    WHERE (prod_price > 0 AND prod_ID > 10) AND prod_prob_ID BETWEEN 10 AND 50;
    ```

## Using Table Aliases

When querying multiple tables or to make your queries more concise, you can assign **aliases** to tables. This is particularly useful when columns in different tables share the same name, preventing ambiguity.

- **Syntax**: Assign a short alias (e.g., `P` for `products`) after the table name in the `FROM` clause.
- **Usage**: Use the alias followed by a dot (`.`) before the column name (e.g., `P.prod_description`).
  - **Example**:
    ```sql
    SELECT P.prod_description, P.prod_price
    FROM products P
    WHERE P.prod_price > 100;
    ```

## Filtering Date and Time Data

When filtering by dates and times, MySQL expects a specific format, typically enclosed in single quotes:

- **Date Format**: `'YYYY-MM-DD'` (e.g., `'2018-01-02'`). Days and months should be two digits, padded with a leading zero if necessary (e.g., `01` for January).
- **Datetime Format**: `'YYYY-MM-DD HH:MM:SS'` (e.g., `'2018-01-02 10:50:50'`).
  - **Example**: To find sales after a specific date:
    ```sql
    SELECT *
    FROM sales
    WHERE sales_date > '2018-01-02';
    ```

## Using Date/Time Functions in `WHERE`

MySQL provides functions to extract parts of a date or time, allowing for more flexible filtering:

- **`YEAR()`**: Extracts the year from a date.
- **`MONTH()`**: Extracts the month from a date.
- **`DAY()`**: Extracts the day from a date.
- **Example**: To find sales only from the year 2018:

  ```sql
  SELECT *
  FROM sales
  WHERE YEAR(sales_date) = 2018;
  ```

  **Alternative for SQLite**

  ```sql
  SELECT *
  FROM ventas
  where strftime('%Y', Ventas_Fecha) == '2024';

  -- To retrieve year only
  SELECT strftime('%Y', v.Ventas_Fecha) AS year
  FROM ventas v
  WHERE year == '2024';
  ```

- **Example**: To find sales from months greater than January:

  ```sql
  SELECT *
  FROM sales
  WHERE MONTH(sales_date) > 1;
  ```

  **Alternative for SQLite**

  ```sql
  SELECT *
  FROM ventas
  WHERE strftime('%m', ventas.Ventas_Fecha) > '01';
  ```

## Using the `BETWEEN` Operator

The `BETWEEN` operator allows you to filter values within a specified range (inclusive).

- **Syntax**: `column_name BETWEEN value1 AND value2`
  - **Example**: To find sales between January 1st and January 3rd, 2018:
    ```sql
    SELECT *
    FROM sales
    WHERE sales_date BETWEEN '2018-01-01' AND '2018-01-03';
    ```
