#!/usr/bin/env python

import json
from pathlib import Path
import re


def main():
    allVehicles = json.loads(Path('combined_results.json').read_text())

    result = [x for x in allVehicles if x['trim'] == 'Premium']

    result = [x for x in result if re.match(r"[Rr]ed", x['exteriorColor'])]

    crossedOffVins = Path('crossedOffVins.txt').read_text().splitlines()

    result = [x for x in result if x['vin'] not in crossedOffVins]
    print(json.dumps(result, indent=4))


if __name__ == "__main__":
    main()
