from pytest_bdd import scenarios

# Import step definitions so pytest can register them
from step_defs.AutomationExercise.ecommerce_steps import *
from step_defs.AutomationExercise.navigation_steps import *
from step_defs.AutomationExercise.user_management_steps import *

scenarios("../features/AutomationExercise")
