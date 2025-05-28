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

---

Here's a summary of the lesson on **Unique Constraints and Indexes in SQL**:

---

## Unique Constraints and Indexes in SQL

This session clarified the relationship between **`UNIQUE` constraints** and **indexes** in SQL. While these two concepts are distinct, they are closely related in MySQL, particularly concerning how `UNIQUE` constraints are implemented and managed.

### What are Indexes in SQL?

Indexes in SQL are special lookup tables that the database search engine can use to speed up data retrieval. Think of an index like the index in a book: it helps you quickly find specific information without having to read the entire book from start to finish.

- **How they work:** Indexes order data in a sequential or organized manner, typically created on columns frequently used for filtering (`WHERE` clauses) or sorting (`ORDER BY` clauses).
- **Benefits:** Significantly faster search and retrieval operations.
- **Costs/Drawbacks:**
  - **Performance Overhead on Writes:** Every time data is added, updated, or deleted in an indexed column, the database has to update the index as well. This creates additional overhead, making write operations (INSERT, UPDATE, DELETE) slower on indexed tables, especially those that change frequently.
  - **Storage Space:** Indexes consume additional disk space.
- **When to Use Indexes:** Generally, indexes are best suited for tables where data doesn't change frequently but is heavily queried (read operations).

### Relationship Between `UNIQUE` Constraints and Indexes

In MySQL, when you define a **`UNIQUE` constraint** on a column, the database **automatically creates an index** on that column. This index is what enforces the uniqueness. Because of this close relationship, removing a `UNIQUE` constraint involves dropping its underlying index.

### Creating a `INDEX`

To create an index for a column, you use the `CREATE INDEX` statement with the following format:

```sql
CREATE INDEX index_name ON table_name (column_name);
```

Here's an example:

```sql
CREATE INDEX idx_email ON Empleados(Email);
```

### Removing a `UNIQUE` Constraint

To remove a `UNIQUE` constraint from a table, you use the `ALTER TABLE` statement in conjunction with `DROP INDEX`.

- **Syntax:**

  ```sql
  ALTER TABLE table_name
  DROP INDEX column_name; -- Use DROP INDEX, and specify the column name, NOT the constraint name
  ```

  - **Key points:**
    - You use `DROP INDEX` (not `DROP CONSTRAINT` or `DROP UNIQUE`).
    - You specify the **column name** that had the `UNIQUE` constraint, not a generated constraint name (like `sales_ibfk_1` for foreign keys) and no parentheses around the column name.

- **Example:**
  The lesson demonstrated removing the `UNIQUE` constraint from the `email` column in the `clients` table:
  ```sql
  -- Assuming 'email' column in 'clients' table has a UNIQUE constraint
  ALTER TABLE clients
  DROP INDEX email;
  ```
  After running this, you can verify in your SQL client's information pane (e.g., DDL tab) that the `UNIQUE` constraint on the `email` column is no longer present.
