# index.py
from crypto import encrypt_text, decrypt_text
import json

def handler(request):
    try:
        path = request.get("path", "/")
        method = request.get("method", "GET")
        body = request.get("body", {})

        if path == "/" and method == "GET":
            return {
                "statusCode": 200,
                "headers": {"Content-Type": "application/json"},
                "body": json.dumps({
                    "message": "Python Encryption API is running",
                    "endpoints": {
                        "encrypt": "/encrypt",
                        "decrypt": "/decrypt"
                    }
                })
            }

        elif path == "/encrypt" and method == "POST":
            plaintext = body.get("plaintext", "")
            seed = body.get("seed")

            if plaintext == "" or seed is None:
                return {"statusCode": 400, "body": json.dumps({"error": "plaintext dan seed wajib diisi"})}

            ciphertext = encrypt_text(plaintext, int(seed))
            return {"statusCode": 200, "body": json.dumps({"ciphertext": ciphertext})}

        elif path == "/decrypt" and method == "POST":
            ciphertext = body.get("ciphertext", "")
            seed = body.get("seed")

            if ciphertext == "" or seed is None:
                return {"statusCode": 400, "body": json.dumps({"error": "ciphertext dan seed wajib diisi"})}

            plaintext = decrypt_text(ciphertext, int(seed))
            return {"statusCode": 200, "body": json.dumps({"plaintext": plaintext})}

        else:
            return {"statusCode": 404, "body": json.dumps({"error": "endpoint tidak ditemukan"})}

    except Exception as e:
        return {"statusCode": 500, "body": json.dumps({"error": str(e)})}
