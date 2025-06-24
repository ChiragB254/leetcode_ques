import os
import re

def parse_problem_file(filename):
    match = re.match(r"D(\d+)-(.+)\.py", filename)
    if not match:
        return None
    day = int(match.group(1))
    raw_title = match.group(2)
    title = raw_title.replace("-", " ").title()
    return day, title, filename

def generate_index(directory="."):
    problem_files = [
        f for f in os.listdir(directory)
        if f.endswith(".py") and f.startswith("D")
    ]

    problems = []
    for f in problem_files:
        parsed = parse_problem_file(f)
        if parsed:
            problems.append(parsed)

    problems.sort(key=lambda x: x[0])  # Sort by day

    with open("INDEX.md", "w", encoding="utf-8") as f:
        f.write("# 📘 LeetCode Python Solutions Index\n\n")
        f.write("| Day | Problem | File |\n")
        f.write("|-----|---------|------|\n")
        for day, title, filename in problems:
            file_link = f"[{filename}](./{filename})"
            f.write(f"| {day} | {title} | {file_link} |\n")

    print(f"✅ INDEX.md generated with {len(problems)} problems.")

if __name__ == "__main__":
    generate_index()
