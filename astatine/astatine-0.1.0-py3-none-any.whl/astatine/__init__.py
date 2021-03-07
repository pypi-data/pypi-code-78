#!/usr/bin/env python3
#
#  __init__.py
"""
Some handy helper functions for Python's AST module.
"""
#
#  Copyright © 2021 Dominic Davis-Foster <dominic@davis-foster.co.uk>
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
#  EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
#  MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
#  IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
#  DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
#  OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
#  OR OTHER DEALINGS IN THE SOFTWARE.
#
#  mark_text_ranges from Thonny
#  https://github.com/thonny/thonny/blob/master/thonny/ast_utils.py
#  Copyright (c) 2020 Aivar Annamaa
#  MIT Licensed
#

# stdlib
import ast
from typing import Optional, Tuple, Type, Union

# 3rd party
from asttokens.asttokens import ASTTokens  # type: ignore
from domdf_python_tools.stringlist import StringList

Str: Tuple[Type, ...]
Constant: Tuple[Type, ...]
Expr: Tuple[Type, ...]

try:  # pragma: no cover
	# 3rd party
	import typed_ast.ast3
	Str = (ast.Str, typed_ast.ast3.Str)
	Constant = (
			ast.Constant,
			typed_ast.ast3.Constant,  # type: ignore
			)
	Expr = (ast.Expr, typed_ast.ast3.Expr)

except ImportError:  # pragma: no cover
	Str = (ast.Str, )
	Constant = (ast.Constant, )
	Expr = (ast.Expr, )

__author__: str = "Dominic Davis-Foster"
__copyright__: str = "2021 Dominic Davis-Foster"
__license__: str = "MIT License"
__version__: str = "0.1.0"
__email__: str = "dominic@davis-foster.co.uk"

__all__ = ["get_docstring_lineno", "get_toplevel_comments", "is_type_checking", "mark_text_ranges"]


def get_toplevel_comments(source: str) -> StringList:
	"""
	Returns a list of comment lines from ``source`` which occur before the first line of source code
	(including before module-level docstrings).

	:param source:
	"""  # noqa: D400

	comments = StringList()

	for line in source.splitlines():
		if not line.startswith('#'):
			break

		comments.append(line)

	comments.blankline(ensure_single=True)

	return comments


def is_type_checking(node: ast.AST) -> bool:
	"""
	Returns whether the given ``if`` block is ``if typing.TYPE_CHECKING`` or equivalent.

	:param node:
	"""

	if isinstance(node, ast.If):
		node = node.test

	if isinstance(node, ast.NameConstant) and node.value is False:
		return True
	elif isinstance(node, ast.Name) and node.id == "TYPE_CHECKING":
		return True
	elif isinstance(node, ast.Attribute) and node.attr == "TYPE_CHECKING":
		return True
	elif isinstance(node, ast.BoolOp):
		for value in node.values:
			if is_type_checking(value):
				return True

	return False


def mark_text_ranges(node: ast.AST, source: str):
	"""
	Recursively add the ``end_lineno`` and ``end_col_offset`` attributes to each child of ``node``
	which already has the attributes ``lineno`` and ``col_offset``.

	:param node: An AST node created with :func:`ast.parse`.
	:param source: The corresponding source code for the node.
	"""  # noqa: D400

	ASTTokens(source, tree=node)

	for child in ast.walk(node):
		if hasattr(child, "last_token"):
			child.end_lineno, child.end_col_offset = child.last_token.end  # type: ignore

			if hasattr(child, "lineno"):
				# Fixes problems with some nodes like binop
				child.lineno, child.col_offset = child.first_token.start  # type: ignore


def get_docstring_lineno(node: Union[ast.FunctionDef, ast.ClassDef, ast.Module], ) -> Optional[int]:
	"""
	Returns the line number of the start of the docstring for ``node``.

	:param node:

	.. warning::

		On CPython 3.6 and 3.7 the line number may not be correct, due to https://bugs.python.org/issue16806.

		CPython 3.8 and above are unaffected, as are PyPy 3.6 and 3.7

		Accurate line numbers on CPython 3.6 and 3.7 may be obtained by using https://github.com/domdfcoding/typed_ast,
		which contains the backported fix from Python 3.8.

	"""

	if not (node.body and isinstance(node.body[0], Expr)):  # pragma: no cover
		return None

	body = node.body[0].value  # type: ignore

	if isinstance(body, Constant) and isinstance(body.value, str):  # pragma: no cover (<py38)
		return body.lineno
	elif isinstance(body, Str):  # pragma: no cover (py38+)
		return body.lineno
	else:  # pragma: no cover
		return None
