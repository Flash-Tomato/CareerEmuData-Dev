#!/usr/bin/env python3

import gzip
import json
import os
import subprocess
import sys
from pathlib import Path

import msgpack

SPLIT = "dev"
ROOT_DIR = Path(__file__).parent
CACHE_DIR = ROOT_DIR / ".cache"
DATA_DIR = ROOT_DIR / "career_emulator_bdci26" / SPLIT / "dataset"
assert DATA_DIR.exists()

def update_cache():
    """Update cache for test set data."""
    if CACHE_DIR.is_dir() and list(CACHE_DIR.glob("*")):
        subprocess.run(["git", "-C", str(CACHE_DIR), "fetch", "origin"], check=True)
        subprocess.run(["git", "-C", str(CACHE_DIR), "reset", "--hard", "origin/main"], check=True)
        subprocess.run(["git", "-C", str(CACHE_DIR), "clean", "-fd"], check=True)
    else:
        subprocess.run(
            ["git", "clone", "https://github.com/Flash-Tomato/TomatoEmuData-Test.git", str(CACHE_DIR)], check=True
        )


def convert_json_to_msgpack(json_path: Path) -> None:
    """Convert json to compressed messagepack data files."""
    msgpack_path = json_path.with_suffix(".data")

    try:
        with json_path.open("r", encoding="utf-8") as f:
            data = json.load(f)

        header = b"DEV"
        if msgpack_path.is_file():
            try:
                raw = msgpack_path.read_bytes()
                if raw.startswith(header):
                    existing = msgpack.unpackb(gzip.decompress(raw[len(header) :]))
                    if existing == data:
                        print(f"Unchanged: {msgpack_path}")
                        return
            except Exception:
                pass

        with msgpack_path.open("wb") as f:
            f.write(header + gzip.compress(msgpack.packb(data)))

        print(f"Converted: {json_path} -> {msgpack_path}")

    except Exception as e:  # pylint: disable=broad-exception-caught
        print(f"Failed: {json_path} ({e})", file=sys.stderr)


if __name__ == "__main__":
    update_cache()
    json_files = list(f for f in DATA_DIR.rglob("*.json") if os.path.sep + "." not in str(f.absolute()))

    for file in json_files:
        current_file = file.relative_to(DATA_DIR)
        reference_file = CACHE_DIR / current_file
        if reference_file.is_file:
            file.write_bytes(reference_file.read_bytes())

    if not json_files:
        print("No JSON files found.")
        sys.exit(1)

    for path in json_files:
        convert_json_to_msgpack(path)
