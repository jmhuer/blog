
import os

os.system("python clean_html.py")
i = "\"" + input("commit messege?: ") + "\""
os.system('git add mini_book')
os.system('git add latex-resume')
c = 'git commit -m ' + i
os.system(c)
os.system("git push")

