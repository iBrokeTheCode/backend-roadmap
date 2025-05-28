# MySQL Data Types: A Comprehensive Guide

Choosing the correct data type for your fields in MySQL is crucial for efficient database performance, optimizing disk space, and memory usage. This tutorial emphasizes precision in data type selection to avoid resource wastage and improve overall system performance.

## 1. Numeric Data Types

Numeric types are used for storing numerical values. It's vital to select the smallest possible data type that can accommodate your expected data range.

- **Integer Types:**

  - **`TINYINT`**: Stores very small integers.
    - Range: $-128$ to $127$ (signed) or $0$ to $255$ (unsigned).
    - Space: $1$ byte.
    - **Use case**: Ideal for storing values like country IDs (up to 255 countries).
  - **`SMALLINT`**: For slightly larger integers.
    - Range: Up to $65,535$ (unsigned).
    - **Use case**: Suitable for quantities like the number of localities in a country if the count is within its range.
  - **`MEDIUMINT`**: For medium-sized integers.
    - Range: $-8,388,608$ to $8,388,607$ (signed) or $0$ to $16,777,215$ (unsigned).
    - **Use case**: Good for product IDs if you expect millions of products.
  - **`INT`**: A commonly used integer type.
    - Range: Up to approximately $4.2$ billion (unsigned).
    - **Caution**: Avoid using `INT` by default for all integer fields. This is a common programming mistake that wastes $4$ bytes per entry when a smaller type could suffice.
  - **`BIGINT`**: For extremely large integers.
    - Range: Very large numbers (up to $18$ quintillion unsigned).
  - **`BIT`**: The smallest integer type.
    - Range: $0$ to $64$.
    - **Caution**: Not recommended due to compatibility issues with some programming languages and drivers. Use `TINYINT` instead if you need the smallest possible integer.

- **Decimal/Real Types:**
  - **`FLOAT`**: Stores single-precision floating-point numbers.
  - **`DOUBLE`**: Stores double-precision floating-point numbers.
  - **`DECIMAL`**: Used for exact decimal values, often for financial data.
    - Allows you to specify the total number of digits and the number of decimal places (e.g., `DECIMAL(10, 2)` for prices with $10$ total digits, $2$ of which are decimal).
    - Can be signed or unsigned, doubling the positive range if unsigned.

## 2. Text/String Data Types

These types store alphanumeric characters.

- **`CHAR`**: Stores a **fixed-length** string.

  - If you define `CHAR(20)` and store "Hola", it will still occupy $20$ characters (4 for "Hola" + 16 empty spaces).
  - **Advantage**: Faster for searches than `VARCHAR` due to fixed length.
  - **Use case**: Ideal for fields where the length is always constant (e.g., passwords, tokens).

- **`VARCHAR`**: Stores a **variable-length** string.

  - Occupies only the space needed for the stored data. "Hola" in `VARCHAR(20)` will only take $4$ bytes.
  - **Caution**: Avoid setting excessively large maximum lengths (e.g., `VARCHAR(65000)`) just to be safe.
    - **Reason 1**: Gives a misleading idea of the data's typical length.
    - **Reason 2**: The database engine reserves the _maximum declared capacity_ in memory (cache/buffer), not just the actual data length, which can negatively impact performance and consume excessive memory.
  - It's best practice to set a reasonable maximum length, perhaps slightly larger than your expected typical length, but not excessively so.

- **`TEXT` Types**: For storing large amounts of text. Generally, prefer `VARCHAR` unless absolutely necessary due to length constraints.
  - **`TINYTEXT`**: Up to $255$ characters. (Trainer advises using `VARCHAR` instead).
  - **`TEXT`**: Up to $65,535$ characters. (Trainer advises using `VARCHAR` in newer MySQL versions).
  - **`MEDIUMTEXT`**: Up to $16$ million characters.
  - **`LONGTEXT`**: Up to $4$ GB of data.
    - **Use case**: For extremely large texts, like patient clinical histories.

## 3. Date and Time Data Types

Used for storing temporal information.

- **`DATE`**: Stores only the date (e.g., 'YYYY-MM-DD').
- **`TIME`**: Stores only the time (e.g., 'HH:MM:SS').
- **`YEAR`**: Stores a year. (Trainer rarely uses this, prefers a numeric field).
- **`DATETIME`**: Stores both date and time (e.g., 'YYYY-MM-DD HH:MM:SS').
  - **Use case**: Useful for recording creation timestamps (e.g., sale date and time).
- **`TIMESTAMP`**: Similar to `DATETIME` but stores the time in Unix format.
  - Different manipulation characteristics compared to `DATETIME`.

## 4. Binary Data Types

Used for storing binary data like images or documents.

- **`BINARY`**: Fixed-length binary string.
- **`VARBINARY`**: Variable-length binary string.
- **`BLOB` types**: Equivalent to `TEXT` types but for binary data.
  - **`TINYBLOB`**: Up to $255$ bytes.
  - **`BLOB`**: Up to $65,535$ bytes.
  - **`MEDIUMBLOB`**: Up to $16$ MB.
  - **`LONGBLOB`**: Up to $4$ GB.
  - **Use case**: Storing scanned documents or images directly in the database.

## 5. Other Data Types

- **`JSON`**: Introduced in MySQL 5.7, gained prominence in MySQL 8.0. Allows storing and querying JSON documents.
- **`UUID` (Universal Unique Identifier)**: A unique, non-repeating identifier.
  - Often used for IDs in modern systems (e.g., product IDs, user IDs).
  - Trainer prefers auto-incrementing numeric IDs for faster searches and easier ordering.
- **Geometry Types**: For geographical or geometric data (points, lines, polygons). Rarely used in typical business applications.
- **`ENUM`**: Allows a field to have one value from a predefined list of strings (e.g., 'Yes', 'No'). Provides data validation at the database level.
- **`SET`**: Similar to `ENUM`, but allows a field to have multiple values from a predefined list of integers.
