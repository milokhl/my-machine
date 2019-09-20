# Regexp and Grep Cheat Sheet
```bash
# Match the start of a line
grep "^beginning" input.txt

# Match the end of a line
grep "end$" input.txt

# Match a whole line exactly
grep "^Must match everything in here exactly$" input.txt

# Case-insensitive (default is sensitive)
grep "^CASE doesn't MATTER this WAY$" -i input.txt

# Find lines with one of the words in a list
grep -E this\|that\|other input.txt

# OR make a file with a pattern on each line
grep -Ff patterns.txt input.txt
```
