
import os

os.system("python scripts/clean_html.py")
i = "\"" + input("commit messege?: ") + "\""
os.system('git add mini_book')
c = 'git commit -m ' + i
os.system(c)
os.system("git push")

