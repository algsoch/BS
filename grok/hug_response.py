import requests

HF_API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-v0.1"
HF_HEADERS = {"Authorization": "Bearer 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"}  # Replace with your key

response = requests.post(HF_API_URL, headers=HF_HEADERS, json={"inputs": "Hello, how are you?"})

print("Response Code:", response.status_code)
print("Response Text:", response.text)
