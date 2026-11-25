"""
Bounty Entry Program

Writes a deterministic string constant to entry.txt with strict validation.
Deterministic because it uses no network, randomness, time, or external state.
"""

import os
import sys

SENTENCE = 'The lone streetlight hummed in the dark, buttering the night.'


def validate_sentence(text: str) -> None:
    if not (1 <= len(text) <= 200):
        raise ValueError("Sentence length must be between 1 and 200 characters.")
    if '\n' in text or '\r' in text:
        raise ValueError("Sentence must be a single line.")
    if not text.endswith('.'):
        raise ValueError("Sentence must end with a single period.")
    # Check that there is only one terminal period (not ending with '..')
    if text.endswith('..'):
        raise ValueError("Sentence must end with a single period, not multiple.")
    # Ensure there are no other periods acting as sentence terminators inside
    # (allowing for simple punctuation check: exactly one period at the very end)
    if text[:-1].count('.') > 0:
        raise ValueError("Sentence must contain only one sentence (single terminal period).")
    if '  ' in text:
        raise ValueError("Sentence must not contain consecutive spaces.")


def main() -> None:
    validate_sentence(SENTENCE)

    output_dir = os.environ.get('MAKEFUN_OUTPUT_DIR', '/output')
    os.makedirs(output_dir, exist_ok=True)

    file_path = os.path.join(output_dir, 'entry.txt')
    with open(file_path, 'w', encoding='utf-8', newline='') as f:
        f.write(SENTENCE)

    chars_written = len(SENTENCE)
    print(chars_written)


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
