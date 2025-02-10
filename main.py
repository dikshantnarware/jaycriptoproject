from alphanumeric_converter import convert_40_key_to_64

# Example private key
private_key = "66914F1EC168D09414BBC5C4AB37BA4BC23B9A86"

# Convert and print output
converted_key = convert_40_key_to_64(private_key)
print(f"Converted 64-character key: {converted_key}")
