from pytest_bdd import scenarios

# Import step definitions so pytest can register them
from step_defs.automation_exercise.ecommerce_steps import *
from step_defs.automation_exercise.navigation_steps import *
from step_defs.automation_exercise.user_management_steps import *

scenarios("../features/automation_exercise")
