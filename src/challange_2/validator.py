
from challange_2.is_valid_value import is_valid_value


def validator(filename: str) -> bool:
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = file.read().strip()

        if not data.startswith("{") or not data.endswith("}"):
            return False

        content = data[1:-1].strip()

        if content == "":
            return True

        pairs = content.split(",")

        for pair in pairs:
            if ":" not in pair:
                return False

            key, value = pair.split(":", 1)

            key = key.strip()
            value = value.strip()

            if not (
                len(key) >= 2
                and key.startswith('"')
                and key.endswith('"')
            ):
                return False

            if not is_valid_value(value):
                return False

        return True

    except OSError:
        return False
