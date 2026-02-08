from pytest_bdd import scenarios

# Import step definitions so pytest can register them
from step_defs.rick_and_morty.character_steps import *
from step_defs.rick_and_morty.navigation_steps import *

scenarios("../features/rick_and_morty/rickandmorty_ui.feature")
