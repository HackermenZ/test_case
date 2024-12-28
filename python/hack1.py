import requests

def get_express_versions():
    url = "https://api.deps.dev/v3alpha/systems/npm/packages/express/versions"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        versions = [version['version'] for version in data['versions']]
        return versions
    else:
        print(f"Failed to fetch versions: {response.status_code}")
        return []

versions = get_express_versions()
print(", ".join(versions))
