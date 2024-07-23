#!/usr/bin/env python3

import argparse
import re
from slugify import slugify
import sys
import yaml


def main():
    spec = yaml.load(sys.stdin.read(), yaml.SafeLoader)
    tags = set()

    for path_name, path in spec["paths"].items():
        for method_name, method in path.items():
            if method_name != "parameters" and "tags" in method and len(method["tags"]):
                for i, tag in enumerate(method["tags"]):
                    tag_slug = slugify(tag)
                    method["tags"][i] = tag_slug
                    method["operationId"] = f"{tag_slug}/{method["operationId"]}"
                    tags.add((tag_slug, tag))

    spec["tags"] = [{"name": tag_slug, "description": tag} for tag_slug, tag in tags]
    sys.stdout.write(yaml.dump(spec))
