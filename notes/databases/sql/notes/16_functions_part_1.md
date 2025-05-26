# Functions in SQL (Part 1)

SQL offers a vast array of built-in functions to perform calculations, manipulate data, and retrieve system information. This lesson covers several key functions, including conditional logic (`IF`, `CASE`), string manipulation (`SUBSTRING`), and various date/time and system functions.

## 1. Conditional Functions: `IF` and `CASE`

These functions allow you to introduce conditional logic into your `SELECT` statements, returning different values based on whether a condition is true or false.

### `IF()` Function

The `IF()` function evaluates a condition and returns one value if the condition is true, and another if it's false. It's limited to simple true/false evaluations.

- **Syntax**: `IF(condition, value_if_true, value_if_false)`
- **Example**: Displaying "Enabled" or "Disabled" based on a product's status:
  ```sql
  SELECT
      P.prod_ID,
      P.prod_description,
      IF(P.prod_status = 1, 'Enabled', 'Disabled') AS product_state
  FROM
      products P;
  ```
- **Limitation**: `IF()` can only handle two outcomes (true or false). For multiple conditions, `CASE` is preferred.

### `CASE` Statement

The `CASE` statement is a more versatile and widely used conditional construct, allowing you to define multiple conditions and corresponding results. It's standard across many SQL databases (including MySQL and SQL Server).

- **Syntax (Simple `CASE`)**:
  ```sql
  CASE expression
      WHEN value1 THEN result1
      WHEN value2 THEN result2
      ELSE default_result
  END AS alias_name
  ```
- **Syntax (Searched `CASE`)**:
  ```sql
  CASE
      WHEN condition1 THEN result1
      WHEN condition2 THEN result2
      ELSE default_result
  END AS alias_name
  ```
- **Example (Evaluates `prod_status` directly)**:
  ```sql
  SELECT
      P.prod_ID,
      P.prod_description,
      CASE P.prod_status
          WHEN 1 THEN 'Enabled'
          WHEN 0 THEN 'Disabled'
          WHEN 2 THEN 'Other Status'
          ELSE 'Unknown' -- Optional: for any other status value
      END AS product_status_text
  FROM
      products P;
  ```
- **Nested Logic in `CASE`**: You can embed subqueries or other functions within the `WHEN` or `THEN` clauses of a `CASE` statement.
  - **Example**: If a product is enabled, calculate its total sales quantity; otherwise, show "Disabled" or "Other Status":
    ```sql
    SELECT
        P.prod_ID,
        P.prod_description,
        CASE P.prod_status
            WHEN 1 THEN (SELECT SUM(BD.quantity) FROM sales_detail BD WHERE BD.prod_ID = P.prod_ID)
            WHEN 0 THEN 0 -- Or 'Disabled'
            WHEN 2 THEN NULL -- Or 'Other Status'
            ELSE 0
        END AS total_sold_quantity
    FROM
        products P;
    ```

## 2. Null Handling Function: `IFNULL()`

The `IFNULL()` function is used to replace `NULL` values in the result set with a specified alternative value. This is very useful for making your query outputs more readable and preventing `NULL` values from appearing in reports.

- **Syntax**: `IFNULL(expression, value_if_null)`
- **Example**: In the previous `CASE` example, if a product was enabled but had no sales, `SUM(BD.quantity)` would return `NULL`. `IFNULL()` can convert this `NULL` to `0`:
  ```sql
  SELECT
      P.prod_ID,
      P.prod_description,
      CASE P.prod_status
          WHEN 1 THEN IFNULL((SELECT SUM(BD.quantity) FROM sales_detail BD WHERE BD.prod_ID = P.prod_ID), 0)
          WHEN 0 THEN 0
          WHEN 2 THEN 0 -- Assuming you want 0 for 'Other Status' too
          ELSE 0
      END AS total_sold_quantity
  FROM
      products P;
  ```

## 3. String Manipulation Function: `SUBSTRING()`

The `SUBSTRING()` function extracts a portion (substring) from a given string.

- **Syntax**: `SUBSTRING(string, start_position, length)`
  - `string`: The source string.
  - `start_position`: The starting position for extraction (1 for the first character).
  - `length`: The number of characters to extract.
- **Example**: Using `SUBSTRING()` within a `CASE` statement to check the first character of a product description:
  ```sql
  SELECT
      P.prod_ID,
      P.prod_description,
      CASE SUBSTRING(P.prod_description, 1, 1) -- Extracts the first character
          WHEN 'A' THEN 'Starts with A'
          WHEN 'B' THEN 'Starts with B'
          ELSE 'Other'
      END AS description_start_char
  FROM
      products P;
  ```

## 4. Date/Time and System Functions (No `FROM` Clause Needed)

Many functions can be executed directly in a `SELECT` statement without needing a `FROM` clause, as they retrieve system-level or calculated values.

- **`CURRENT_DATE()`**: Returns the current date.
  ```sql
  SELECT CURRENT_DATE() AS today;
  ```
- **`CURRENT_TIME()`**: Returns the current time.
  ```sql
  SELECT CURRENT_TIME() AS now_time;
  ```
- **`CURRENT_TIMESTAMP()`**: Returns the current date and time.
  ```sql
  SELECT CURRENT_TIMESTAMP() AS current_datetime;
  ```
- **`DATABASE()`**: Returns the name of the currently selected database.
  ```sql
  SELECT DATABASE() AS current_db;
  ```
- **`CURRENT_USER()`**: Returns the username and host of the current MySQL user.
  ```sql
  SELECT CURRENT_USER() AS logged_in_user;
  ```
- **`DATEDIFF(date1, date2)`**: Calculates the difference in days between two dates. `date1` should be the later date to get a positive result.
  ```sql
  SELECT DATEDIFF('2023-06-25', '2023-01-01') AS days_passed; -- Result: 175
  ```
  - **Application**: Calculating the age of invoices or records:
    ```sql
    SELECT
        V.invoice_number,
        V.sale_date,
        DATEDIFF(CURRENT_DATE(), V.sale_date) AS days_since_sale
    FROM
        sales V;
    ```
- **`DAYOFWEEK(date)`**: Returns the weekday index for a date (1 = Sunday, 2 = Monday, ..., 7 = Saturday).
  ```sql
  SELECT DAYOFWEEK(CURRENT_DATE()) AS weekday_number;
  ```
