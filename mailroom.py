# mailroom.py: the real logic for reading the subscribers file
#
# check.py tests these functions. Run the tests with:  uv run python check.py

SUBSCRIBERS_FILE: str = "data/subscribers.csv"
HEADER_LINES: int = 1   # the first line holds column names, not a subscriber
GROUP_COLUMN: int = 3   # first_name=0, last_name=1, email=2, group=3


def read_subscribers(path: str) -> str:
    """Promise: give back the whole file at `path` as one piece of text."""
    with open(path, encoding="utf-8") as file:
        return file.read()


def count_emails(text: str) -> int:
    """Promise: count the subscriber rows (one email per row, header not counted)."""
    lines: list[str] = text.splitlines()
    return len(lines) - HEADER_LINES


def count_group(text: str, group: str) -> int:
    """Promise: count the rows whose group column equals `group`."""
    count: int = 0
    for line in text.splitlines():
        fields: list[str] = line.split(",")
        if fields[GROUP_COLUMN] == group:
            count += 1
    return count
