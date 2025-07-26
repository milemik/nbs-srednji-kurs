from nbs_kurs.get_values_from_nbs import ValueData


def get_value_by_currency(short_name: str, data: list[ValueData]) -> list[ValueData]:
    return list(filter(lambda x: x.short_name == short_name, data))