# --------------------------------------------------------------- Imports ---------------------------------------------------------------- #

# System
from typing import Union, Dict, List, Tuple, Any, Hashable

# ---------------------------------------------------------------------------------------------------------------------------------------- #



# ------------------------------------------------------------ type: JSONData ------------------------------------------------------------ #

JSONData = Union[
    str, int, float, bool,
    Dict[Hashable, Any],
    List[Any],
    Tuple[Any]
]


# ---------------------------------------------------------------------------------------------------------------------------------------- #