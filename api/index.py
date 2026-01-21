from .crypto import encrypt_text, decrypt_text
import json

def handler(request):
    path = request.get("path", "/")
    method = request.get("method", "GET")
    body = request.get("body", {})

    if path == "/" and method == "GET":
        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"message": "API is running"})
        }

    elif path == "/encrypt" and method == "POST":
        plaintext = body.get("plaintext", "")
        seed = body.get("seed", 0)
        ciphertext = encrypt_text(plaintext, int(seed))
        return {"statusCode": 200, "body": json.dumps({"ciphertext": ciphertext})}

    elif path == "/decrypt" and method == "POST":
        ciphertext = body.get("ciphertext", "")
        seed = body.get("seed", 0)
        plaintext = decrypt_text(ciphertext, int(seed))
        return {"statusCode": 200, "body": json.dumps({"plaintext": plaintext})}

    return {"statusCode": 404, "body": json.dumps({"error": "endpoint not found"})}
