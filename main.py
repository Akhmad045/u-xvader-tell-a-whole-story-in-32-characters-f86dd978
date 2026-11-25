"""Tell a Whole Story in 32 Characters - entry program.

Writes the single Wi-Fi network name to /output/entry.txt.
The name: Password: Your Anniversary, Dave. The password is the
anniversary Dave forgot - the network itself is the rebuke, and the
whole marriage is in the hint.
"""

import os

NAME = "Password: Your Anniversary, Dave"


def main() -> None:
    name = NAME.strip()
    if not name or len(name) > 32:
        raise ValueError("entry must be a Wi-Fi name of 1-32 characters")
    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(name)


if __name__ == "__main__":
    main()
