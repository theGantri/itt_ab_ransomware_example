import typer
import os

app = typer.Typer()

def encrypt_file(file: str):
    file_data_to_encrypt = open(file, "rb").read()
    file_size = len(file_data_to_encrypt)
    key = os.urandom(file_size)

    with open(file + ".key", "wb") as key_output:
        key_output.write(key)
    file_data_encrypted = bytes(a ^ b for (a, b) in zip(file_data_to_encrypt, key))
    with open(file, "wb") as encrypted_out:
        encrypted_out.write(file_data_encrypted)

def decrypt_file(file: str, key_file: str):
    file_data_to_decrypt = open(file, "rb").read()
    key = open(key_file, "rb").read()
    file_data_decrypted = bytes(a ^ b for (a, b) in zip(file_data_to_decrypt, key))

    with open(file, "wb") as decrypted_out:
        decrypted_out.write(file_data_decrypted)

@app.command()
def encrypt(folder: str):
    for file in os.listdir(folder):
        encrypt_file(f"{folder}\\{file}")

@app.command()
def decrypt(folder: str):
    keys = []
    files = []
    for file in os.listdir(folder):
        if file.endswith(".key"):
            keys.append(f"{folder}\\{file}")
        else:
            files.append(f"{folder}\\{file}")
    pairs = []
    for key in keys:
        for file in files:
            if key.split("\\")[-1].startswith(file.split("\\")[-1]):
                pairs.append([key, file])
    for pair in pairs:
        decrypt_file(pair[1], pair[0])
        os.remove(pair[0])

if __name__ == "__main__":
    app()