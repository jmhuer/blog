import os
import codecs

base = 'mini_book/_build/html'

def replace_html(base,replace,with_):
    for subdir, dirs, files in os.walk(base):
        for file in files:
            filename = os.path.join(subdir, file)
            if filename.endswith('.html'):
                f = codecs.open(filename, 'r')
                # for line in f.read():
                s = f.read().replace(replace, with_)
                with open(filename, 'w') as filetowrite:
                    filetowrite.write(s)


replace =  "Powered by <a href=\"https://jupyterbook.org\">Jupyter Book</a>"
with_ = " "

replace_html(base, replace,with_)

replace =  "<i class=\"fas fa-external-link-alt\">"
with_ = " "

replace_html(base, replace,with_)