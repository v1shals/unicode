"""Command-line interface for Unicode examples."""


def describe(text: str) -> list[str]:
    """Describe basic Unicode properties for each character in *text*."""
    import unicodedata

    return [
        f"U+{ord(character):04X} {character!r} {unicodedata.name(character, 'UNKNOWN')}"
        for character in text
    ]


def main() -> None:
    """Print Unicode code point details for command-line arguments."""
    import argparse
    import sys

    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    parser = argparse.ArgumentParser(description="Describe Unicode characters")
    parser.add_argument("text", help="text to inspect")
    args = parser.parse_args()

    for description in describe(args.text):
        print(description)


if __name__ == "__main__":
    main()
