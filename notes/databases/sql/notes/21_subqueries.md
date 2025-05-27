# Subqueries in SQL

A **subquery** (also called an inner query or inner select) is simply a `SELECT` statement embedded within another SQL query. Subqueries allow you to perform complex queries by using the results of one query as input for another. They can be placed in several parts of a main query.

## Where Subqueries Can Be Used

Subqueries can typically be executed in three main locations within a SQL statement:

1.  **In the `SELECT` Clause (List of Fields)**: To display a calculated or retrieved value from another table alongside your main query results for each row.
2.  **In the `FROM` Clause (As a Table/Source)**: To create a temporary, derived table on which the main query operates. This allows you to pre-filter or aggregate data before joining.
3.  **In the `WHERE` Clause (As a Condition)**: To filter the main query's results based on values returned by the subquery.

## 1. Subqueries in the `SELECT` Clause

When a subquery is in the `SELECT` clause, it executes once for _each row_ of the outer query. It's often used to retrieve an aggregate value or a single piece of related information.

- **Syntax**:
  ```sql
  SELECT
      column1,
      column2,
      (SELECT aggregate_function(another_column) FROM another_table WHERE condition) AS subquery_result_alias
  FROM
      main_table;
  ```
- **Key**: The subquery must typically return a **single value** (scalar subquery) for each row of the outer query.
- **Example**: Displaying product details along with the total units sold for each product:
  ```sql
  SELECT
      P.prod_ID,
      P.prod_description,
      P.prod_color,
      (SELECT SUM(BD.quantity) FROM sales_detail BD WHERE BD.prod_ID = P.prod_ID) AS total_units_sold,
      (SELECT SUM(BD.price) FROM sales_detail BD WHERE BD.prod_ID = P.prod_ID) AS total_sales_amount
  FROM
      products P;
  ```
  - **Explanation**: For each product in the `products` table, the subquery calculates the `SUM` of `quantity` and `price` from `sales_detail` _only_ for that specific product ID. Products with no sales will show `NULL` for `total_units_sold` and `total_sales_amount`.

## 2. Subqueries in the `FROM` Clause

Using a subquery in the `FROM` clause allows you to treat the result set of the subquery as a temporary table. This is very powerful for pre-aggregating data or filtering it before joining it with other tables.

- **Syntax**:
  ```sql
  SELECT
      main_table.column,
      subquery_alias.column
  FROM
      main_table
  JOIN
      (SELECT column1, aggregate_function(column2) FROM another_table GROUP BY column1 HAVING condition) AS subquery_alias
  ON
      main_table.common_column = subquery_alias.common_column;
  ```
- **Key**: The subquery in the `FROM` clause **must** have an **alias**.
- **Example**: Joining `products` with a pre-aggregated list of sales details for products that sold more than 100 units (sum of quantities):
  ```sql
  SELECT
      P.prod_ID,
      P.prod_description,
      P.prod_color
  FROM
      products P
  JOIN
      (SELECT BD.prod_ID, SUM(BD.quantity) AS total_sold_units -- Subquery calculates total units per product
       FROM sales_detail BD
       GROUP BY BD.prod_ID
       HAVING SUM(BD.quantity) > 100) AS B -- Alias 'B' for the subquery result
  ON
      P.prod_ID = B.prod_ID; -- Join on the product ID
  ```
  - **Explanation**: This query first calculates the total units sold for each product (`SUM(BD.quantity) GROUP BY BD.prod_ID`) and filters for only those products where the total units sold are greater than 100 (`HAVING SUM(BD.quantity) > 100`). The result of this subquery (a temporary table `B`) is then joined with the `products` table (`P`) to retrieve the main product information.
  - You can then combine this with a subquery in the `SELECT` clause to show the actual `total_sold_units` as well:
    ```sql
    SELECT
        P.prod_ID,
        P.prod_description,
        P.prod_color,
        (SELECT SUM(BD2.quantity) FROM sales_detail BD2 WHERE BD2.prod_ID = P.prod_ID) AS units_sold_for_this_product
    FROM
        products P
    JOIN
        (SELECT BD.prod_ID, SUM(BD.quantity) AS total_sold_units
         FROM sales_detail BD
         GROUP BY BD.prod_ID
         HAVING SUM(BD.quantity) > 100) AS B
    ON
        P.prod_ID = B.prod_ID;
    ```

## 3. Subqueries in the `WHERE` Clause

Subqueries in the `WHERE` clause are used to filter the results of the outer query based on a condition that depends on the subquery's output.

- **Syntax**:
  ```sql
  SELECT
      column1, column2
  FROM
      main_table
  WHERE
      column_to_filter_on IN (SELECT value_to_match FROM another_table WHERE condition)
  OR
      column_to_filter_on > (SELECT single_value FROM another_table WHERE condition);
  ```
- **Key**: The subquery must return values that can be compared with the column in the outer `WHERE` clause. It can return a single value (for comparison operators like `=`, `>`, `<`) or a list of values (for operators like `IN`, `EXISTS`).
- **Example**: Selecting all products that have total sales greater than 100 units:
  ```sql
  SELECT
      P.* -- Select all columns from products table
  FROM
      products P
  WHERE
      (SELECT SUM(BD.quantity) FROM sales_detail BD WHERE BD.prod_ID = P.prod_ID) > 100;
  ```
  - **Explanation**: This query will return all columns from the `products` table, but only for those products where the sum of their sold quantities (calculated by the subquery) is greater than 100.

## Performance Considerations

While subqueries are very powerful and flexible, they can sometimes impact query performance, especially in very large databases. Each subquery needs to be executed, and in some cases (like scalar subqueries in the `SELECT` clause), they might execute for every row of the outer query, leading to significant overhead. It's important to consider alternative approaches (like `JOIN`s) if performance becomes an issue. However, for many common scenarios, subqueries offer a concise and readable way to achieve complex data retrieval.
