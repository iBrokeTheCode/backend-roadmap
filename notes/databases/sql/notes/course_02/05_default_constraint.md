# Default Constraints in SQL

This session covered the **`DEFAULT` constraint** in SQL, which allows you to specify a default value for a column. This default value will be automatically inserted into the column for any new records if no other value is explicitly provided. It's especially useful for columns where a common starting value is expected.

## What is a `DEFAULT` Constraint?

- **Purpose:** To set a predefined value that a column will take if no value is specified during an `INSERT` operation.
- **Benefit:** Simplifies data entry by automatically populating fields with common values, reducing the need for manual input.
- **Example:** In a `clients` table, a `complaint_count` column could have a `DEFAULT` value of `0`. This means whenever a new client is added without specifying a `complaint_count`, it will automatically be set to `0`.

## Assigning a `DEFAULT` Constraint

There are two primary ways to add a `DEFAULT` constraint:

#### 1. During Table Creation

You can define the `DEFAULT` constraint directly when you create the table.

- **Syntax:**
  ```sql
  CREATE TABLE table_name (
      column_name DATATYPE DEFAULT default_value,
      -- ... other columns ...
  );
  ```
- **Example (for `clients` table):**
  First, the tutorial demonstrated dropping the `clients` table to start fresh:
  ```sql
  DROP TABLE clients; -- If it exists
  ```
  Then, creating the `clients` table with the `DEFAULT` constraint on `complaint_count`:
  ```sql
  CREATE TABLE clients (
      client_code INT PRIMARY KEY AUTO_INCREMENT,
      name VARCHAR(255),
      last_name VARCHAR(255),
      email VARCHAR(255),
      gender ENUM('M', 'F'),
      complaint_count INT DEFAULT 0 -- DEFAULT constraint defined here
  );
  ```

#### 2. To an Existing Table (`ALTER TABLE`)

You can modify an existing table to add or change a `DEFAULT` constraint on a column using `ALTER TABLE`.

- **Syntax (to add/change DEFAULT):**

  ```sql
  ALTER TABLE table_name
  CHANGE COLUMN existing_column_name existing_column_name DATATYPE DEFAULT default_value;
  ```

  - **`CHANGE COLUMN`**: This clause is used to modify an existing column's definition.
  - **`existing_column_name existing_column_name`**: You need to repeat the column name if you're not changing its name.
  - **`DATATYPE`**: You must re-specify the column's data type, even if it's not changing.

- **Example (for `clients` table `complaint_count`):**
  First, ensure `clients` exists without the `DEFAULT` constraint:
  ```sql
  DROP TABLE clients; -- Drop if exists
  CREATE TABLE clients ( -- Create it without the DEFAULT initially
      client_code INT PRIMARY KEY AUTO_INCREMENT,
      name VARCHAR(255),
      last_name VARCHAR(255),
      email VARCHAR(255),
      gender ENUM('M', 'F'),
      complaint_count INT
  );
  ```
  Now, add the `DEFAULT` constraint:
  ```sql
  ALTER TABLE clients
  CHANGE COLUMN complaint_count complaint_count INT DEFAULT 0;
  ```

## Illustrating `DEFAULT` Constraint Usage

The main benefit of `DEFAULT` is seen during `INSERT` operations when you omit the column that has a default value.

- **Example: Inserting a new client record without specifying `complaint_count`**

  ```sql
  INSERT INTO clients (name, last_name, gender, email)
  VALUES ('Roberto', 'Romero', 'M', 'rr@example.com');
  ```

  - In this case, the `complaint_count` for Roberto Romero will automatically be set to `0` because of the `DEFAULT` constraint.
  - The `client_code` will also be automatically assigned due to its `AUTO_INCREMENT` property.

- **Verification (using `SELECT`):**
  To see the effect, you can retrieve all records from the table:
  ```sql
  SELECT * FROM clients;
  ```
  This will show `Roberto Romero` with `client_code = 1` (or next available ID) and `complaint_count = 0`.
