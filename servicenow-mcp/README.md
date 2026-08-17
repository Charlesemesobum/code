# servicenow-mcp

MCP server exposing ServiceNow CMDB/CI operations as tools, backed by the
ServiceNow Table API with basic auth.

## Setup

```bash
cd servicenow-mcp
python -m venv .venv && source .venv/bin/activate
pip install -e .
```

Set credentials via environment variables:

```bash
export SN_INSTANCE=your-instance   # or a full URL, e.g. https://your-instance.service-now.com
export SN_USERNAME=your-username
export SN_PASSWORD=your-password
```

## Run

```bash
servicenow-mcp
```

Or point an MCP client (e.g. Claude Code) at it directly:

```json
{
  "mcpServers": {
    "servicenow": {
      "command": "servicenow-mcp",
      "env": {
        "SN_INSTANCE": "your-instance",
        "SN_USERNAME": "your-username",
        "SN_PASSWORD": "your-password"
      }
    }
  }
}
```

## Tools

- `search_cis(query, table="cmdb_ci", limit=10)` — search CIs by name.
- `get_ci(sys_id, table="cmdb_ci")` — fetch a single CI.
- `query_cis(table="cmdb_ci", sysparm_query="", fields="", limit=10)` — raw encoded query.
- `create_ci(table, fields)` — create a CI.
- `update_ci(sys_id, fields, table="cmdb_ci")` — update a CI.
