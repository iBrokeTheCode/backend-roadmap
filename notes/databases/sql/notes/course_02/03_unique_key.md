# Unique Constraints in SQL

This session covered the **`UNIQUE` constraint** in SQL, which ensures that all values in a specified column or set of columns are distinct. It's a crucial constraint for maintaining data integrity, especially when a column needs to have unique values but isn't necessarily the table's primary key.

## Understanding the `UNIQUE` Constraint

- **Purpose:** Guarantees that every value in the constrained column(s) is different from every other value in that same column(s).
- **Relationship with Primary Key:**
  - A **`PRIMARY KEY`** automatically has a `UNIQUE` constraint (along with `NOT NULL`). You don't need to explicitly add `UNIQUE` to a primary key column.
  - A table can have **only one `PRIMARY KEY`**, but it can have **multiple `UNIQUE` constraints** on different columns or combinations of columns.
- **Example Use Case:** In a `clients` table, a `UNIQUE` constraint could be applied to an `email` column, as each client should typically have a distinct email address.

## Assigning a `UNIQUE` Constraint

There are two primary ways to add a `UNIQUE` constraint:

### 1. During Table Creation

You can define the `UNIQUE` constraint directly when you create the table, either at the column level or as a table-level constraint.

- **Syntax (Table-level example, as shown in tutorial):**
  ```sql
  CREATE TABLE clients (
      client_ID INT PRIMARY KEY,
      client_name VARCHAR(255),
      email VARCHAR(255),
      -- ... other columns ...
      UNIQUE KEY (email) -- UNIQUE constraint defined at the table level
  );
  ```
  - To demonstrate this, the tutorial first dropped the `clients` and `sales` tables (since `sales` had a foreign key reference to `clients`).
  - This ensures a fresh creation of the `clients` table with the `UNIQUE` constraint on the `email` column.

### 2. To an Existing Table (`ALTER TABLE`)

You can add a `UNIQUE` constraint to a column in a table that already exists using the `ALTER TABLE` statement.

- **Syntax:**
  ```sql
  ALTER TABLE table_name
  ADD UNIQUE KEY (column_name);
  ```
- **Example:**

  ```sql
  -- First, create the clients table WITHOUT the UNIQUE constraint
  DROP TABLE clients; -- Drop if exists
  CREATE TABLE clients (
      client_ID INT PRIMARY KEY,
      client_name VARCHAR(255),
      email VARCHAR(255)
  );

  -- Now, add the UNIQUE constraint to the email column
  ALTER TABLE clients
  ADD UNIQUE (email);
  ```

## Verifying a `UNIQUE` Constraint

After adding a `UNIQUE` constraint, you can verify its existence through your SQL client's interface:

- Navigate to the table's information (e.g., in HeidiSQL, double-click the table or select "Information" tab).
- Check the "DDL" (Data Definition Language) or "Indexes" tab to confirm that the `UNIQUE` constraint is listed for the specified column (e.g., `email`).

The `UNIQUE` constraint is a powerful tool for maintaining data quality and preventing duplicate entries in columns where uniqueness is required but a primary key is not suitable.
