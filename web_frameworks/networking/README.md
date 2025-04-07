# Networking Fundamentals for Web Devs

## 1. HTTP/HTTPS (Hypertext Transfer Protocol/Secure):

**Theory:**

- HTTP is the foundation of data communication for the World Wide Web. It's an application-layer protocol that defines how messages are formatted and transmitted.
- HTTPS is the secure version of HTTP. It encrypts the communication using SSL/TLS, ensuring data privacy and integrity.
- **HTTP:** Unencrypted, data is sent in plain text.
- **HTTPS:** Encrypted, data is secured using SSL/TLS certificates.

**Importance:**

- Essential for understanding how web browsers and servers interact.
- HTTPS is crucial for secure data transmission, especially for sensitive information like passwords and credit card details.

## 2. Request/Response Cycle

**Theory:**

- The core communication model in web development.
- A client (e.g., web browser) sends an HTTP request to a server.
- The server processes the request and sends back an HTTP response.
- **Request:** Contains information about what the client wants (e.g., a web page, data).
- **Response:** Contains the requested data and information about the server's processing.

**Components:**

- **Request:**

  - **Method:** (GET, POST, PUT, DELETE, etc.) Defines the action the client wants to perform.
  - **URL:** (Uniform Resource Locator) Specifies the resource being requested.
  - **Headers:** Additional information about the request (e.g., user-agent, content type).
  - **Body:** (Optional) Contains data sent to the server (e.g., form data).

- **Response:**

  - **Status Code:** (e.g., 200 OK, 404 Not Found, 500 Internal Server Error) Indicates the result of the request.
  - **Headers:** Additional information about the response (e.g., content type, server).
  - **Body:** (Optional) Contains the requested data (e.g., HTML, JSON).

## 3. Status Codes:

**Theory:**

- Three-digit codes that indicate the status of an HTTP response.
- Essential for client-side error handling and server-side logging.

**Common Codes:**

- **2xx (Success):**
  - **200 OK:** Request succeeded.
  - **201 Created:** Resource created successfully.
- **3xx (Redirection):**
  - **301 Moved Permanently:** Resource moved to a new URL.
  - **302 Found:** Resource temporarily moved.
- **4xx (Client Error):**
  - **400 Bad Request:** Invalid request syntax.
  - **401 Unauthorized:** Authentication required.
  - **403 Forbidden:** Server refuses to authorize the request.
  - **404 Not Found:** Resource not found.
- **5xx (Server Error):**
  - **500 Internal Server Error:** Server encountered an error.
  - **503 Service Unavailable:** Server temporarily unavailable.

## 4. DNS Basics (Domain Name System):

**Theory:**

- Translates domain names (e.g., google.com) into IP addresses (e.g., 172.217.160.142).
- Allows users to access websites using human-readable names instead of IP addresses.

**Process:**

- Browser requests the IP address from a DNS resolver.
- Resolver queries DNS servers until it finds the IP address.
- Resolver returns the IP address to the browser.

See [Notes](./notes.md)
