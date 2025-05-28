# Adding Columns and Records to Tables

This session served as a practical interlude to learning about constraints, focusing on how to dynamically modify table structures by adding new columns and how to insert new records into those tables. This is crucial for adapting your database schema and populating it with data.

## 1. Adding a Column to an Existing Table (`ALTER TABLE ADD COLUMN`)

You can add new columns to an existing table using the `ALTER TABLE` statement. This allows you to expand your table's structure without having to recreate it from scratch.

- **Syntax:**

  ```sql
  ALTER TABLE table_name
  ADD COLUMN new_column_name DATATYPE [CONSTRAINT] [AFTER existing_column];
  ```

  - **`ALTER TABLE table_name`**: Specifies the table you want to modify.
  - **`ADD COLUMN new_column_name DATATYPE`**: Defines the name and data type of the new column.
  - **`[CONSTRAINT]`**: You can optionally add constraints (like `NOT NULL`, `UNIQUE`, `DEFAULT`) to the new column right away.
  - **`[AFTER existing_column]`**: This optional clause specifies the position of the new column relative to an existing one. If omitted, the column is usually added to the end of the table.

- **Example: Adding a `gender` column to the `clients` table**
  First, the tutorial demonstrated dropping and recreating the `clients` table to start fresh:

  ```sql
  DROP TABLE clients; -- If it exists
  CREATE TABLE clients (
      client_code INT PRIMARY KEY AUTO_INCREMENT,
      name VARCHAR(255),
      last_name VARCHAR(255),
      email VARCHAR(255),
      complaint_count INT
  );
  ```

  Then, adding the `gender` column:

  ```sql
  ALTER TABLE clients
  ADD COLUMN gender ENUM('M', 'F') AFTER last_name;
  ```

  - **`ENUM('M', 'F')`**: This is a specific data type that restricts the column's values to a predefined list (in this case, 'M' for Masculine or 'F' for Feminine).
  - **`AFTER last_name`**: Places the `gender` column immediately after the `last_name` column.

- **Verification**: You can verify the new column by checking the table's DDL (Data Definition Language) in your SQL client.

---

## 2. Adding Records (Rows) to a Table (`INSERT INTO`)

Once your table structure is ready, you insert new records using the `INSERT INTO` statement.

- **Syntax (explicit column list - recommended):**

  ```sql
  INSERT INTO table_name (column1, column2, column3, ...)
  VALUES (value1, value2, value3, ...);
  ```

  - **`INSERT INTO table_name`**: Specifies the target table.
  - **`(column1, column2, ...)`**: A comma-separated list of the columns you are providing values for. This is highly recommended for clarity and robustness.
  - **`VALUES (value1, value2, ...)`**: A comma-separated list of values, corresponding to the order of the columns specified. String values must be enclosed in single quotes (`'`).

- **Key Points for `INSERT`:**

  - **`AUTO_INCREMENT` columns**: You do _not_ include columns with `AUTO_INCREMENT` in your column list or `VALUES` clause, as the database automatically generates their values.
  - **Order Matters**: The order of values in the `VALUES` clause must match the order of columns in the column list.

- **Example: Inserting a new client record**
  ```sql
  INSERT INTO clients (name, last_name, gender, email, complaint_count)
  VALUES ('Carlos', 'Martinez', 'M', 'carlosmartinez@gmail.com', 0);
  ```
  - This will insert a new row into the `clients` table. The `client_code` will be automatically generated, and the specified values will be placed into their respective columns.
