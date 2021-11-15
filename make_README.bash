set -e
rm -f README.md
./venv/bin/jupyter-nbconvert --to markdown README.ipynb
python3 clean_README.md.py
