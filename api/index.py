from flask import Flask, request, jsonify
from crypto import encrypt_text, decrypt_text

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Flask Encryption API is running",
        "endpoints": {
            "encrypt": "/encrypt",
            "decrypt": "/decrypt"
        }
    })


@app.route("/encrypt", methods=["POST"])
def encrypt():
    data = request.get_json()

    plaintext = data.get("plaintext", "")
    seed = data.get("seed")

    if plaintext == "" or seed is None:
        return jsonify({"error": "plaintext dan seed wajib diisi"}), 400

    ciphertext = encrypt_text(plaintext, int(seed))
    return jsonify({"ciphertext": ciphertext})


@app.route("/decrypt", methods=["POST"])
def decrypt():
    data = request.get_json()

    ciphertext = data.get("ciphertext", "")
    seed = data.get("seed")

    if ciphertext == "" or seed is None:
        return jsonify({"error": "ciphertext dan seed wajib diisi"}), 400

    plaintext = decrypt_text(ciphertext, int(seed))
    return jsonify({"plaintext": plaintext})

if __name__ == "__main__":
    app.run(debug=True)

