# Foreign Key Constraints in SQL

This session delves into **foreign key constraints**, a crucial element for establishing relationships between tables and building a **relational database**. Until foreign keys are defined, tables remain isolated collections of data.

## What is a Foreign Key?

A **foreign key (FK)** is a column or a combination of columns in one table (the **child table** or **referencing table**) that refers to the **primary key (PK)** in another table (the **parent table** or **referenced table**). It acts as a link between two tables, ensuring that data in the child table corresponds to existing data in the parent table. This concept is vital for maintaining **referential integrity**, meaning data consistency between related tables.

- **Example from the `sales` database schema:**
  - `client_code` in the `sales` table is a **foreign key** that references `client_code` (which is a **primary key**) in the `clients` table.
  - Similarly, `product_code` in `sales` links to `product_code` in `products`, and `supplier_code` in `products` links to `supplier_code` in `suppliers`.

**Important Considerations for Foreign Keys:**

- **Matching Data Types:** The data type of the foreign key column(s) in the child table **must match** the data type of the primary key column(s) in the parent table.
- **Data Consistency:** Foreign keys prevent actions that would break the links between tables. For example, you cannot delete a client from the `clients` table if there are sales records in the `sales` table referencing that client, unless you specify a deletion rule.

## Defining Foreign Key Constraints

There are several ways to define foreign key constraints in SQL:

### 1. Defining a Foreign Key During Table Creation (Table-Level)

This is a common and clear way to define a foreign key when you're first creating the child table. It's done at the table level after all columns are defined.

- **Syntax:**
  ```sql
  CREATE TABLE child_table_name (
      column1 DATATYPE PRIMARY KEY,
      fk_column DATATYPE,
      -- ... other columns ...
      FOREIGN KEY (fk_column) REFERENCES parent_table_name (pk_column)
      ON DELETE CASCADE -- Optional: Specifies action on parent deletion
  );
  ```
- **`ON DELETE CASCADE`:** This clause specifies what happens to rows in the child table when the referenced row in the parent table is deleted.

  - **`CASCADE`:** If a record in the parent table is deleted, corresponding records in the child table will also be automatically deleted. This is often desired for consistency (e.g., if a client is deleted, all their sales records should also be deleted).
  - Other options exist (e.g., `SET NULL`, `RESTRICT`, `NO ACTION`), but `CASCADE` is a powerful and frequently used choice.

- **Example (for `sales` table referencing `clients`):**
  First, ensure the `sales` table is dropped if it exists from previous exercises:
  ```sql
  DROP TABLE sales;
  ```
  Then, create the `sales` table with the foreign key:
  ```sql
  CREATE TABLE sales (
      purchase_number INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
      client_code INT,
      product_code INT,
      supplier_code INT,
      purchase_date DATE,
      quantity INT,
      price DECIMAL(10,2),
      -- ... other columns ...
      FOREIGN KEY (client_code) REFERENCES clients (client_code)
      ON DELETE CASCADE
  );
  ```

### 2. Adding a Foreign Key to an Existing Table (`ALTER TABLE`)

If a table already exists and you want to add a foreign key constraint to it without recreating the entire table, you use the `ALTER TABLE` statement.

- **Syntax:**

  ```sql
  ALTER TABLE child_table_name
  ADD CONSTRAINT fk_name -- Optional: Give your constraint a name
  FOREIGN KEY (fk_column) REFERENCES parent_table_name (pk_column)
  ON DELETE CASCADE;
  ```

  - It's good practice to name your foreign key constraints (e.g., `fk_name`) for easier management later. If you don't provide a name, the database will generate one.

- **Example (for `sales` table referencing `clients`):**
  First, ensure `sales` exists without the FK constraint:
  ```sql
  DROP TABLE sales; -- Drop if it exists
  CREATE TABLE sales ( -- Create it without the FK initially
      purchase_number INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
      client_code INT,
      product_code INT,
      supplier_code INT,
      purchase_date DATE,
      quantity INT,
      price DECIMAL(10,2)
  );
  ```
  Now, add the foreign key constraint:
  ```sql
  ALTER TABLE sales
  ADD FOREIGN KEY (client_code) REFERENCES clients (client_code)
  ON DELETE CASCADE;
  ```

### 3. Removing a Foreign Key Constraint (`ALTER TABLE DROP FOREIGN KEY`)

You might need to remove a foreign key constraint to modify table structures or resolve issues.

- **Syntax:**
  ```sql
  ALTER TABLE child_table_name
  DROP FOREIGN KEY fk_constraint_name;
  ```
- **Important:** You need the actual **name of the foreign key constraint**, not just the column name. You can find this name in your SQL client's table information (e.g., DDL or Indexes tab). MySQL often generates names like `table_name_ibfk_1`.

- **Example (for `sales` table's client foreign key):**
  If the constraint name is `sales_ibfk_1`:
  ```sql
  ALTER TABLE sales
  DROP FOREIGN KEY sales_ibfk_1;
  ```

### 4. Defining a Foreign Key Using a Graphical Interface

Most SQL client tools provide a graphical interface to add or modify constraints without writing SQL code. This is a convenient alternative for visual users.

1.  Right-click on the child table (e.g., `sales`) in the database tree.
2.  Select "Alter Table...".
3.  Go to the "Foreign Keys" or "Indexes" tab (interface varies by tool).
4.  Add a new foreign key.
5.  Specify the name of the constraint (e.g., `restriction_client_fk`).
6.  Select the **referencing table** (child table, e.g., `sales`) and its **foreign key column** (e.g., `client_code`).
7.  Select the **referenced table** (parent table, e.g., `clients`) and its **primary key column** (e.g., `client_code`).
8.  Configure `ON DELETE` (e.g., `CASCADE`).
9.  Apply the changes. The tool will generate and execute the corresponding `ALTER TABLE` DDL.
