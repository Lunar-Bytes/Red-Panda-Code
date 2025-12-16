import re

def preprocess(code: str) -> str:
    lines = code.splitlines()
    processed_lines = []

    for line in lines:
        original = line

        # Ignore empty lines and comments
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            processed_lines.append(line)
            continue

        # --- Implicit multiplication rules ---

        # 5x -> 5 * x
        line = re.sub(r'(\d)([a-zA-Z_])', r'\1 * \2', line)

        # x5 -> x * 5
        line = re.sub(r'([a-zA-Z_])(\d)', r'\1 * \2', line)

        # 2(x + y) -> 2 * (x + y)
        line = re.sub(r'(\d)\s*\(', r'\1 * (', line)

        # )( -> ) * (
        line = re.sub(r'\)\s*\(', r') * (', line)

        processed_lines.append(line)

    return "\n".join(processed_lines)
