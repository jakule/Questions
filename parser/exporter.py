from json import JSONEncoder


def save_as_json(filename: str, obj) -> None:
    """
    Export object as json. This function declares own JSON exporter,
    so can be used with none exportable data structures.
    :param filename: The name of JSON file
    :param obj: Generic object that will be saved
    """
    class Encoder(JSONEncoder):
        def default(self, o):
            return o.__dict__

    db = Encoder().encode(obj)
    with open(filename, "w") as f:
        f.write(db)
