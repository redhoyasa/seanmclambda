import json
from tempfile import NamedTemporaryFile

import requests

BASE_URL = "https://kroki.io/"
DIAGRAM_TYPE = "vegalite"


def get_graph(diagram_source, output_format="png"):
    header = {
        "Content-Type": "application/json"
    }
    data = {
        "diagram_source": json.dumps(diagram_source),
        "diagram_type": DIAGRAM_TYPE,
        "output_format": output_format
    }
    response = requests.post(BASE_URL, headers=header, data=json.dumps(data), stream=True)
    if not response.ok:
        raise Exception("failed to get graph")

    with NamedTemporaryFile(delete=False) as f:
        f.write(response.content)
        return f

    return None
