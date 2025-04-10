# Notes

## Exercises

1. **HTTP Request/Response Exploration:**

   a. Use your browser's developer tools (Network tab) to inspect HTTP requests and responses when visiting websites.
   b. Observe the request methods, URLs, headers, and status codes.

   - Press `Ctrl + Shift + I` or `F12` to Inspect
   - Select Network tab
   - Select any resource and view Headers, Response, etc.

2. **Status Code Experimentation:**

   a. Try accessing non-existent URLs to observe 404 Not Found errors.
   b. Research and experiment with other HTTP status codes.

   - `https://www.python.org/static/stylesheets/style.08a078d0aa02.csss` returns an 404 error
   - `https://www.python.org/static/stylesheets/style.08a078d0aa02.css` returns the css file

3. **DNS Lookup:**

   a. Use the `nslookup` or `dig` command-line tools to perform DNS lookups for various domain names.
   b. Example: `nslookup google.com`

   - `nslookup google.com` displays addresses (IPv4 and IPv6) and name (google.com)
   - `dig google.com` displays similar information, in this case only the IPv4 addresses

4. **HTTP Client:**

   a. Use a tool like `curl` or `httpie` to make HTTP requests from the command line.
   b. Example: `curl https://www.example.com`

   - `curl https://www.google.com` returns the HTML code.
