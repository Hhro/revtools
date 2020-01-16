import subprocess
from ..log import logger

def extract_asar(asar, dest=None):
    args = ["asar"]

    args += ["extract", asar, dest]

    print(
        ("  RUN: '" + " ".join(args)+"'")
    )
    subprocess.run(args)