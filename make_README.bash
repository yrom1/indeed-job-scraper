set -e
rm -f README.md
python3 -m nbconvert --to markdown README.ipynb
python3 clean_README.py
