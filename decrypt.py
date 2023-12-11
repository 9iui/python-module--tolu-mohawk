from cryptography.fernet import Fernet
import argparse
import base64

def decrypt(input_file, key):
    cipher_suite = Fernet(base64.urlsafe_b64encode(key))

    with open(input_file, 'rb') as file:
        encrypted_message = file.read()

    decrypted_message = cipher_suite.decrypt(encrypted_message)
    print("Decrypted Message:", decrypted_message.decode())

def main():
    parser = argparse.ArgumentParser(description="Decrypt a message from a file using a key.")
    parser.add_argument("--input", required=True, help="The input file path")
    parser.add_argument("--key", required=True, help="The decryption key")

    args = parser.parse_args()

    # Ensure the key is 32 bytes long
    key = base64.urlsafe_b64encode(args.key.encode())
    key = key.ljust(32, b'=')

    decrypt(args.input, key)

if __name__ == "__main__":
    main()
