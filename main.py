import os

LINE = "My calendar was so full I booked a meeting with myself to cancel my meetings \u2014 and past me declined, saying I was busy."

def main():
    # Gate: UTF-8, 1-200 chars, not only whitespace, one line, no leading/trailing whitespace.
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert LINE.strip(), "line must not be only whitespace"
    assert LINE == LINE.strip(), "line must have no leading/trailing whitespace"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
