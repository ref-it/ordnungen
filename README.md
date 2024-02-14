# Ordnungen

## Installation von Abhängigkeiten

HTML:

```
dnf install python3-pip make
pip install sphinx sphinx_rtd_theme sphinx-intl
```

PDF:

```
dnf install python3-pip texlive-scheme-full
pip install sphinx sphinx_rtd_theme
```

## Bauen der Dokumentation

HTML:

```
./build-html.sh
```

PDF:

```
./build-pdf.sh
```

## Bearbeiten

Die Ordnungen-Sammlung basiert auf [Sphinx](https://www.sphinx-doc.org/). Für das Verfassen und Bearbeiten von Dokumenten muss [reStructuredText](https://de.wikipedia.org/wiki/ReStructuredText) verwendet werden. Einen Anleitung dafür findet sich [hier](https://thomas-cokelaer.info/tutorials/sphinx/rest_syntax.html).

Beim Anlegen eines neuen Dokumentes sollte beachtet werden, dass dieses auch in der Datei `index.rst` eingetragen werden muss.
