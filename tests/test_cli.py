from unicode.cli import describe


def test_describe_ascii_character() -> None:
    result = describe("A")

    assert result == ["U+0041 'A' LATIN CAPITAL LETTER A"]


def test_describe_unicode_character() -> None:
    result = describe("é")

    assert result == ["U+00E9 'é' LATIN SMALL LETTER E WITH ACUTE"]
