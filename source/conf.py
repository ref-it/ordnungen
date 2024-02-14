# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'StuRa-Ordnungen'
copyright = 'Studierendenrat der TU Ilmenau'
author = 'Studierendenrat der TU Ilmenau'
release = ''

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx_rtd_theme',
    'sphinx.ext.autosectionlabel',
]

autosectionlabel_prefix_document = True

templates_path = ['_templates']
exclude_patterns = []

language = 'de'


# Internationalization

locale_dirs = ['locale/']   # path is example but recommended.
gettext_compact = False     # optional.



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_css_files = [
    'css/custom.css',
]
html_show_sourcelink = False
html_logo = "_static/logo.svg"
html_theme_options = {
    'logo_only': False,
    'display_version': True,
}
html_favicon = '_static/favicon.ico'


latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '11pt',
    'fontpkg': '\\usepackage{paratype}\\renewcommand*\\familydefault{\sfdefault}\\renewcommand\\ttdefault{txtt}',
    'fncychap': ''
}
