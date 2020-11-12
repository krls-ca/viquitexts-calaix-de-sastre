# Calaix de Sastre - Viquitexts

> :warning: **AVERTÈNCIA:** Aquests són alguns dels codis no formals que he anat creant des que vaig començar a fer petits codis de manteniment per al Viquitexts el 2006. Una part d'ells no s'han mantingut des de la seva creació i poden no ser ja compatibles amb la versió actual del pywikibot. S'adjunten en aquest repositori per raons històriques i per si poden servir d'inspiració a d'altres en un futur.

Els codis tenen com a dependencia la llibreria pywikibot: https://www.mediawiki.org/wiki/Manual:Pywikibot/ca.

Calaix de sastre dels diferents projectes Wikimedia:
1. [Calaix de Sastre Viquipèdia](https://github.com/krls-ca/viquipedia-calaix-de-sastre)
2. [Calaix de Sastre Wikimedia Commons](https://github.com/krls-ca/viquipedia-calaix-de-sastre)
3. [Calaix de Sastre Wikidata](https://github.com/krls-ca/viquipedia-calaix-de-sastre)
4. [Calaix de Sastre Viquitexts](https://github.com/krls-ca/viquipedia-calaix-de-sastre)
5. [Calaix de Sastre Viquidites](https://github.com/krls-ca/viquipedia-calaix-de-sastre)

## Reorganització Viquitexts en basc (2017, mant. 2018)

Era un codi que categoritzava segons el nivell de revisió de les pàgines transcrites al Viquitexts basc, quan aquest es trobava encara integrat en el Viquitexts multilingüe. Va ser una acció necessària per tal de poder posar en valor el nombre de pàgines transcrites en èuscar abans de proposar que aquest esdevingués un projecte independent amb domini públic. D'aquesta acció es va desencadenar l'aprovació del nou projecte el 2018.

```sh
$ python mass-cat-index-wikisource.py
```

## Concurs Viquirepte (2013, mant. 2015)

Era un codi rudinimentari que donat un conjunt finit de Llibres a concurs, assigna una puntuació per pàgina validada i/o revisades en un temps finit de concurs. Aquest va ser utilitzat almenys en tres ocasions i va ser adaptat en d'altres concursos homònims en d'altres idiomes.

https://ca.wikisource.org/wiki/Viquitexts:Viquirepte_16%C3%A8_aniversari (2019)
https://ca.wikisource.org/wiki/Viquitexts:Viquirepte_Jocs_Florals_de_Barcelona (2014)
https://ca.wikisource.org/wiki/Viquitexts:Viquirepte_10%C3%A8_aniversari (2013)

```sh
$ python wikisource-contest.py
```