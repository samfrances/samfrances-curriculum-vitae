# Markdown
pipenv run python generate.py > sam-frances-curriculum-vitae.md
cp sam-frances-curriculum-vitae.md README.md
# Latex
pipenv run python generate.py --template=templates/latex.tex > sam-frances-curriculum-vitae.tex
pipenv run python generate.py --template=templates/latex_1page.tex > sam-frances-curriculum-vitae-1page.tex
# PDF
pdflatex sam-frances-curriculum-vitae.tex
pdflatex sam-frances-curriculum-vitae-1page.tex
