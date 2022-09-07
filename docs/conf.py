from datetime import date

from myst_parser import __version__
from sphinx.application import Sphinx

project = "copier_python_test"
copyright = f"{date.today().year}, Executable Book Project"  # noqa: A001
author = "Blake Naccarato"
version = __version__
master_doc = "index"
language = "en"
extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx_autodoc_typehints",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
    "sphinx_design",
    "sphinxext.rediraffe",
]
templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
html_theme = "sphinx_book_theme"
html_theme_options = {
    "home_page_in_toc": True,
    "github_url": "https://github.com/executablebooks/MyST-Parser",
    "repository_url": "https://github.com/executablebooks/MyST-Parser",
    "repository_branch": "master",
    "path_to_docs": "docs",
    "use_repository_button": True,
    "use_edit_page_button": True,
}
html_static_path = ["_static"]
myst_enable_extensions = [
    "dollarmath",
    "amsmath",
    "deflist",
    "fieldlist",
    "html_admonition",
    "html_image",
    "colon_fence",
    "smartquotes",
    "replacements",
    "linkify",
    "strikethrough",
    "substitution",
    "tasklist",
]
myst_number_code_blocks = ["typescript"]
myst_heading_anchors = 2
myst_footnote_transition = True
myst_dmath_double_inline = True
rediraffe_redirects = {
    "using/intro.md": "sphinx/intro.md",
    "sphinx/intro.md": "intro.md",
    "using/use_api.md": "api/index.md",
    "api/index.md": "api/reference.rst",
    "using/syntax.md": "syntax/syntax.md",
    "using/syntax-optional.md": "syntax/optional.md",
    "using/reference.md": "syntax/reference.md",
    "sphinx/reference.md": "configuration.md",
    "sphinx/index.md": "faq/index.md",
    "sphinx/use.md": "faq/index.md",
    "sphinx/faq.md": "faq/index.md",
    "explain/index.md": "develop/background.md",
}
suppress_warnings = ["myst.strikethrough"]
intersphinx_mapping = {
    "python": ("https://docs.python.org/3.7", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master", None),
    "markdown_it": ("https://markdown-it-py.readthedocs.io/en/latest", None),
}
autodoc_member_order = "bysource"
nitpicky = True
nitpick_ignore = [
    ("py:class", "docutils.nodes.document"),
    ("py:class", "docutils.nodes.docinfo"),
    ("py:class", "docutils.nodes.Element"),
    ("py:class", "docutils.nodes.Node"),
    ("py:class", "docutils.nodes.field_list"),
    ("py:class", "docutils.nodes.problematic"),
    ("py:class", "docutils.nodes.pending"),
    ("py:class", "docutils.nodes.system_message"),
    ("py:class", "docutils.statemachine.StringList"),
    ("py:class", "docutils.parsers.rst.directives.misc.Include"),
    ("py:class", "docutils.parsers.rst.Parser"),
    ("py:class", "docutils.utils.Reporter"),
    ("py:class", "nodes.Element"),
    ("py:class", "nodes.Node"),
    ("py:class", "nodes.system_message"),
    ("py:class", "Directive"),
    ("py:class", "Include"),
    ("py:class", "StringList"),
    ("py:class", "DocutilsRenderer"),
    ("py:class", "MockStateMachine"),
]


def setup(app: Sphinx):
    """Add functions to the Sphinx setup."""
    from myst_parser._docs import (
        DirectiveDoc,
        DocutilsCliHelpDirective,
        MystConfigDirective,
    )

    app.add_css_file("custom.css")
    app.add_directive("myst-config", MystConfigDirective)
    app.add_directive("docutils-cli-help", DocutilsCliHelpDirective)
    app.add_directive("doc-directive", DirectiveDoc)
