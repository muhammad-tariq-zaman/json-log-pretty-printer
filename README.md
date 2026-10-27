# json-log-pretty-printer

Read a JSON-lines log file, pretty-print each entry, and optionally filter
by log level. Malformed lines are skipped, not invented.

## How to run

```bash
python3 main.py app.jsonl --level ERROR
```

## Example output (sample from test fixture data)

```text
{
  "level": "ERROR",
  "msg": "fail"
}
```

Standard library only. No network access.
