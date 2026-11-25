# check.py: tests for mailroom.py (plain assert, no pytest needed)
#
# Run:  uv run python check.py
# If every assert holds, the last line prints. If one fails, Python stops
# with AssertionError and shows that assert's message.

from mailroom import SUBSCRIBERS_FILE, count_emails, count_group, read_subscribers

subscribers: str = read_subscribers(SUBSCRIBERS_FILE)

# Behaviour 1: when the file is read, its output type is string
assert isinstance(subscribers, str), "reading the file should give back text (str)"

# Behaviour 2: total number of emails will be 24
assert count_emails(subscribers) == 24, "there should be 24 emails"

# Behaviour 3: the daily-drinkers group has 8 rows
assert count_group(subscribers, "daily-drinkers") == 8, "daily-drinkers should have 8 rows"

print("All 3 checks passed.")
