# check.py — reading the subscribers file (tests first)
#
# Step 1 (done): wrote the tests first and watched all three FAIL (NameError).
# Step 2 (now): the three functions below. Run:  uv run pytest check.py

SUBSCRIBERS_FILE: str = "data/subscribers.csv"
HEADER_LINES: int = 1   # the first line holds column names, not a subscriber
GROUP_COLUMN: int = 3   # first_name=0, last_name=1, email=2, group=3


def read_subscribers(path: str) -> str:
    with open(path, encoding="utf-8") as file:
        return file.read()


def count_emails(text: str) -> int:
    lines: list[str] = text.splitlines()
    return len(lines) - HEADER_LINES


def count_group(text: str, group: str) -> int:
    count: int = 0
    for line in text.splitlines():
        fields: list[str] = line.split(",")
        if fields[GROUP_COLUMN] == group:
            count += 1
    return count


def test_read_gives_text() -> None:
    text: str = read_subscribers(SUBSCRIBERS_FILE)
    assert isinstance(text, str)


def test_total_emails_is_24() -> None:
    text: str = read_subscribers(SUBSCRIBERS_FILE)
    assert count_emails(text) == 24


def test_daily_drinkers_has_8_rows() -> None:
    text: str = read_subscribers(SUBSCRIBERS_FILE)
    assert count_group(text, "daily-drinkers") == 8
