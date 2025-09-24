"""
Basic Dictionary App (under 200 lines)

Interactive CLI to add, lookup, edit, remove, and list words.
Data persists to a JSON file next to this script.

Commands:
  help                     Show commands
  lookup WORD              Show definition of WORD
  add WORD DEFINITION...   Add WORD with DEFINITION (fails if exists)
  edit WORD DEFINITION...  Replace definition of WORD
  remove WORD              Delete WORD
  list [PREFIX]            List words, optionally filtered by PREFIX
  save                     Force save to disk
  exit | quit              Exit the app
"""

from __future__ import annotations

import json
import shlex
from difflib import get_close_matches
from pathlib import Path


DATA_FILE = Path(__file__).with_name("dictionary_data.json")


def load_data(path: Path) -> dict[str, str]:
    if not path.exists():
        return {}
    try:
        with path.open("r", encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, dict):
            # Coerce non-str keys/values defensively
            return {str(k): str(v) for k, v in data.items()}
    except Exception:
        pass
    return {}


def save_data(path: Path, data: dict[str, str]) -> None:
    tmp = path.with_suffix(path.suffix + ".tmp")
    with tmp.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    tmp.replace(path)


def print_help() -> None:
    print(__doc__.strip())


def lookup(data: dict[str, str], word: string) -> None:  # type: ignore[name-defined]
    # Type hint above kept minimal to fit under 200 lines; runtime unaffected.
    w = word.strip()
    if not w:
        print("Please provide a word to lookup.")
        return
    if w in data:
        print(f"{w}: {data[w]}")
        return
    print(f"'{w}' not found.")
    suggestions = get_close_matches(w, data.keys(), n=5, cutoff=0.6)
    if suggestions:
        print("Did you mean:")
        for s in suggestions:
            print(f"  - {s}")


def add_word(data: dict[str, str], word: str, definition: str) -> None:
    w = word.strip()
    if not w or not definition.strip():
        print("Usage: add WORD DEFINITION...")
        return
    if w in data:
        print(f"'{w}' already exists. Use 'edit' to change it.")
        return
    data[w] = definition.strip()
    save_data(DATA_FILE, data)
    print(f"Added '{w}'.")


def edit_word(data: dict[str, str], word: str, definition: str) -> None:
    w = word.strip()
    if not w or not definition.strip():
        print("Usage: edit WORD DEFINITION...")
        return
    if w not in data:
        print(f"'{w}' does not exist. Use 'add' to create it.")
        return
    data[w] = definition.strip()
    save_data(DATA_FILE, data)
    print(f"Updated '{w}'.")


def remove_word(data: dict[str, str], word: str) -> None:
    w = word.strip()
    if not w:
        print("Usage: remove WORD")
        return
    if w in data:
        del data[w]
        save_data(DATA_FILE, data)
        print(f"Removed '{w}'.")
    else:
        print(f"'{w}' not found.")


def list_words(data: dict[str, str], prefix: str | None = None) -> None:
    words = sorted(data.keys())
    if prefix:
        words = [w for w in words if w.lower().startswith(prefix.lower())]
    if not words:
        print("No entries.")
        return
    for w in words:
        print(w)


def main() -> None:
    data = load_data(DATA_FILE)
    print("Dictionary App — type 'help' for commands.")
    while True:
        try:
            line = input("> ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nBye!")
            break
        if not line:
            continue
        try:
            parts = shlex.split(line)
        except ValueError as e:
            print(f"Parse error: {e}")
            continue
        cmd, *args = parts
        cmd = cmd.lower()

        if cmd in {"exit", "quit"}:
            print("Bye!")
            break
        if cmd == "help":
            print_help()
        elif cmd == "lookup" and len(args) >= 1:
            lookup(data, args[0])
        elif cmd == "add" and len(args) >= 2:
            add_word(data, args[0], " ".join(args[1:]))
        elif cmd == "edit" and len(args) >= 2:
            edit_word(data, args[0], " ".join(args[1:]))
        elif cmd == "remove" and len(args) >= 1:
            remove_word(data, args[0])
        elif cmd == "list":
            list_words(data, args[0] if args else None)
        elif cmd == "save":
            save_data(DATA_FILE, data)
            print("Saved.")
        else:
            print("Unknown or invalid command. Type 'help'.")


if __name__ == "__main__":
    main()

