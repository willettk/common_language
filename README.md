# common_language
#
*The United States and Great Britain are two countries separated by a common language.*
- George Bernard Shaw

For those annoying times when Americans need to submit articles to MNRAS, 
or Brits to ApJ.

Absolutely no guarantees that this won't replace some vital bit
of LaTeX and screw up your document. 

Word list originally from http://www.tysto.com/uk-us-spelling-list.html

Example:

```
python britishise.py manuscript_us.tex [manuscript_gb.tex]
```

or

```
python americanize.py manuscript_gb.tex [manuscript_us.tex]
```

Changes are printed to the terminal; if you supply the second 
argument, it'll save your new version to that file.
