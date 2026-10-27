"""JSON-lines log pretty printer: pretty-print and filter by level."""
import argparse
import json
import sys


def parse_lines(text, level=None):
    entries = []
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            entry = json.loads(line)
        except json.JSONDecodeError:
            continue
        if level and str(entry.get("level", "")).upper() != level.upper():
            continue
        entries.append(entry)
    return entries


def render(entries):
    return "\n".join(json.dumps(e, indent=2, sort_keys=True) for e in entries)


def main(argv=None):
    p = argparse.ArgumentParser(description="Pretty-print JSON-lines logs.")
    p.add_argument("file")
    p.add_argument("--level", default=None, help="e.g. ERROR, INFO")
    args = p.parse_args(argv)
    entries = parse_lines(open(args.file, encoding="utf-8").read(), args.level)
    if entries:
        print(render(entries))
    print(f"{len(entries)} entr(y/ies) shown.", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
