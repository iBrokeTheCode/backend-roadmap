# Aggregate Functions in SQL

Aggregate functions perform calculations on a set of rows and return a single summary value. They're incredibly powerful for getting insights from your data, often used in conjunction with the `WHERE` clause to filter the data before the calculation.

Here are the main aggregate functions discussed:

- **`COUNT()`**: Counts the number of rows that match a specified criterion.

  - **Syntax**: `COUNT(column_name)` or `COUNT(*)`
  - **Use Case**: To count all records in a table, or to count records that meet specific conditions (e.g., number of sales on a particular date). Using `*` inside `COUNT()` is common for counting rows.
  - **Example**:

    ```sql
    SELECT COUNT(*) AS total_sales
    FROM sales
    WHERE sales_date = '2018-01-02'; -- Counts sales on a specific date
    ```

    Or to count all sales:

    ```sql
    SELECT COUNT(*) AS total_records
    FROM sales;
    ```

    Alternative version for SQLite:

    ```sql
    SELECT count(*) AS total
    FROM ventas
    WHERE strftime('%Y', Ventas_Fecha) = '2024'
    ```

- **`SUM()`**: Calculates the total sum of values in a numeric column.

  - **Syntax**: `SUM(numeric_column_name)`
  - **Use Case**: To get the total amount of sales, total quantity sold, etc.
  - **Example**:

    ```sql
    SELECT SUM(total_amount) AS total_sales_value
    FROM sales
    WHERE YEAR(sales_date) = 2018 AND MONTH(sales_date) = 1; -- Sums sales for Jan 2018
    ```

    Alternative version for SQLite:

    ```sql
    SELECT sum(Ventas_Total) as total
    FROM ventas
    WHERE strftime('%Y', Ventas_Fecha) = '2024' AND strftime('%m', Ventas_Fecha) = '01'
    ```

- **`MIN()`**: Finds the minimum value in a numeric column.

  - **Syntax**: `MIN(numeric_column_name)`
  - **Use Case**: To find the lowest sale amount, the earliest date, etc.
  - **Example**:
    ```sql
    SELECT MIN(total_amount) AS minimum_sale
    FROM sales
    WHERE YEAR(sales_date) = 2018 AND MONTH(sales_date) = 1; -- Finds the min sale in Jan 2018
    ```

- **`MAX()`**: Finds the maximum value in a numeric column.

  - **Syntax**: `MAX(numeric_column_name)`
  - **Use Case**: To find the highest sale amount, the latest date, etc.
  - **Example**:
    ```sql
    SELECT MAX(total_amount) AS maximum_sale
    FROM sales
    WHERE YEAR(sales_date) = 2018 AND MONTH(sales_date) = 1; -- Finds the max sale in Jan 2018
    ```

- **`AVG()`**: Calculates the average value of a numeric column.
  - **Syntax**: `AVG(numeric_column_name)`
  - **Use Case**: To find the average sale amount, average product price, etc.
  - **Example**:
    ```sql
    SELECT AVG(total_amount) AS average_sale
    FROM sales
    WHERE YEAR(sales_date) = 2018 AND MONTH(sales_date) = 1; -- Finds the average sale in Jan 2018
    ```

## Key Points for Aggregate Functions

- **Column Requirement for `SUM`, `MIN`, `MAX`, `AVG`**: Unlike `COUNT(*)`, these functions **require a specific column name** as an argument because they operate on the values within that column.
- **Filtering with `WHERE`**: Aggregate functions are often used with a `WHERE` clause to limit the scope of the calculation to specific records. The function then operates only on the rows that pass the `WHERE` condition.
- **Speed and Efficiency**: Modern database engines like MySQL are highly optimized to perform these calculations very quickly, even on large datasets.

These aggregate functions are powerful on their own, but their true potential is unlocked when combined with the `GROUP BY` clause, which will be discussed in the next lesson. `GROUP BY` allows you to apply these functions to distinct groups of data within your table, providing subtotals and granular summaries.
