# -*- coding: utf-8 -*-
"""
"""

from quantities.unitquantity import UnitTemperature

K = degK = kelvin = Kelvin = UnitTemperature(
    'Kelvin',
    symbol='K',
    aliases=['degK', 'kelvin']
)
degR = rankine = Rankine = UnitTemperature(
    'Rankine',
    K/1.8,
    symbol='degR',
    u_symbol='°R',
    aliases=['degR', 'rankine']
)
degC = celsius = Celsius = UnitTemperature(
    'Celsius',
    K,
    symbol='degC',
    u_symbol='°C',
    aliases=['degC', 'celsius']
)
degF = fahrenheit = Fahrenheit = UnitTemperature(
    'Fahrenheit',
    K,
    symbol='degF',
    u_symbol='°F',
    aliases=['degF', 'fahrenheit']
)
# Unicode has special compatibility characters for ℃ ℉, but their use is
# discouraged by the unicode consortium.
