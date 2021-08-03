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


replace =  "class=\"fas fa-expand\"></i></button></a>"

with_ = replace + "\n" + "<link rel=\"stylesheet\" href=\"https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css\"> <a class=\"full-screen-button\"><button type=\"button\" class=\"btn btn-secondary topbarbtn\" data-toggle=\"tooltip\" data-placement=\"bottom\" onclick=\"location.href=\'https://github.com/jmhuer\';\" aria-label=\"Github\" title=\"Github\" style=\"margin-top:2px\"><i class=\"fa fa-github\" style=\"font-size:27px\"></i></button></a> <a class=\"full-screen-button\"><button type=\"button\" class=\"btn btn-secondary topbarbtn\" data-toggle=\"tooltip\" data-placement=\"bottom\" onclick=\"location.href=\'independent/emailme.html\';\" aria-label=\"Github\" title=\"Email me\" ><i class=\"fa fa-envelope\" style=\"font-size:23px\"></i></button></a>"

replace_html(base, replace,with_)
