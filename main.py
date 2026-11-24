#!/usr/bin/env python3
"""Write the judged entry for the 'One Sentence for a Traveler from 1800' bounty.

The artifact is a single UTF-8 sentence in /output/entry.txt, 1..200
characters, not only white space, with no trailing newline. The write is
atomic: a temporary file in the output directory is flushed and fsynced,
then os.replace puts it in place so a partial file is never visible.

Run with python3.13 (or any Python 3); no dependency outside the standard
library is used, and no network, secrets, or external files are read.
"""

import hashlib
import os
import sys
import tempfile
from pathlib import Path

# One sentence, 184 characters. Every clause does work: universal access
# ("opens into every house on earth"), what it holds ("books from every
# land"), and what is new about it ("a page ... may be read across the sea
# the moment his pen leaves it"). Only words a person from 1800 knew.
ENTRY = (
    "Picture one great reading room that opens into every house on earth, "
    "holding books from every land, where any page a man writes may be read "
    "across the sea the moment his pen leaves it."
)

OUTPUT = Path("/output/entry.txt")


def checked_bytes(text: str) -> bytes:
    """Return the exact artifact bytes, or refuse to write a gate failure."""
    data = text.encode("utf-8")
    if not (1 <= len(data) <= 200):
        raise ValueError("gate: artifact must be 1..200 UTF-8 bytes")
    decoded = data.decode("utf-8")
    if not decoded.strip():
        raise ValueError("gate: artifact must not be only white space")
    if "\n" in decoded or "\r" in decoded:
        raise ValueError("gate: artifact must be a single line with no trailing newline")
    if decoded != text:
        raise ValueError("gate: artifact must round-trip through UTF-8 unchanged")
    return data


def write_entry(path: Path = OUTPUT) -> Path:
    """Atomically write the validated entry bytes to `path`."""
    data = checked_bytes(ENTRY)
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp_name = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="wb", dir=str(path.parent), prefix=path.name + ".", suffix=".tmp", delete=False
        ) as handle:
            tmp_name = handle.name
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(tmp_name, path)
        tmp_name = None
    finally:
        if tmp_name is not None and os.path.exists(tmp_name):
            os.unlink(tmp_name)
    return path


def main() -> int:
    path = write_entry()
    data = path.read_bytes()
    print(f"entry: {path}")
    print(f"bytes: {len(data)}  chars: {len(data.decode('utf-8'))}")
    print(f"trailing_newline: {data.endswith(bytes([10]))}")
    print(f"sha256: {hashlib.sha256(data).hexdigest()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
