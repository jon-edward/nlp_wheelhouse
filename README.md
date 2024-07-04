# nlp_wheelhouse
This is a collection of useful NLP tools as Python wheels built for a Windows isolated environment.

## Installation
To install the libraries included, download the `nlp_wheelhouse-win_amd64.zip` from the 
[Releases](https://github.com/jon-edward/nlp_wheelhouse/releases) section, extract it into a directory 
named `wheelhouse`, then run `python -m pip install --no-index --find-links=wheelhouse .\wheelhouse`.

You can also clone this repository, install `requests` and `setuptools`, and run 
`python build.py` to build a local wheelhouse - see `python build.py --help` 
for CLI usage. 

## Adding a library
New libraries can be added to `requirements.txt` and will be picked up on the next release.

## Adding spaCy models
SpaCy models are usually downloaded through `python -m spacy download <model>`, but in an isolated environment
this option isn't available. 

You can run `build.py` with the argument `--extra-wheel-urls <url> [<url2> <url3> ...]` 
which will download a remote wheel file, add it to the wheelhouse directory, and add its distribution name 
to the resulting requirements file to force its installation.

SpaCy models are stored in GitHub Releases, so you can provide a model's download link (ie. the asset link 
for [`en_core_web_sm`](https://github.com/explosion/spacy-models/releases/tag/en_core_web_sm-3.7.1)) as an 
extra wheel url and spaCy will be able to load the model like normal.
 