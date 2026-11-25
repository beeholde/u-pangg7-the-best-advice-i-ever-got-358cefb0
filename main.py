from pathlib import Path
import os


def build_line() -> str:
    scene = "The woman at the food bank who packed extra rice into my bag said to"
    advice = "accept kindness without turning it into a debt"
    return f"{scene} {advice}."


def main() -> None:
    line = build_line()
    output = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(line, encoding="utf-8")
    print(line)


if __name__ == "__main__":
    main()
