# MCP

## Resources

- [Model Context Protocol](https://modelcontextprotocol.io/introduction) - MCP is an open protocol that standardizes how applications provide context to LLMs.
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) - Python implementation of the Model Context Protocol (MCP)
- [Learn MCP! For Beginners + Create Our First MCP From Scratch”](https://youtu.be/wnHczxwukYY?si=xzHYAwOUO5ukOXoW) - YouTube tutorial by Midudev
- [MCP so](https://mcp.so/) - Find Awesome MCP Servers and Clients
- [Outerbase](https://www.outerbase.com/) - Databases client

- [MCP Crash Course for Python Developers - GitHub Repository](https://youtu.be/5xqFjh56AwM?si=p87Uj1glgKlvbHau)
- [MCP Crash Course for Python Developers - YouTube Tutorial](https://github.com/daveebbelaar/ai-cookbook/tree/main/mcp/crash-course)

## Steps

- Enable Agent mode in VSCode `Chat Agent Enabled`

- Follow the basic example from [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)

  ```shell
  # Create project with uv
  uv init mcp-server-demo
  cd mcp-server-demo

  # Add MCP to dependencies
  uv add "mcp[cli]"

  # Run the mcp command with uv
  uv run mcp

  # Install in Claude Desktop
  mcp install server.py

  # Test with MCP Inspector
  mcp dev server.py
  ```

- Create a simple MCP server that exposes a calculator tool and some data:

  ```py
  # server.py
  from mcp.server.fastmcp import FastMCP

  # Create an MCP server
  mcp = FastMCP("Demo")


  # Add an addition tool
  @mcp.tool()
  def add(a: int, b: int) -> int:
      """Add two numbers"""
      return a + b


  # Add a dynamic greeting resource
  @mcp.resource("greeting://{name}")
  def get_greeting(name: str) -> str:
      """Get a personalized greeting"""
      return f"Hello, {name}!"
  ```

- Go to VSCode and in your `settings.json` file add your MCP

  ```json
  {
    "mcp": {
      "servers": {
        "add": {
          "command": "uv",
          "args": [
            "run",
            "--with",
            "mcp[cli]",
            "mcp",
            "run",
            "/ABSOLUTE_PATH/script.py"
          ]
        }
      }
    }
  }
  ```
