# Simple truecaser for CMC (and other types of) data

You can learn a model by sending a bunch of properly cased data to the script ```learn.py```, one (of a few) token(s) per line, sentence boundary being an empty line. The tool simply counts the number of different casings in tokens that are not at the start of sentences. The statistics / model is written to standard output.

```
python learn.py < standard_data | gzip -c > model.gz
```

Once you have the model, you can apply it with the script ```apply.py```, again the input being one (or a few) token(s) per line and the sentence boundary being an empty line. There is a flag ```-U``` if you want for first tokens in sentences to be always non-lowercased. If you do not want the start of the sentence to be non-lowercased, you do not need sentence boundaries.

```
python apply.py model < non_standard_data > truecased_data
```

Currently there is a model for Slovene, learnt from the Slovene web corpus, available in ```lexicon.sl.gz```.

```
$ python apply.py lexicon.sl.gz < example.txt
jst
ne vem
gdo
je
Alenka
Bratušek
.

iPhone
dela
kot
Apple
.

$ python apply.py -U lexicon.sl.gz < example.txt
Jst
ne vem
gdo
je
Alenka
Bratušek
.

iPhone
dela
kot
Apple
.

```
