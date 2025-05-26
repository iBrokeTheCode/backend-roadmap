# The Importance of Indexes in Databases

Indexes are a fundamental concept in database management, crucial for the efficient retrieval of data. Without them, working with large databases would be impractically slow. Think of an index in a book: you don't read the entire book to find a specific topic; instead, you go to the index, find the topic and its corresponding page number, and then directly navigate to that page. Database indexes work similarly.

When you have a table with thousands or millions of records (like a customer table with $2,418$ clients, or even $1$ million), and you want to find a specific record (e.g., client ID $18$), a database without an index would have to read every single record until it finds the one you're looking for. This process is incredibly slow, especially with large datasets. Indexes allow the database to quickly locate specific records based on your search criteria, similar to how a book index provides a direct path to information.

Therefore, when designing a database table, it's essential to consider what types of searches will be performed on it and which fields will be used for filtering. These are the fields that should have indexes.

## Types of Indexes in MySQL

There are three main types of indexes:

- **Primary Key (`PRIMARY KEY`)**:

  - This is the most important type of index.
  - Every table **should** have a primary key, usually the table's ID field (e.g., `product_ID`, `client_ID`).
  - It's represented by a **_orange key icon_**.
  - **Characteristic**: The data in a primary key field can **never be duplicated**. Each value must be unique. If you try to insert a record with a primary key that already exists, the system will prevent it.

- **Key (Non-Unique Index)**:

  - These are general indexes that **can contain duplicate values**.
  - It's represented by a **_green key icon_**.
  - **Use case**: Ideal for fields where repetition is expected but you still need fast lookups. For example, in a `sales` table, a `client_ID` field (referencing the `client` table's primary key) would be a non-unique index because a single client can have multiple sales records. When you filter by `client_ID`, the database uses this index to quickly find all sales for that client.

- **Unique Index (`UNIQUE`)**:

  - Similar to a primary key in that it **does not allow duplicate values**.
  - However, it's **not the primary key** of the table. A table can have multiple unique indexes but only one primary key.
  - **Use case**: For fields that need to be unique but are not the main identifier for the record.

- **Fulltext Index (`FULLTEXT`)**:
  - Used specifically with `TEXT` data types (`TEXT`, `MEDIUMTEXT`, `LONGTEXT`).
  - Facilitates complex text searches.
  - **Note**: The speaker indicates this type of index requires special handling and is not as commonly used as the other three.

## Best Practices for Indexing

Choosing which fields to index is critical for database performance.

- **Fields to Index**:

  - **IDs**: Any foreign key fields (e.g., `cli_ID` in a `sales` table referencing the `client` table).
  - **Dates**: If you frequently query data within date ranges (e.g., "sales between X and Y date"), the date field should be indexed.

- **Fields to **Avoid** Indexing**:
  - **Amounts/Monetary Values**: Generally, these should not be indexed.
  - **Fields with Few Possible Values**: If a field only has two possible values (e.g., `status` with $0$ or $1$), an index is usually not beneficial.
    - **Rule of Thumb**: An index is most effective when the query result represents **less than $10\%$** of the total records in the table. For instance, searching for a specific client ID in a table of $2,400$ clients ($1$ record out of $2,400$) is highly optimized by an index. However, if $60\%$ of your records have a '1' status and $40\%$ have a '0' status, the database might spend more resources using the index than simply scanning the table.
