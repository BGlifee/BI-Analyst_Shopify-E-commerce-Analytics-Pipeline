import requests


def shopify_graphql_request(store_url: str, api_version: str, access_token: str, query: str, variables: dict | None = None) -> dict:
    url = f"https://{store_url}/admin/api/{api_version}/graphql.json"
    headers = {
        "Content-Type": "application/json",
        "X-Shopify-Access-Token": access_token,
    }

    payload = {
        "query": query,
        "variables": variables or {}
    }

    response = requests.post(url, headers=headers, json=payload, timeout=30)
    response.raise_for_status()
    return response.json()