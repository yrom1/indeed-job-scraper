set -e
rm -f README.md
python3 -m nbconvert --to markdown read_local_pickle.nbconvert.ipynb
mv read_local_pickle.nbconvert.md README.md
python3 clean_README.py
