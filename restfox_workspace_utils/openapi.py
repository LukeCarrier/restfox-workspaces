#!/usr/bin/env python3

import argparse
import sys
import yaml


def main():
    # FIXME: try to fix duplicate aliases or out of order aliases and anchors.
    spec = yaml.load(sys.stdin.read(), yaml.SafeLoader)

    for path_name, path in spec["paths"].items():
        for method_name, method in path.items():
            if "summary" in method:
                method["summary"] = method["summary"].rstrip(".")
                if len(method["summary"]) > 100:
                    if "description" in method:
                        method["description"] = f"{method["summary"]}\n\n{method["description"]}"
                    else:
                        method["description"] = method["summary"]
                    method["summary"] = f"{method["summary"][:99]}…"

    sys.stdout.write(yaml.dump(spec))
