import requests

url = "https://example.com"

response = requests.get(url)

print("Status Code:", response.status_code)
print()
print(response.text[:500])