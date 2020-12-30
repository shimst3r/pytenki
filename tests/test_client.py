"""
test_client is a suite of integration tests for the internal wttr.io client.
"""
from pytenki import WttrClient

import pytest


@pytest.fixture
def client():
    client = WttrClient()

    return client


def test_client_get(client):
    data = client.get()

    assert "Morning" in data
    assert "Noon" in data
    assert "Evening" in data
    assert "Night" in data


def test_client_get_in_german(client):
    data = client.get(lang="de")

    assert "Früh" in data
