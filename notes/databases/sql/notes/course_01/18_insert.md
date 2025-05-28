# Inserting Data into Tables with `INSERT`

The **`INSERT`** statement is a fundamental SQL instruction used to add new records (rows) into your database tables. It's how you populate your tables with data.

## Basic `INSERT` Syntax

The most recommended way to use `INSERT` is by explicitly listing the columns you're providing values for. This makes your query more robust against future table structure changes.

```sql
INSERT INTO table_name (column1, column2, ...)
VALUES (value1, value2, ...);
```

- **`INSERT INTO table_name`**: Specifies the table where you want to insert data.
- **`(column1, column2, ...)`**: A comma-separated list of the columns you are providing values for.
- **`VALUES (value1, value2, ...)`**: A comma-separated list of the values to be inserted, corresponding to the order of columns in the list above. String values should be enclosed in single quotes (`'`).

**Example: Inserting into a new `students` table**

First, create a `students` table:

```sql
CREATE TABLE students (
    student_ID INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    student_name VARCHAR(80) NOT NULL
);
```

Now, insert a single student record:

```sql
INSERT INTO students (student_name)
VALUES ('Pablo Tilde');
```

- **Auto-incrementing IDs**: Notice that `student_ID` is not included in the column list or `VALUES` clause because it's an `AUTO_INCREMENT` column. The database automatically generates its value.
- **`NOT NULL` columns**: `student_name` was defined as `NOT NULL`, meaning a value _must_ be provided for it.

## Bulk Inserts: Inserting Multiple Rows at Once

You can insert multiple rows with a single `INSERT` statement by providing multiple sets of `VALUES`, each separated by a comma. This is significantly more efficient than running individual `INSERT` statements for many records.

```sql
INSERT INTO students (student_name)
VALUES
    ('Pedro Jerez'),
    ('Maria Antonieta'),
    ('Pablo Neruda');
```

- **Efficiency**: This "bulk insert" method is highly recommended for adding hundreds or thousands of records, as it reduces the overhead of executing multiple individual commands.

## Inserting into Specific Columns (and Default Values)

When your table has columns with **default values**, you only need to specify the columns for which you want to provide explicit values. The database will use the default values for any omitted columns.

**Example: Inserting into a `products` table with default values**

Assume `products` has `prod_description` (no default), `prod_color` (no default), and `prod_status` (default `1`), `prod_price` (default `0`), etc.

```sql
INSERT INTO products (prod_description, prod_color)
VALUES ('My New Product', 'Red');
```

- In this case, `prod_status`, `prod_price`, and any other columns with default values will be automatically populated by the database's predefined defaults.

**Bulk Inserting into Specific Columns:**

You can also combine bulk inserts with specifying columns:

```sql
INSERT INTO products (prod_description, prod_color)
VALUES
    ('Product A', 'Blue'),
    ('Product B', 'Green'),
    ('Product C', 'Yellow');
```

## Important Considerations

- **Explicit Column Listing**: Always explicitly list the columns in your `INSERT` statement (`INSERT INTO table_name (column1, column2, ...)`) rather than omitting the column list.
  - **Why?**: If you omit the column list (`INSERT INTO table_name VALUES (value1, value2, ...)`), the database expects you to provide a value for _every_ column in the table, in the exact order they were defined. If the table structure changes (e.g., a new column is added), your query will break. Explicitly listing columns makes your `INSERT` statements more robust and maintainable.
- **Data Types**: Ensure the values you provide match the data type of the corresponding columns (e.g., strings in quotes, numbers without quotes).
