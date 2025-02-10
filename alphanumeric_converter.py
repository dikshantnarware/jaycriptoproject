import hashlib
import logging

# Configure logging
logging.basicConfig(
    filename="alphanumeric_converter.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def convert_40_key_to_64(input_key: str) -> str:
    """
    Converts a 40-character hexadecimal private key into a 64-character SHA-256 hash.
    
    Args:
        input_key (str): A 40-character hex string representing the private key.
    
    Returns:
        str: A 64-character hex string if successful, else an error message.
    """
    try:
        if len(input_key) != 40:
            raise ValueError("Invalid input length! Expected a 40-character hexadecimal key.")
        
        # Convert hex string to bytes
        input_bytes = bytes.fromhex(input_key)
        
        # Compute SHA-256 hash
        hashed_key = hashlib.sha256(input_bytes).hexdigest()
        
        logging.info(f"Successfully converted key: {input_key} -> {hashed_key}")
        return hashed_key
    except ValueError as e:
        logging.error(f"Error converting key: {e}")
        return f"Error: {e}"

# Only runs if this script is executed directly
if __name__ == "__main__":
    user_input = input("Enter your 40-character key: ").strip()
    result = convert_40_key_to_64(user_input)
    print(f"Converted Key: {result}")
