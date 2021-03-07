import logging
from typing import Any, Dict, Optional

from checkov.common.util.type_forcers import convert_str_to_bool
from checkov.terraform.parser_utils import eval_string, split_merge_args, string_to_native, to_string

#
# Functions defined in this file implement terraform functions.
#
# Inputs:
#   - First arg (unnamed) - the value string provided to the function
#   - "var_resolver" - function pointer to resolve variable/local references and such
#   - "function_name" - name of the function being called (mainly useful for error reporting when a
#                       function isn't defined)
# These may be expanded over time, so accepting kwargs (via `**`) is recommended.
#
# If the value cannot be processed, `FUNCTION_FAILED` should be returned.
#

FUNCTION_FAILED = "____FUNCTION_FAILED____"


def merge(original, var_resolver, **_):
    # https://www.terraform.io/docs/language/functions/merge.html
    args = split_merge_args(original)
    if args is None:
        return FUNCTION_FAILED
    merged_map = {}
    for arg in args:
        if arg.startswith("{"):
            arg_value = string_to_native(arg)
            if arg_value is None:
                return FUNCTION_FAILED
        else:
            arg_value = var_resolver(arg)
        if isinstance(arg_value, dict):
            merged_map.update(arg_value)
        else:
            return FUNCTION_FAILED  # don't know what this is, blow out
    return merged_map


def concat(original, var_resolver, **_):
    # https://www.terraform.io/docs/language/functions/concat.html
    args = split_merge_args(original)
    if args is None:
        return FUNCTION_FAILED
    merged_list = []
    for arg in args:
        if arg.startswith("["):
            value = eval_string(arg)
            if value is None:
                logging.debug("Unable to convert to list: %s", arg)
                return FUNCTION_FAILED
        else:
            value = var_resolver(arg)
        if isinstance(value, list):
            merged_list.extend(value)
        else:
            return FUNCTION_FAILED  # don't know what this is, blow out
    return merged_list


def tobool(original, **_):
    # https://www.terraform.io/docs/configuration/functions/tobool.html
    bool_value = convert_str_to_bool(original)
    return bool_value if isinstance(bool_value, bool) else FUNCTION_FAILED


def tonumber(original, **_):
    # https://www.terraform.io/docs/configuration/functions/tonumber.html
    if original.startswith('"') and original.endswith('"'):
        original = original[1:-1]
    try:
        if "." in original:
            return float(original)
        else:
            return int(original)
    except ValueError:
        return FUNCTION_FAILED

    
def tostring(original, **_):
    # Indicates a safe string, all good
    if original.startswith('"') and original.endswith('"'):
        return original[1:-1]
    # Otherwise, need to check for valid types (number or bool)
    bool_value = convert_str_to_bool(original)
    if isinstance(bool_value, bool):
        return bool_value
    else:
        try:
            if "." in original:
                return str(float(original))
            else:
                return str(int(original))
        except ValueError:
            return FUNCTION_FAILED  # no change


def tolist(original, **_):
    # https://www.terraform.io/docs/configuration/functions/tolist.html
    altered_value = eval_string(original)
    if altered_value is None:
        return FUNCTION_FAILED
    return altered_value if isinstance(altered_value, list) else list(altered_value)


def toset(original, **_):
    # https://www.terraform.io/docs/configuration/functions/toset.html
    altered_value = eval_string(original)
    if altered_value is None:
        return FUNCTION_FAILED
    return altered_value if isinstance(altered_value, set) else set(altered_value)


def tomap(original, **_):
    # https://www.terraform.io/docs/language/functions/tomap.html
    original = original.replace(":", "=")     # converted to colons by parser #shrug

    altered_value = eval_string(original)
    if altered_value is None or not isinstance(altered_value, dict):
        return FUNCTION_FAILED
    return _check_map_type_consistency(altered_value)


def map(original, **_):
    # https://www.terraform.io/docs/language/functions/map.html

    # NOTE: Splitting by commas is annoying due to possible commas in strings. To avoid
    #       the issue, act like it's a list (to allow comma separation) and let the HCL
    #       parser deal with it. Then iterating the list is easy.
    converted_to_list = eval_string(f"[{original}]")
    if converted_to_list is None or len(converted_to_list) & 1:       # none or odd number of args
        return FUNCTION_FAILED

    new_map = {}
    for i in range(0, len(converted_to_list), 2):
        new_map[converted_to_list[i]] = converted_to_list[i + 1]
    return _check_map_type_consistency(new_map)


def _check_map_type_consistency(value: Dict) -> Dict:
    # If there is a string and anything else, convert to string
    had_string = False
    had_something_else = False
    for k, v in value.items():
        if v == "${True}":
            value[k] = True
            v = True
        elif v == "${False}":
            value[k] = False
            v = False

        if isinstance(v, str):
            had_string = True
            if had_something_else:
                break
        else:
            had_something_else = True
            if had_string:
                break
    if had_string and had_something_else:
        value = {k: to_string(v) for k, v in value.items()}
    return value
