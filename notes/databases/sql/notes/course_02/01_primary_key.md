# Primary Key Constraints in SQL

This session introduced **SQL constraints**, which are rules applied to the data in a table to ensure its accuracy and reliability. If a data action violates a constraint, the action is aborted. Constraints can be applied at the column level (affecting only that column) or at the table level (affecting multiple columns).

## Common SQL Constraints

The lesson reviewed several common SQL constraints:

- **`NOT NULL`**: Ensures a column cannot contain `NULL` values. (Already used)
- **`UNIQUE`**: Guarantees that all values in a column are distinct. (Already used)
- **`PRIMARY KEY`**: A combination of `NOT NULL` and `UNIQUE`. It **uniquely identifies** each row in a table. (Already used)
- **`FOREIGN KEY`**: Prevents actions that would break links between tables. (New)
- **`CHECK`**: Ensures that values in a column satisfy a specific condition. (New)
- **`DEFAULT`**: Sets a default value for a column if no value is specified during insertion. (New)
- **`CREATE INDEX`**: Used to create indexes, which speed up data retrieval. (New)

## Understanding Primary Keys (`PRIMARY KEY`)

A primary key is essential for uniquely identifying each record in a table. It's a fundamental concept in relational databases.

**Key Characteristics of a Primary Key:**

- **Unique**: Each value in the primary key column(s) must be different.
- **Not Null**: The primary key column(s) cannot contain `NULL` values.
- **Uniquely Identifies**: It serves as the main identifier for records in the table.

**Assigning a Primary Key**

You can assign a primary key in two main ways when creating a table:

1.  **Column-level definition**:

    ```sql
    CREATE TABLE table_name (
        column_id INT AUTO_INCREMENT PRIMARY KEY, -- Primary key defined on the column itself
        column_name VARCHAR(255)
    );
    ```

    - The `AUTO_INCREMENT` property (which only works with `PRIMARY KEY` or `UNIQUE` constraints) automatically generates sequential unique numbers for new records.

2.  **Table-level definition**: This method is often preferred for clarity, especially when defining composite primary keys (keys made of multiple columns).
    ```sql
    CREATE TABLE sales (
        purchase_number INT UNSIGNED AUTO_INCREMENT,
        client_code INT,
        product_code INT,
        supplier_code INT,
        -- ... other columns ...
        PRIMARY KEY (purchase_number) -- Primary key defined at the table level
    );
    ```
