import os

os.system("rm -r mini_book/_build/html")
os.system("jupyter-book build ./mini_book --all")
os.system("python scripts/clean_html.py")
