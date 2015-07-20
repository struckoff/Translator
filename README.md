# Simple cli dictionary tool

## Info

  Simple command line application uses google translate to translate words
  or urban dictionary to find descriptions  

##Usage

````
./translate.py -h
usage: translate.py [-h] {google,urban} ... target

positional arguments:
  {google,urban}
    google        use Google Translate
    urban         use Urban Dictionary
  target

optional arguments:
  -h, --help      show this help message and exit
````

####for "google" option:

````
usage: translate.py google [-h] [-f FRM] [-t TO] [-v]

optional arguments:
  -h, --help      show this help message and exit
  -f , --from     FROM
  -t , --to       TO
  -v, --verbose   show all translation variants
````

####for "urban" option:

````
usage: translate.py google [-h] [-f FRM] [-t TO] [-v]

optional arguments:
  -h, --help          show this help message and exit
  -f FRM, --from FRM  FROM
  -t TO, --to TO      TO
  -v, --verbose       show all translation variants
````
