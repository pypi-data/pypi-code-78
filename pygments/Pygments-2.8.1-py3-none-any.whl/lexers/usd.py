"""
    pygments.lexers.usd
    ~~~~~~~~~~~~~~~~~~~

    The module that parses Pixar's Universal Scene Description file format.

    :copyright: Copyright 2006-2021 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

from pygments.lexer import RegexLexer, bygroups
from pygments.lexer import words as words_
from pygments.lexers._usd_builtins import COMMON_ATTRIBUTES, KEYWORDS, \
    OPERATORS, SPECIAL_NAMES, TYPES
from pygments.token import Comment, Keyword, Name, Number, Operator, \
    Punctuation, String, Text, Whitespace

__all__ = ["UsdLexer"]


def _keywords(words, type_):
    return [(words_(words, prefix=r"\b", suffix=r"\b"), type_)]


_TYPE = r"(\w+(?:\[\])?)"
_BASE_ATTRIBUTE = r"(\w+(?:\:\w+)*)(?:(\.)(timeSamples))?"
_WHITESPACE = r"([ \t]+)"


class UsdLexer(RegexLexer):
    """
    A lexer that parses Pixar's Universal Scene Description file format.

    .. versionadded:: 2.6
    """

    name = "USD"
    aliases = ["usd", "usda"]
    filenames = ["*.usd", "*.usda"]

    tokens = {
        "root": [
            (r"(custom){_WHITESPACE}(uniform)(\s+){}(\s+){}(\s*)(=)".format(
                _TYPE, _BASE_ATTRIBUTE, _WHITESPACE=_WHITESPACE),
             bygroups(Keyword.Token, Whitespace, Keyword.Token, Whitespace,
                      Keyword.Type, Whitespace, Name.Attribute, Text,
                      Name.Keyword.Tokens, Whitespace, Operator)),
            (r"(custom){_WHITESPACE}{}(\s+){}(\s*)(=)".format(
                _TYPE, _BASE_ATTRIBUTE, _WHITESPACE=_WHITESPACE),
             bygroups(Keyword.Token, Whitespace, Keyword.Type, Whitespace,
                      Name.Attribute, Text, Name.Keyword.Tokens, Whitespace,
                      Operator)),
            (r"(uniform){_WHITESPACE}{}(\s+){}(\s*)(=)".format(
                _TYPE, _BASE_ATTRIBUTE, _WHITESPACE=_WHITESPACE),
             bygroups(Keyword.Token, Whitespace, Keyword.Type, Whitespace,
                      Name.Attribute, Text, Name.Keyword.Tokens, Whitespace,
                      Operator)),
            (r"{}{_WHITESPACE}{}(\s*)(=)".format(
                _TYPE, _BASE_ATTRIBUTE, _WHITESPACE=_WHITESPACE),
             bygroups(Keyword.Type, Whitespace, Name.Attribute, Text,
                      Name.Keyword.Tokens, Whitespace, Operator)),
        ] +
        _keywords(KEYWORDS, Keyword.Tokens) +
        _keywords(SPECIAL_NAMES, Name.Builtins) +
        _keywords(COMMON_ATTRIBUTES, Name.Attribute) +
        [(r"\b\w+:[\w:]+\b", Name.Attribute)] +
        _keywords(OPERATORS, Operator) +  # more attributes
        [(type_ + r"\[\]", Keyword.Type) for type_ in TYPES] +
        _keywords(TYPES, Keyword.Type) +
        [
            (r"[(){}\[\]]", Punctuation),
            ("#.*?$", Comment.Single),
            (",", Punctuation),
            (";", Punctuation),  # ";"s are allowed to combine separate metadata lines
            ("=", Operator),
            (r"[-]*([0-9]*[.])?[0-9]+(?:e[+-]*\d+)?", Number),
            (r"'''(?:.|\n)*?'''", String),
            (r'"""(?:.|\n)*?"""', String),
            (r"'.*?'", String),
            (r'".*?"', String),
            (r"<(\.\./)*([\w/]+|[\w/]+\.\w+[\w:]*)>", Name.Namespace),
            (r"@.*?@", String.Interpol),
            (r'\(.*"[.\\n]*".*\)', String.Doc),
            (r"\A#usda .+$", Comment.Hashbang),
            (r"\s+", Whitespace),
            (r"\w+", Text),
            (r"[_:.]+", Punctuation),
        ],
    }
