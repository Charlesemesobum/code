import os

import httpx


class ServiceNowConfigError(RuntimeError):
    pass


class ServiceNowClient:
    def __init__(self) -> None:
        instance = os.environ.get("SN_INSTANCE")
        username = os.environ.get("SN_USERNAME")
        password = os.environ.get("SN_PASSWORD")

        if not instance or not username or not password:
            raise ServiceNowConfigError(
                "SN_INSTANCE, SN_USERNAME, and SN_PASSWORD environment "
                "variables must all be set."
            )

        if instance.startswith("http://") or instance.startswith("https://"):
            base_url = instance.rstrip("/")
        else:
            base_url = f"https://{instance}.service-now.com"

        self._client = httpx.AsyncClient(
            base_url=base_url,
            auth=(username, password),
            headers={"Accept": "application/json", "Content-Type": "application/json"},
            timeout=30.0,
        )

    async def aclose(self) -> None:
        await self._client.aclose()

    async def query_table(
        self,
        table: str,
        sysparm_query: str = "",
        fields: str = "",
        limit: int = 10,
    ) -> list[dict]:
        params = {"sysparm_limit": str(limit)}
        if sysparm_query:
            params["sysparm_query"] = sysparm_query
        if fields:
            params["sysparm_fields"] = fields

        response = await self._client.get(f"/api/now/table/{table}", params=params)
        response.raise_for_status()
        return response.json().get("result", [])

    async def get_record(self, table: str, sys_id: str, fields: str = "") -> dict:
        params = {}
        if fields:
            params["sysparm_fields"] = fields

        response = await self._client.get(
            f"/api/now/table/{table}/{sys_id}", params=params
        )
        response.raise_for_status()
        return response.json().get("result", {})

    async def create_record(self, table: str, fields: dict) -> dict:
        response = await self._client.post(f"/api/now/table/{table}", json=fields)
        response.raise_for_status()
        return response.json().get("result", {})

    async def update_record(self, table: str, sys_id: str, fields: dict) -> dict:
        response = await self._client.patch(
            f"/api/now/table/{table}/{sys_id}", json=fields
        )
        response.raise_for_status()
        return response.json().get("result", {})
