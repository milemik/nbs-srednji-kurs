from nbs_kurs.get_values_from_nbs import ValueData


def _print_line() -> None:
    print("--------------------------------------------------")

def print_results(value_data: list[ValueData]) -> None:
    for value in value_data:
        _print_line()
        print(f"OZNAKA VALUTE: {value.short_name}")
        print(f"SIFRA VALUTE: {value.value_key}")
        print(f"ZEMLJA: {value.country}")
        print(f"VAZI ZA: {value.valid_for}")
        print(f"SREDNI KURS: {value.value}")