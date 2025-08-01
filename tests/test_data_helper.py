from decimal import Decimal

import pytest

from nbs_kurs.data_helper import get_value_by_currency, get_currency_by_name
from nbs_kurs.get_values_from_nbs import ValueData


@pytest.fixture
def data_values():
    return [
        ValueData(short_name="USD", value_key=1, country="Russia", valid_for=1, value=Decimal("1.23")),
        ValueData(short_name="EUR", value_key=1, country="Europe", valid_for=1, value=Decimal("110.23")),
    ]


@pytest.mark.parametrize(
    ["short_names", "expected"],
    [
        (["EUR"], [ValueData(short_name="EUR", value_key=1, country="Europe", valid_for=1, value=Decimal("110.23"))]),
        (["USD"], [ValueData(short_name="USD", value_key=1, country="Russia", valid_for=1, value=Decimal("1.23"))]),
        (
            ["USD", "EUR"],
            [
                ValueData(short_name="USD", value_key=1, country="Russia", valid_for=1, value=Decimal("1.23")),
                ValueData(short_name="EUR", value_key=1, country="Europe", valid_for=1, value=Decimal("110.23")),
            ],
        ),
    ],
)
def test_get_value_by_currency(short_names, expected, data_values):
    res = get_value_by_currency(
        short_names=short_names,
        data=data_values,
    )

    assert res == expected


@pytest.mark.parametrize(
    ["name", "expected"],
    [
        ("EUR", ValueData(short_name="EUR", value_key=1, country="Europe", valid_for=1, value=Decimal("110.23"))),
        ("USD", ValueData(short_name="USD", value_key=1, country="Russia", valid_for=1, value=Decimal("1.23"))),
        ("GBP", None),
        ("", None),
    ],
)
def test_get_currency_by_name(name, expected, data_values):
    res = get_currency_by_name(
        name=name,
        data=data_values,
    )

    assert res == expected


def test_get_currency_by_name_empty_data():
    res = get_currency_by_name(
        name="USD",
        data=[],
    )

    assert res is None
