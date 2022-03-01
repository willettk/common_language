# common_language

> *The United States and Great Britain are two countries separated by a common language.*
> - George Bernard Shaw<sup>*[{{citation needed}}](https://english.stackexchange.com/questions/74737/what-is-the-origin-of-the-phrase-two-nations-divided-by-a-common-language)*</sup>

For those annoying times when Americans need to submit articles to [MNRAS](https://academic.oup.com/mnras) or JFM, 
or Brits to [ApJ](https://iopscience.iop.org/journal/0004-637X).

Word list originally from http://www.tysto.com/uk-us-spelling-list.html

## Examples

#### 🇺🇸 -> 🇬🇧 
```
python3 __main__.py --to uk manuscript_us.tex [manuscript_gb.tex]
```

#### 🇬🇧  ->  🇺🇸
```
python3 __main__.py --to us manuscript_gb.tex [manuscript_us.tex]
```

Replacement suggestions are printed to the terminal. Then, you select whether you replace or not. 

## Fork notes
- Made it interactive. User can reject changes. 
- Better visualization of word replacement. 
- Merge the two scripts "britishise.py" and "americanize.py" into one. User supplies argument "--to {us, uk}"  
- Using `argparse` to parse arguments.  
- Read and write file as streams, instead of loading the entire file into RAM.  
- Be verbose about `undo` (previously named `dontfix`). 
- Omitting output filename will default to `{basename}_uk.{ext}`. 

## Todo
- Change string matching to word-wise. So, part-of-word will not be matched. 
