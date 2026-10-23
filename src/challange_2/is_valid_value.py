
def is_valid_value(value: str) -> bool:
    value = value.strip()

    # Boolean and null values
    if value in ("true", "false", "null"):
        return True

    # String values must start and end with double quotes
    if len(value) >= 2 and value.startswith('"') and value.endswith('"'):
        return True

    # Number values
    try:
        float(value)
        return True
    except ValueError:
        return False
