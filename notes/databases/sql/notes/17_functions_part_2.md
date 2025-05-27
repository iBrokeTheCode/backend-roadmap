# Functions in SQL (Part 2)

This lesson continues our exploration of SQL functions, focusing on date and time manipulation, data type conversion, string length, and other utility functions.

## 1. Date and Time Functions

These functions are essential for working with dates and times, allowing you to add, subtract, and format date/time values.

- **`ADDDATE()`**: Adds a specified number of days to a date.

  - **Syntax**: `ADDDATE(date, INTERVAL value unit)` or `ADDDATE(date, days_to_add)`
  - **Example**: Adding 10 days to the current date:
    ```sql
    SELECT ADDDATE(CURRENT_DATE(), INTERVAL 10 DAY) AS future_date;
    -- Or simply: SELECT ADDDATE(CURRENT_DATE(), 10) AS future_date;
    ```
  - **Note**: `ADDDATE()` primarily focuses on adding days, though it can use `INTERVAL` for other units.

- **`ADDTIME()`**: Adds a specified time value to a time or datetime.

  - **Syntax**: `ADDTIME(time_or_datetime, time_to_add)`
  - **Example**: Adding 15 minutes to the current timestamp:
    ```sql
    SELECT ADDTIME(CURRENT_TIMESTAMP(), '00:15:00') AS time_plus_15_mins;
    ```

- **`DATE_ADD()`**: A more versatile function for adding intervals (days, months, years, etc.) to a date.

  - **Syntax**: `DATE_ADD(date, INTERVAL value unit)`
  - **`unit` options**: `DAY`, `MONTH`, `YEAR`, `HOUR`, `MINUTE`, `SECOND`, etc.
  - **Example**: Adding 10 months to the current date:
    ```sql
    SELECT DATE_ADD(CURRENT_DATE(), INTERVAL 10 MONTH) AS date_plus_10_months;
    ```
  - **Example**: Adding 10 years to the current date:
    ```sql
    SELECT DATE_ADD(CURRENT_DATE(), INTERVAL 10 YEAR) AS date_plus_10_years;
    ```

- **`DATE_SUB()`**: The inverse of `DATE_ADD()`, used to subtract intervals from a date.

  - **Syntax**: `DATE_SUB(date, INTERVAL value unit)`
  - **Example**: Subtracting 10 days from the current date:
    ```sql
    SELECT DATE_SUB(CURRENT_DATE(), INTERVAL 10 DAY) AS date_minus_10_days;
    ```

- **`DATE_FORMAT()`**: Formats a date or datetime value into a string based on a specified format.
  - **Syntax**: `DATE_FORMAT(date, format_string)`
  - **`format_string`**: Uses `%` placeholders for different date/time components (e.g., `%Y` for 4-digit year, `%m` for 2-digit month, `%d` for day of month, `%W` for full weekday name, `%M` for full month name, `%H` for hour (24-hour), `%i` for minutes, `%s` for seconds).
  - **Example**: Displaying a date as "August 21, 2023 (Monday)":
    ```sql
    SELECT DATE_FORMAT('2023-08-21', '%M %d, %Y (%W)') AS formatted_date;
    ```

## 2. Data Type Conversion Function: `CAST()`

The `CAST()` function converts a value from one data type to another.

- **Syntax**: `CAST(expression AS data_type)`
- **Common `data_type`s**: `CHAR`, `DATE`, `DATETIME`, `SIGNED INTEGER`, `DECIMAL`, etc.
- **Example**: Converting a string to a date:
  ```sql
  SELECT CAST('2023-06-25' AS DATE) AS converted_date;
  ```
- **Example**: Converting a number to a character string:
  ```sql
  SELECT CAST(12345 AS CHAR) AS number_as_text;
  ```
  This allows you to then apply string functions (like `SUBSTRING`) to the numeric value.

## 3. String Functions

- **`CHAR_LENGTH()`**: Returns the length of a string in characters. (Note: `LENGTH()` returns length in bytes, which can differ for multi-byte character sets).

  - **Syntax**: `CHAR_LENGTH(string)`
  - **Example**: Getting the length of product descriptions:
    ```sql
    SELECT P.prod_ID, P.prod_description, CHAR_LENGTH(P.prod_description) AS description_length
    FROM products P;
    ```

- **`COMPRESS()`**: Compresses a string.

  - **Syntax**: `COMPRESS(string)`
  - **Use Case**: Can be used to save storage space for large text fields.
  - **Caution**: Data stored compressed cannot be directly searched using `LIKE` or other string functions without first decompressing it.
  - **Example**:
    ```sql
    SELECT COMPRESS(P.prod_description) AS compressed_description
    FROM products P;
    ```

- **`UNCOMPRESS()`**: Decompresses a string that was compressed with `COMPRESS()`.

  - **Syntax**: `UNCOMPRESS(compressed_string)`
  - **Example**:
    ```sql
    SELECT UNCOMPRESS(COMPRESS(P.prod_description)) AS original_description
    FROM products P;
    ```

- **`CONCAT()`**: Concatenates (joins) two or more strings together.

  - **Syntax**: `CONCAT(string1, string2, ...)`
  - **Example**: Combining product ID, description, and color:
    ```sql
    SELECT CONCAT('(', P.prod_ID, ') ', P.prod_description, ' ', P.prod_color) AS full_product_info
    FROM products P;
    ```

- **`CONCAT_WS()`**: Concatenates strings with a specified separator.
  - **Syntax**: `CONCAT_WS(separator, string1, string2, ...)`
  - **Example**: Concatenating description and color with a space as a separator:
    ```sql
    SELECT CONCAT_WS(' ', P.prod_description, P.prod_color) AS description_and_color
    FROM products P;
    ```

## 4. Numeric Conversion Function: `CONV()`

The `CONV()` function converts a number from one numeric base to another.

- **Syntax**: `CONV(N, from_base, to_base)`
  - `N`: The number to convert.
  - `from_base`: The base of the input number.
  - `to_base`: The base to convert the number to.
- **Example**: Converting decimal 10 to binary (base 2):
  ```sql
  SELECT CONV(10, 10, 2) AS decimal_to_binary; -- Result: '1010'
  ```
- **Example**: Converting hexadecimal 'A' (which is 10 in decimal) to decimal (base 10):
  ```sql
  SELECT CONV('A', 16, 10) AS hex_to_decimal; -- Result: '10'
  ```
