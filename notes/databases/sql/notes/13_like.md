# Text Searches with the `LIKE` Clause in SQL

The `LIKE` clause in SQL is used for pattern matching within text data. Unlike the `=` operator, which requires an exact match, `LIKE` allows you to search for values that partially match a specified pattern using **wildcard characters**. This is incredibly useful for implementing search functionalities, similar to what you'd find in any system.

## Basic Syntax

The `LIKE` clause is used within the `WHERE` clause:

```sql
SELECT column1, column2
FROM TableName
WHERE text_column LIKE 'pattern';
```

## Wildcard Character: The Percentage Sign (`%`)

The primary wildcard character used with `LIKE` in SQL (specifically MySQL, as discussed in the lesson) is the **percentage sign (`%`)**.

- **`%` (Percentage Sign)**: Represents zero, one, or multiple characters.

  - **`'pattern%'`**: Matches any string that **starts with** 'pattern'.
    - Example: `LIKE 'tarugo%'` would find 'tarugo', 'tarugoA', 'tarugo_green', etc.
  - **`'%pattern'`**: Matches any string that **ends with** 'pattern'.
    - Example: `LIKE '%tarugo'` would find 'A_tarugo', 'new_tarugo', 'tarugo', etc.
  - **`'%pattern%'`**: Matches any string that **contains** 'pattern' anywhere within the string. This is the most common use case for general text searches.
    - Example: `LIKE '%tarugo%'` would find 'red_tarugo_long', 'short_tarugo', 'tarugo', etc.

**Example**: Searching for products where the description contains the word "tarugo":

```sql
SELECT prod_ID, prod_description, prod_color, prod_price
FROM products P
WHERE P.prod_description LIKE '%tarugo%';
```

## Searching Across Multiple Columns

You can extend your search to multiple columns using `OR` conditions or by concatenating columns.

1.  **Using `OR`**:
    You can search for a pattern in one column **OR** another column.

    ```sql
    SELECT prod_ID, prod_description, prod_color, prod_price
    FROM products P
    WHERE P.prod_description LIKE '%negro%' OR P.prod_color LIKE '%negro%';
    ```

    This query would find products where "negro" is in the description OR in the color field.

2.  **Using `CONCAT()` for Combined Search**:
    The `CONCAT()` function allows you to combine multiple text columns into a single string, and then apply the `LIKE` clause to the concatenated result. This is often more efficient than multiple `OR` conditions for a single search term.
    ```sql
    SELECT prod_ID, prod_description, prod_color, prod_price
    FROM products P
    WHERE CONCAT(P.prod_description, ' ', P.prod_color) LIKE '%negro%';
    ```
    - **Explanation**: `CONCAT(P.prod_description, ' ', P.prod_color)` joins the description and color fields into one string (a space can be added between them for readability, though not strictly necessary for simple `%pattern%` searches). The `LIKE '%negro%'` is then applied to this combined string, finding "negro" whether it's in the description or the color.
