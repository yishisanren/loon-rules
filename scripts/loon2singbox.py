#!/usr/bin/env python3
"""Convert a Loon/Surge/Clash-style .list rule file into a sing-box
source rule-set (.json, version 2).

Usage: loon2singbox.py <input.list> <output.json>

Each matcher type is emitted as its own rule object so the rule-set
matches with OR semantics across types (sing-box AND-combines different
fields within a single rule object).
"""
import json
import sys

# Loon rule type -> sing-box source rule-set field
TYPE_MAP = {
    "DOMAIN": "domain",
    "DOMAIN-SUFFIX": "domain_suffix",
    "DOMAIN-KEYWORD": "domain_keyword",
    "DOMAIN-WILDCARD": "domain_regex",  # best-effort
    "IP-CIDR": "ip_cidr",
    "IP-CIDR6": "ip_cidr",
}
# Field emission order (stable, readable output)
FIELD_ORDER = ["domain", "domain_suffix", "domain_keyword", "domain_regex", "ip_cidr"]


def convert(in_path, out_path):
    buckets = {f: [] for f in FIELD_ORDER}
    seen = {f: set() for f in FIELD_ORDER}
    skipped = []

    with open(in_path, encoding="utf-8") as fh:
        for raw in fh:
            line = raw.strip()
            if not line or line.startswith("#") or line.startswith(";"):
                continue
            parts = [p.strip() for p in line.split(",")]
            rtype = parts[0].upper()
            if rtype not in TYPE_MAP or len(parts) < 2:
                skipped.append(line)
                continue
            field = TYPE_MAP[rtype]
            value = parts[1]
            if not value:
                continue
            if value not in seen[field]:
                seen[field].add(value)
                buckets[field].append(value)

    rules = []
    for field in FIELD_ORDER:
        if buckets[field]:
            rules.append({field: buckets[field]})

    out = {"version": 2, "rules": rules}
    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=2)
        fh.write("\n")

    total = sum(len(v) for v in buckets.values())
    print(f"{in_path} -> {out_path}: {total} entries, {len(rules)} rule group(s)")
    if skipped:
        print(f"  skipped {len(skipped)} unsupported line(s):", file=sys.stderr)
        for s in skipped:
            print(f"    {s}", file=sys.stderr)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(1)
    convert(sys.argv[1], sys.argv[2])
