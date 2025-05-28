# `NOT NULL` Constraints in SQL

This session focused on the **`NOT NULL` constraint**, a fundamental rule in SQL that prevents a column from containing `NULL` values. By default, columns can usually hold `NULL`, meaning they can be left empty. The `NOT NULL` constraint changes this, ensuring that a specified field always has a value.

## What is a `NOT NULL` Constraint?

- **Purpose:** To force a column to always contain a value, preventing it from being left empty (`NULL`).
- **Implication:** If you try to insert a new record or update an existing one without providing a value for a `NOT NULL` column, the database will return an error, and the operation will fail.
- **Example:** In a `suppliers` table, while a `phone` number might be optional (allowing `NULL`), the `supplier_name` should almost certainly be `NOT NULL` to ensure you always know who the supplier is.

## Assigning a `NOT NULL` Constraint

There are several ways to apply the `NOT NULL` constraint:

### 1. During Table Creation

This is the most common way to define `NOT NULL` when you initially create a table.

- **Syntax:**
  ```sql
  CREATE TABLE table_name (
      column_name DATATYPE NOT NULL,
      -- ... other columns ...
  );
  ```
- **Example (for `suppliers` table):**
  First, the tutorial demonstrated dropping the `suppliers` table to start fresh:
  ```sql
  DROP TABLE suppliers; -- If it exists
  ```
  Then, creating the `suppliers` table with `NOT NULL` on `supplier_name`:
  ```sql
  CREATE TABLE suppliers (
      supplier_code INT PRIMARY KEY AUTO_INCREMENT,
      supplier_name VARCHAR(255) NOT NULL, -- NOT NULL constraint defined here
      phone VARCHAR(20)
  );
  ```
- **Verification:** You can check the table's DDL (Data Definition Language) in your SQL client to confirm `supplier_name` is listed as `NOT NULL`.

### 2. Modifying an Existing Table to be `NOT NULL` (`ALTER TABLE CHANGE COLUMN`)

You can modify an existing column to enforce the `NOT NULL` constraint if it wasn't set during creation or if it was previously nullable.

- **Syntax:**

  ```sql
  ALTER TABLE table_name
  CHANGE COLUMN existing_column_name existing_column_name DATATYPE NOT NULL;
  ```

  - **`CHANGE COLUMN`**: Used to modify an existing column's definition.
  - **`existing_column_name existing_column_name DATATYPE`**: You must repeat the column name and its data type, even if you're not changing them, before adding `NOT NULL`.

- **Example (making `supplier_name` `NOT NULL` again):**
  The lesson first made `supplier_name` nullable using `MODIFY COLUMN`:
  ```sql
  ALTER TABLE suppliers
  MODIFY COLUMN supplier_name VARCHAR(255) NULL; -- Temporarily allow NULL
  ```
  Then, it demonstrated using `CHANGE COLUMN` to make it `NOT NULL` again:
  ```sql
  ALTER TABLE suppliers
  CHANGE COLUMN supplier_name supplier_name VARCHAR(255) NOT NULL;
  ```

## Removing the `NOT NULL` Constraint (Making a Column Nullable)

If you need to allow a column to accept `NULL` values after it was defined as `NOT NULL`, you can use `ALTER TABLE` with `MODIFY COLUMN` or `CHANGE COLUMN`.

- **Syntax (using `MODIFY COLUMN` - often simpler):**

  ```sql
  ALTER TABLE table_name
  MODIFY COLUMN column_name DATATYPE NULL;
  ```

  - **`MODIFY COLUMN`**: Directly changes a column's definition. You don't need to repeat the column name.

- **Example (making `supplier_name` nullable):**
  ```sql
  ALTER TABLE suppliers
  MODIFY COLUMN supplier_name VARCHAR(255) NULL;
  ```
- **Verification:** Check the DDL to confirm `supplier_name` no longer has `NOT NULL` beside it.

## Illustrating `NOT NULL` Constraint in Action (Error Handling)

The impact of `NOT NULL` is most evident when you try to violate it.

- **Scenario:** Attempting to insert a record into `suppliers` without providing a `supplier_name` (assuming `supplier_name` is `NOT NULL`).
  ```sql
  INSERT INTO suppliers (phone)
  VALUES ('50395xxxxx'); -- Omitting supplier_name
  ```
- **Result:** The database will return an error (e.g., "Column 'supplier_name' cannot be null"), because the `NOT NULL` constraint prevents the insertion of an incomplete record.
- **Resolution:** To successfully insert the record, you must provide a value for the `supplier_name`:
  ```sql
  INSERT INTO suppliers (supplier_name, phone)
  VALUES ('Example Company', '50395xxxxx');
  ```
  This will now insert the record correctly.
