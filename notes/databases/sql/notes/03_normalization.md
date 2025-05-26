# Database Normalization: The Three Normal Forms

Database normalization is a set of rules and principles for designing database tables to minimize data redundancy and improve data integrity. These principles, developed by experts over many years, are essential for creating efficient and maintainable databases.

## 1. First Normal Form (1NF)

The First Normal Form (1NF) lays the groundwork for well-structured tables. It has four core principles:

- **Every table must have a unique Primary Key**: This is crucial for quickly accessing specific records. As discussed in the previous lesson, a primary key (e.g., `client_ID`, `product_ID`) ensures that each record is uniquely identifiable, allowing for lightning-fast data retrieval.
- **No repeating groups of data**: Avoid creating multiple columns for similar data within the same table (e.g., `phone1`, `phone2`, `phone3`). Instead, create a **separate, auxiliary table** to store these repeating values.
  - **Example**: For multiple phone numbers for a client, create a `Client_Phones` table with columns like `client_ID` (foreign key to the `Clients` table), `phone_ID` (primary key for this table), and `phone_Number`. This allows a client to have any number of phones without modifying the `Clients` table structure.
  - This also applies to other repeating data, such as social media accounts for users; create a `User_Social_Media` table.
- **Each column must contain atomic values**: This means each field should hold a single, indivisible piece of information.
  - **Example**: Instead of a `name` column holding "John Doe," separate it into `first_Name` and `last_Name` columns.
- **Each column in a row must have a single value for that row**: This reinforces the previous point.
  - **Example**: Avoid storing multiple child names in a single `children` field (e.g., "Alice, Bob, Carol"). If you need to record multiple children, create a separate `Client_Children` table.

## 2. Second Normal Form (2NF)

The Second Normal Form (2NF) builds upon 1NF and focuses on eliminating **partial dependencies**:

- **Every non-key column in a table must depend on the _entire_ primary key**: This means that all attributes in a table must be fully functionally dependent on the table's primary key.
  - **If the primary key is a single column**: All other columns in that table must directly describe or be related to that single primary key. For example, in a `Clients` table where `client_ID` is the primary key, all fields like `client_Name`, `client_Address`, etc., must describe that specific client. You shouldn't include product details or supplier details in the `Clients` table.
  - **If the primary key is a composite key (made of multiple columns)**: Every non-key column must depend on the _entire combination_ of columns that make up the primary key, not just a part of it.
    - **Example**: If you have a table `Product_Categories` with a composite primary key of `product_ID` and `category_ID`, any other field in that table (e.g., `relationship_Type`) must be relevant to the combination of _both_ the product and the category, not just the product or just the category.
  - **Common Exception in Practice (Denormalization)**: In real-world systems, especially in transactional tables like `Sale_Details` (which records individual items sold in a sale), you might see fields like `price` and `cost` duplicated from the `Products` table. While seemingly violating 2NF, this is a common and **accepted practice** called denormalization.
    - **Reason**: To maintain **historical accuracy**. The price and cost of a product can change over time. By duplicating these values at the moment of the sale, the `Sale_Details` record preserves the actual price and cost at which the transaction occurred, preventing inconsistencies if the product's price changes later in the `Products` table. This allows for accurate calculations of profit for past sales.

## 3. Third Normal Form (3NF)

The Third Normal Form (3NF) further refines table design by eliminating **transitive dependencies**:

- **A non-key column should not depend on another non-key column**: This means that information that doesn't directly relate to the primary key, but rather to another non-key attribute, should be moved to a separate table.
  - **Example**: Consider a `Products` table with `prod_ID` (primary key), `prod_Name`, `prod_Status_Code`, and `prod_Status_Description`. Here, `prod_Status_Description` depends on `prod_Status_Code`, which is a non-key field. This is a transitive dependency.
  - **Solution**: Create a separate `Product_Statuses` table with `status_ID` (primary key) and `status_Description`. Then, in the `Products` table, you would only have `prod_Status_Code` (as a foreign key referencing `status_ID`). This ensures that status descriptions are managed centrally and not duplicated across product records.
  - **Another Example**: In an `Employees` table, if you have `employee_ID`, `employee_Name`, `department_Name`, and `department_Manager`, the `department_Manager` depends on `department_Name` (a non-key field), not directly on `employee_ID`. This is a transitive dependency. To fix this, create a separate `Departments` table with `department_ID` (primary key), `department_Name`, and `department_Manager`. The `Employees` table would then only contain `department_ID` as a foreign key.

The goal of these normal forms is to create coherent and unambiguous tables where all non-key attributes are directly and solely dependent on the table's primary key, avoiding mixed entities and ensuring data integrity.
