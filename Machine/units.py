from dataclasses import dataclass
from typing import Dict


@dataclass
class CurrencyUnit:
    unit: str
    value: float


_jod_units = [
    CurrencyUnit("100 fills", 0.1),
    CurrencyUnit("Quarter JD", 0.25),
    CurrencyUnit("Half JD", 0.5),
    CurrencyUnit("1 JD", 1),
    CurrencyUnit("5 JD", 5),
    CurrencyUnit("10 JD", 10)
]

jod_units: Dict[str, CurrencyUnit] = {jod_unit.unit: jod_unit for jod_unit in _jod_units}
