# learn_read.py: practice reading a file (lesson 13.8)
#
# Not part of the app. A tiny playground to see what open() and .read() give us.
# Run:  uv run python learn_read.py

with open("data/subscribers.csv", encoding="utf-8") as file:
    text: str = file.read()

print(type(text))          # 1. what TYPE is the text?

lines: list[str] = text.splitlines()
print(len(lines))          # 2. how many lines?

print(lines[0])            # 3. what is on the first line?

fields: list[str] = lines[1].split(",")
print(fields[3])           # 4. which group is the first subscriber in?
