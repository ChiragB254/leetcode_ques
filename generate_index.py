import os
import re

README_FILE = "README.md"
INDEX_FILE = "INDEX.md"
RECENT_TAG_START = "<!-- RECENT_START -->"
RECENT_TAG_END = "<!-- RECENT_END -->"

def parse_problem_file(filename):
    match = re.match(r"D(\d+)-(.+)\.py", filename)
    if not match:
        return None
    day = int(match.group(1))
    raw_title = match.group(2)
    title = raw_title.replace("-", " ").title()
    return day, title, filename

def generate_index_and_recent(directory="."):
    problem_files = [
        f for f in os.listdir(directory)
        if f.endswith(".py") and f.startswith("D")
    ]

    problems = []
    for f in problem_files:
        parsed = parse_problem_file(f)
        if parsed:
            problems.append(parsed)

    problems.sort(key=lambda x: x[0])  # Sort by day ascending

    # Write full INDEX.md
    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        f.write("# 📘 LeetCode Python Solutions Index\n\n")
        f.write("| Day | Problem | File |\n")
        f.write("|-----|---------|------|\n")
        for day, title, filename in problems:
            file_link = f"[{filename}](./{filename})"
            f.write(f"| {day} | {title} | {file_link} |\n")

    print(f"✅ INDEX.md generated with {len(problems)} problems.")

    # Get top 5 most recent (highest day number)
    recent = sorted(problems, key=lambda x: x[0], reverse=True)[:5]
    recent_md = "\n".join(
        f"- **Day {day}**: [{title}](./{filename})"
        for day, title, filename in recent
    )

    # Update README.md
    if os.path.exists(README_FILE):
        with open(README_FILE, "r", encoding="utf-8") as f:
            readme = f.read()

        if RECENT_TAG_START in readme and RECENT_TAG_END in readme:
            before = readme.split(RECENT_TAG_START)[0]
            after = readme.split(RECENT_TAG_END)[1]
            updated = (
                before
                + RECENT_TAG_START
                + "\n\n"
                + recent_md
                + "\n\n"
                + RECENT_TAG_END
                + after
            )

            with open(README_FILE, "w", encoding="utf-8") as f:
                f.write(updated)

            print("✅ README.md updated with recent problems.")
        else:
            print("⚠️ README.md missing RECENT_START / RECENT_END markers.")
    else:
        print("⚠️ README.md not found.")

if __name__ == "__main__":
    generate_index_and_recent()
