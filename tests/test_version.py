"""
test_version ensures that nobody screws up the package version over time. :)
"""


def test_version():
    from pytenki import __version__

    assert __version__ == "0.1.0"
