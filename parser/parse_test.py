import pytest

from parser.parse import remove_clutter


@pytest.mark.parametrize(
    "input_string",
    (
        "ACP - 45 JIRA   ADMINISTRATION     80   CertMagic.net",
        "ACP-100 JIRA ADMINISTRATION  98 CertMagic.net",
        "ACP-100 JIRA ADMINISTRATION  101 \n\tCertMagic.net",  # noqa
    ),
)
def test_remove_simple_clutter(input_string: str):
    result = remove_clutter(input_string)
    assert not result
