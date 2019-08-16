#!/usr/bin/env python3
import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from orggraph.jobs import Jobs

jobs = Jobs("data/jobs.yaml")

for job in jobs.jobs():
    print(job.title)

    if job.salary["lowest"] != job.salary["highest"]:
        print(f"  == pays between {job.salary['lowest']} and {job.salary['highest']} (median {job.salary['median']})")
    else:
        print(f"  == pays {job.salary['highest']}")
