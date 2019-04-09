from checkio_referee import RefereeRank, ENV_NAME



import settings_env
from tests import TESTS


class Referee(RefereeRank):
    TESTS = TESTS
    ENVIRONMENTS = settings_env.ENVIRONMENTS

    DEFAULT_FUNCTION_NAME = "find_message"
    FUNCTION_NAMES = {
        "python_3": "find_message",
        "js_node": "findMessage"
    }
    ENV_COVERCODE = {
        
    }