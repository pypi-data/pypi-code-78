api = '''
# --------------------------------------------------------------- Imports ---------------------------------------------------------------- #

# System
from typing import Optional, Dict

# Pip
from ksimpleapi import Api

# Local


# ---------------------------------------------------------------------------------------------------------------------------------------- #



[CLASS_NAME_COMMENT_LINE]

class [CLASS_NAME](Api):

    # ---------------------------------------------------------- Overrides ----------------------------------------------------------- #

    @classmethod
    def extra_headers(cls) -> Optional[Dict[str, any]]:
        return {

        }


    # ------------------------------------------------------ Public properties ------------------------------------------------------- #




    # -------------------------------------------------------- Public methods -------------------------------------------------------- #




    # ------------------------------------------------------ Private properties ------------------------------------------------------ #




    # ------------------------------------------------------- Private methods -------------------------------------------------------- #




# ---------------------------------------------------------------------------------------------------------------------------------------- #
'''.strip()