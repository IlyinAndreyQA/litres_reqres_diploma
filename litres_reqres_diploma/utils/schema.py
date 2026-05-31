import json

from jsonschema import validate

from litres_reqres_diploma.utils.paths import schemas_dir


def validate_schema(response, schema_name: str) -> None:
    with open(schemas_dir / schema_name, encoding="utf-8") as schema_file:
        schema = json.load(schema_file)

    validate(instance=response.json(), schema=schema)

