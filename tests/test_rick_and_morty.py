from pytest_bdd import scenarios

# Import step definitions so pytest can register them
from step_defs.RickAndMorty.character_steps import *
from step_defs.RickAndMorty.navigation_steps import *

scenarios("../features/RickAndMorty")