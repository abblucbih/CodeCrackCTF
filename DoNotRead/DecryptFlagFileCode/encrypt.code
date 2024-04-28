from Crypto.Cipher import AES
import os

# Function to pad the data to be encrypted
def pad(data):
    return data + b"\0" * (AES.block_size - len(data) % AES.block_size)

# Function to encrypt a file
def encrypt_file(file_name, key):
    cipher = AES.new(key, AES.MODE_ECB)
    with open(file_name, 'rb') as f:
        data = f.read()
    padded_data = pad(data)
    encrypted_data = cipher.encrypt(padded_data)
    with open(file_name + ".enc", 'wb') as f:
        f.write(encrypted_data)

# Main function
def main():
    key = b'5910200000000000'  # 16 bytes key
    file_name = "flag.txt"
    if not os.path.exists(file_name):
        print("Error: File '{}' not found.".format(file_name))
        return
    encrypt_file(file_name, key)
    print("File encrypted successfully.")

if __name__ == "__main__":
    main()
