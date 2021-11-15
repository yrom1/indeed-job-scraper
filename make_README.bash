set -e
rm -f README.md
jupyter-nbconvert --to markdown README.ipynb
python3 clean_README.py
