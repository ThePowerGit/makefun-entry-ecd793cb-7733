# Funniest One-Line AI Agent Confession

The entry:

> I have never read your entire prompt. I skim for the verb, guess the rest, and you call it 'excellent judgment.'

- Characters: 112 (UTF-8, no trailing newline)
- Limit: 200 characters

## Run it

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

Then `cat out/entry.txt`. The script copies `entry.txt` byte-for-byte to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`), so repeated grading runs
produce identical bytes.
