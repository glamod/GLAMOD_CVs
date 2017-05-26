# Instructions for building the GLAMOD Controlled Vocabulary

These are brief instructions on the process undertaken to build the GLAMOD CV:

## Fork CMIP6_CVs on GitHub:

Fork: https://github.com/WCRP/CMIP6_CVs
To:   https://github.com/agstephens/CMIP6_CVs
 
## Clone to local repo:

```
cd ~/gws/git
git clone https://github.com/agstephens/CMIP6_CVs
```
 
## Enter and create glamod CVs branch:

```
cd CMIP6_CVs/
git checkout -b GLAMOD_CVs
git push -u origin GLAMOD_CVs
```
 
## Edit the CV content but leave a few files in there for testing:

 - deleted many files
 - deleted `src/` dir
 - updated metadata in files
 - removed some parts of files
 - renamed files from `CMIP6_*` to `GLAMOD_*`:
    `for f in CMIP6* ; do nf=$(echo $f | sed 's/CMIP6/GLAMOD/g') ; git mv $f $nf ; done`
 - committed and pushed to GitHub.
 
## Create a brand-new GitHub vocabs repo:

 https://github.com/glamod/GLAMOD_CVs
 
 - with `README.md` and Licence: BSD simplified
 
## Clone the repo locally:

```
cd ../
git clone https://agstephens@github.com/glamod/GLAMOD_CVs
cd GLAMOD_CVs/
```

## Copy content from new branch of CMIP6_CVs into this new repo:

```
cp ../CMIP6_CVs/*.* ./
git add *.*
git commit
git push
```

## Clone the existing pyessv library from github:

```
cd ../
git clone https://github.com/ES-DOC/pyessv
```

## Create a virtualenv for it:

```
cd pyessv/
virtualenv venv
. venv/bin/activate
pip install -r requirements.txt
```
 
## Fork pyessv-writer and rewrite for GLAMOD:

On Github:

Fork: https://github.com/ES-DOC/pyessv-writer
To:   https://github.com/glamod/pyessv-writer
   
## Clone to local machine:

```
cd ../
git clone https://agstephens@github.com/glamod/pyessv-writer
cd pyessv-writer/
```
 
## Edit writer files to work on GLAMOD:

```
 README.md
 sh/activate
 sh/utils.sh
 sh/write_glamod_cvs.py
 sh/write_glamod_cvs.sh
```

Then add them, commit and push to GitHub.

## Activate virtualenv (for pyessv) and then run the writer to generate the local version of the CV:

```
source ../pyessv/venv/bin/activate
export PYTHONPATH=$PYTHONPATH:../pyessv
mkdir  -p ~/.esdoc/pyessv-archive
python sh/write_glamod_cvs.py --source=../GLAMOD_CVs
```

This writes the cached version of the CV to:

`~/.esdoc/pyessv-archive/glamod-team/glamod`
 
## Work with the vocabulary using the pyessv library:

```
$ python
>>> import pyessv
>>> freq = pyessv.load('glamod-team', 'glamod', 'frequency')
>>> for term in freq: print term
...
glamod-team:glamod:frequency:1hr
glamod-team:glamod:frequency:1hrclimmon
glamod-team:glamod:frequency:3hr
glamod-team:glamod:frequency:3hrclim
glamod-team:glamod:frequency:6hr
glamod-team:glamod:frequency:day
glamod-team:glamod:frequency:decadal
glamod-team:glamod:frequency:fx
glamod-team:glamod:frequency:mon
glamod-team:glamod:frequency:monclim
glamod-team:glamod:frequency:subhr
glamod-team:glamod:frequency:yr
glamod-team:glamod:frequency:yrclim

>>> inst_mohc =  pyessv.load('glamod-team', 'glamod', 'institution-id', 'mohc')
>>> print inst_mohc
glamod-team:glamod:institution-id:mohc

>>> print inst_mohc.label
MOHC

>>> print inst_mohc.data
{u'postal_address': u'Met Office Hadley Centre, Fitzroy Road, Exeter, Devon, EX1 3PB, UK'}

>>> print inst_mohc.data['postal_address']
Met Office Hadley Centre, Fitzroy Road, Exeter, Devon, EX1 3PB, UK

>>> for key in [ 'all_names', 'alternative_name', 'alternative_url', 'ancestors', \
                   'associations', 'authority', 'canonical_name', 'collection', \
                   'create_date', 'data', 'description', 'get_comparator', 'hierarchy', \
                   'idx', 'io_name', 'label', 'name', 'namespace', 'parent', 'raw_name', \
                   'scope', 'status', 'synonyms', 'typekey', 'uid', 'url']:
 ...     print key, "=", getattr(inst_mohc, key, "NOT DEFINED")
all_names = set([u'mohc', u'MOHC'])
alternative_name = None
alternative_url = None
ancestors = [glamod-team, glamod-team:glamod, glamod-team:glamod:institution-id]
associations = []
authority = glamod-team
canonical_name = mohc
collection = glamod-team:glamod:institution-id
create_date = 2017-05-25 22:15:20.195258+00:00
data = {u'postal_address': u'Met Office Hadley Centre, Fitzroy Road, Exeter, Devon, EX1 3PB, UK'}
description = MOHC
get_comparator = <function get_comparator at 0xe44938>
hierarchy = [glamod-team, glamod-team:glamod, glamod-team:glamod:institution-id, glamod-team:glamod:institution-id:mohc]
idx = 3
io_name = mohc
label = MOHC
name = mohc
namespace = glamod-team:glamod:institution-id:mohc
parent = None
raw_name = MOHC
scope = glamod-team:glamod
status = pending
synonyms = []
typekey = term
uid = a5a96893-5f40-4232-8953-6715e11e7288
url = None

## Push changes in pyessv-writer to the server

```
git commit -a -m 'Updated to work with GLAMOD'
```


