import json
from pathlib import Path


resources_dir = Path(__file__).resolve().parents[1] / "resources"


def read_json_resource(file_name: str):
    with open(resources_dir / file_name, encoding="utf-8") as file:
        return json.load(file)
