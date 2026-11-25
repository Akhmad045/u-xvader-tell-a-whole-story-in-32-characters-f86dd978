"""Tell a Whole Story in 32 Characters - entry program.

Writes the single Wi-Fi network name to /output/entry.txt.
The name: Password: Your Anniversary, Dave. The password is the
anniversary Dave forgot - the network itself is the rebuke, and the
whole marriage is in the hint.

The gate scores /output/entry.txt as UTF-8 text of 1 to 32 characters,
not only white space, so validate() enforces exactly that (plus no
control characters and no leading/trailing whitespace) before writing.
Run with --self-test to exercise the validator without writing.
"""

import os
import sys

NAME = "Password: Your Anniversary, Dave"
MAX_CHARS = 32


def validate(name: str) -> str:
    """Return the name if it passes the gate, else raise ValueError."""
    if not name or not name.strip():
        raise ValueError("entry must not be empty or whitespace-only")
    if name != name.strip():
        raise ValueError("entry must not have leading/trailing whitespace")
    if len(name) > MAX_CHARS:
        raise ValueError(
            f"entry must be at most {MAX_CHARS} characters, got {len(name)}")
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in name):
        raise ValueError("entry must not contain control characters")
    return name


def self_test() -> None:
    """Check the validator accepts the entry and rejects bad inputs."""
    cases = [
        (NAME, True),
        ("", False),
        ("   ", False),
        ("x" * 33, False),
        ("x" * 32, True),
        ("a\nb", False),
        (" Password: Your Anniversary, Dave", False),
        ("Password: Your Anniversary, Dave ", False),
        ("\tPassword", False),
    ]
    for text, ok in cases:
        try:
            validate(text)
            passed = True
        except ValueError:
            passed = False
        status = "ok" if passed == ok else "FAIL"
        print(f"{status}: {text!r} -> valid={passed} (expected {ok})")
        if passed != ok:
            raise SystemExit(1)
    # Write + read-back must be byte-identical.
    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(validate(NAME))
    with open(out_path, "rb") as f:
        data = f.read()
    assert data == NAME.encode("utf-8"), data
    assert len(data) == 32, len(data)
    print(f"ok: entry.txt is byte-exact, {len(data)} bytes")
    print("self-test passed")


def main() -> None:
    if "--self-test" in sys.argv:
        self_test()
        return
    name = validate(NAME)
    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(name)


if __name__ == "__main__":
    main()
