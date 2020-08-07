# common_language

> *The United States and Great Britain are two countries separated by a common language.*
> - George Bernard Shaw

For those annoying times when Americans need to submit articles to [MNRAS](https://academic.oup.com/mnras), 
or Brits to [ApJ](https://iopscience.iop.org/journal/0004-637X).

Absolutely no guarantees that this won't replace some vital bit
of LaTeX and screw up your document. 

Word list originally from http://www.tysto.com/uk-us-spelling-list.html

## Examples

#### 🇬🇧  ->  🇺🇸
```
python britishise.py manuscript_us.tex [manuscript_gb.tex]
```

#### 🇺🇸 -> 🇬🇧 
```
python americanize.py manuscript_gb.tex [manuscript_us.tex]
```

Changes are printed to the terminal; if you supply the second 
argument, it'll save your new version to that file.
