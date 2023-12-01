import os
from pathlib import Path

for i in range(2, 26):
    folder = format(i, "02d")
    os.makedirs(Path("2023", folder))
    with open(Path("2023", folder, "solution.py"), "w") as fp:
        pass
    with open(Path("2023", folder, "in.txt"), "w") as fp:
        pass
