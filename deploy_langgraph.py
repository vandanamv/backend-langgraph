# deploy_langgraph.py
import os
import requests
import json

api_key = os.environ["LANGCHAIN_API_KEY"]
image = os.environ["IMAGE"]

# Replace this with your real API endpoint once available
api_url = "https://api.langgraph.run/deploy"

payload = {"image": image, "service_name": "langgraph-backend"}
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

print("🚀 Triggering deployment to LangGraph Platform...")
response = requests.post(api_url, headers=headers, data=json.dumps(payload))
print("Status:", response.status_code)
print("Response:", response.text)
