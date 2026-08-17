from mcp.server.fastmcp import FastMCP

from servicenow_mcp.client import ServiceNowClient

mcp = FastMCP("servicenow-mcp")

_client: ServiceNowClient | None = None


def _get_client() -> ServiceNowClient:
    global _client
    if _client is None:
        _client = ServiceNowClient()
    return _client


@mcp.tool()
async def search_cis(query: str, table: str = "cmdb_ci", limit: int = 10) -> list[dict]:
    """Search Configuration Items by name.

    Args:
        query: Text to match against the CI name (case-insensitive substring).
        table: CMDB table to search (defaults to the base cmdb_ci table;
            use a subclass like cmdb_ci_server for more specific results).
        limit: Maximum number of records to return.
    """
    sysparm_query = f"nameLIKE{query}"
    return await _get_client().query_table(table, sysparm_query=sysparm_query, limit=limit)


@mcp.tool()
async def get_ci(sys_id: str, table: str = "cmdb_ci") -> dict:
    """Fetch a single Configuration Item by its sys_id.

    Args:
        sys_id: The sys_id of the CI record.
        table: CMDB table the record belongs to.
    """
    return await _get_client().get_record(table, sys_id)


@mcp.tool()
async def query_cis(
    table: str = "cmdb_ci",
    sysparm_query: str = "",
    fields: str = "",
    limit: int = 10,
) -> list[dict]:
    """Run a raw encoded query against a CMDB table.

    Args:
        table: CMDB table to query.
        sysparm_query: ServiceNow encoded query string (e.g. "operational_status=1^install_status=1").
        fields: Comma-separated list of fields to return; empty returns all fields.
        limit: Maximum number of records to return.
    """
    return await _get_client().query_table(
        table, sysparm_query=sysparm_query, fields=fields, limit=limit
    )


@mcp.tool()
async def create_ci(table: str, fields: dict) -> dict:
    """Create a new Configuration Item.

    Args:
        table: CMDB table to insert into (e.g. cmdb_ci_server).
        fields: Field name/value pairs for the new record.
    """
    return await _get_client().create_record(table, fields)


@mcp.tool()
async def update_ci(sys_id: str, fields: dict, table: str = "cmdb_ci") -> dict:
    """Update an existing Configuration Item.

    Args:
        sys_id: The sys_id of the CI record to update.
        fields: Field name/value pairs to update.
        table: CMDB table the record belongs to.
    """
    return await _get_client().update_record(table, sys_id, fields)


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()
