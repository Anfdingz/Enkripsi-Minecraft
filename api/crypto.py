# crypto.py
blocks = [
    "STE", "GRS", "DIT", "COE", "OAK",
    "OAG", "BEK", "FLR", "STR",
    "FLA", "STA", "SAD", "GRL", "GOE",
    "IRE", "CAE", "OAD", "OAS", "SPE",
    "GLS", "LAE", "LAK", "DIR",
    "SAE", "NOK", "BED"
]

colors = [
    "&8", "&10", "&4", "&7", "&14", "&6", "&8", "&9", "&1",
    "&13", "&4", "&14", "&7", "&6", "&15", "&0", "&6",
    "&10", "&14", "&15", "&1", "&9", "&7", "&14", "&6", "&13"
]

def encrypt_text(plaintext, seed):
    plaintext = plaintext.upper()
    cipher = ""
    for ch in plaintext:
        if ch.isalpha():
            block_id = ord(ch) - ord('A') + 1
            new_id = (block_id - 1 + seed) % 26 + 1
            cipher += colors[block_id - 1] + blocks[new_id - 1]
    return cipher

def decrypt_text(ciphertext, seed):
    plaintext = ""
    i = 0
    while i < len(ciphertext):
        if ciphertext[i] == "&":
            i += 1
            while i < len(ciphertext) and ciphertext[i].isdigit():
                i += 1
            block = ciphertext[i:i+3]
            i += 3
            block_id = blocks.index(block) + 1
            orig_id = (block_id - 1 - seed) % 26 + 1
            plaintext += chr(orig_id + ord('A') - 1)
        else:
            i += 1
    return plaintext
