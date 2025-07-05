from pytest_bdd import scenarios

# Import step definitions so pytest can register them
from step_defs.RickAndMorty.api_steps import *

scenarios("../features/RickAndMorty/rickandmorty_api.feature")