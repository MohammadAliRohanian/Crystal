# Post and get the user with same id that post
import sys

sys.path.append("B:/Code/crystal")

import os

from datetime import datetime
from database.models.run_model import *
from database.repositories.run_db import *

# Import test cases
from cases.user.post_user import *
from cases.user.get_user import *

# Start run
name = os.path.basename(__file__)
run_started_at = datetime.now()
description = "create user then get user to see if it exists"
results = []
run_id = init_run(name, run_started_at, description)
run = run_model()

# Test cases
res = post_user_1_happy(run_id)

res = get_user_2_happy(run_id, res["result"]["id"])

# Check run overall result
run_result = "Fail"
if res["result"]["id"] != None:
    run_result = "Pass"

# End run
run_ended_at = datetime.now()
run.append(run_result, run_started_at, run_ended_at, run_id)
finalize_run(run)
