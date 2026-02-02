---
name: mcp-builder
description: "Create robust Model Context Protocol (MCP) servers that enable Claude to interact with external tools and data sources. Use when: MCP server, tools protocol, Claude integration, custom tools, MCP implementation."
source: vibeship-spawner-skills (Apache 2.0)
---

# MCP Server Development Guide

As an MCP server developer, you help users create custom tools and data integrations for Claude. You understand the MCP specification, can build servers in TypeScript or Python, and know how to create effective tool interfaces.

## Key Principles

- Use the official MCP SDK (@modelcontextprotocol/sdk for TypeScript, mcp package for Python)
- Define clear, well-typed tool schemas
- Include proper context in responses
- Handle errors gracefully with informative messages
- Include comprehensive input validation
- Optimize for Claude's context window

## Before Writing Code

Research first:
1. Check official MCP documentation via Context7
2. Review integration requirements (APIs, data sources)
3. Identify scope and capabilities needed

## TypeScript Server Pattern

```typescript
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { ListToolsRequestSchema, CallToolRequestSchema } from "@modelcontextprotocol/sdk/types.js";

const server = new Server(
  { name: "my-server", version: "1.0.0" },
  { capabilities: { tools: {} } }
);

server.setRequestHandler(ListToolsRequestSchema, async () => ({
  tools: [{
    name: "my_tool",
    description: "Performs specific task",
    inputSchema: {
      type: "object",
      properties: {
        param: { type: "string", description: "Parameter description" }
      },
      required: ["param"]
    }
  }]
}));

server.setRequestHandler(CallToolRequestSchema, async (request) => {
  if (request.params.name === "my_tool") {
    const { param } = request.params.arguments;
    return { content: [{ type: "text", text: `Result: ${param}` }] };
  }
  throw new Error(`Unknown tool: ${request.params.name}`);
});

const transport = new StdioServerTransport();
await server.connect(transport);
```

## Python Server Pattern

```python
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

server = Server("my-server")

@server.list_tools()
async def list_tools():
    return [Tool(
        name="my_tool",
        description="Performs specific task",
        inputSchema={
            "type": "object",
            "properties": {
                "param": {"type": "string", "description": "Parameter"}
            },
            "required": ["param"]
        }
    )]

@server.call_tool()
async def call_tool(name: str, arguments: dict):
    if name == "my_tool":
        return [TextContent(type="text", text=f"Result: {arguments['param']}")]
    raise ValueError(f"Unknown tool: {name}")

async def main():
    async with stdio_server() as (read_stream, write_stream):
        await server.run(read_stream, write_stream, server.create_initialization_options())

import asyncio
asyncio.run(main())
```

## Tool Design Best Practices

1. **Clear Names**: Use snake_case, be descriptive
2. **Detailed Descriptions**: Explain purpose and return value
3. **Typed Parameters**: Include type and description for each
4. **Error Handling**: Return clear error messages
5. **Focused Scope**: One clear purpose per tool

## Testing Your Server

1. Run server locally
2. Use MCP Inspector to test tools
3. Verify with real Claude integration
4. Check error handling edge cases
