# Configuration file for the Sphinx documentation builder.

project = 'OSDR Tutorials'
copyright = '2024, GeneLab'
author = 'GeneLab'
version = 'latest'

# Inject project name into rst files if needed
rst_epilog = f"""
.. |project_name| replace:: {project}
"""

# Add extensions
extensions = [
    'myst_parser',
    'sphinx_markdown_tables',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.intersphinx', # To do: implement
    'sphinx_copybutton',
    'sphinx_design',
    'hoverxref.extension',
    'sphinx_rtd_theme'
]

autosectionlabel_prefix_document = True 

# Myst extension's extensions
myst_enable_extensions = [
    "dollarmath",  # Enables $ signs for math
    "amsmath",     # Supports more complex math via LaTeX
    "deflist",     # Definition lists
    "html_admonition",  # TO do: implement
    "html_image",  # Render plain html img tags in docs  
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# Custom Styling
html_title = project
html_logo = "_static/images/OSDR_logos.png"
html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'display_version': False,
    'style_nav_header_background': "#105bd8",
    'sticky_navigation': True
}
html_static_path = ['_static']
html_css_files = ['css/custom.css']
html_show_sphinx = False
html_show_copyright = False

# Intersphinx mapping
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}

# To do: Implement glossary term hover 
# Hover configuration
hoverxref_auto_ref = True
hoverxref_api_host = 'https://readthedocs.org'
hoverxref_roles = ['term', 'ref']
hoverxref_role_types = {
    'term': 'tooltip',
    'ref': 'tooltip',
}


html_context = {
    "display_github": True,
    "github_user": "nasa",
    "github_repo": "OSDR_Tutorials",
    "github_version": "main",
    "conf_py_path": "/source/"
}
