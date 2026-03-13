#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_plant_types.py                                    :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: trakotos <trakotos@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/09 14:38:40 by trakotos            #+#    #+#            #
#   Updated: 2026/03/09 14:56:33 by trakotos           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


class Plant:
    def __init__(self, name: str, height: int, age: int):
        self._name = name
        self._height = height
        self._age = age


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self._color = color
        self._is_bloom = False

    def print_info(self):
        print(
            f"{self._name} (Flower): {self._height}cm, "
            f"{self._age} days, {self._color} color"
        )

    def bloom(self):
        self._is_bloom = True
        print(f"{self._name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter
        self._shade = None

    def print_info(self):
        print(
            f"{self._name} (Tree): {self._height}cm, "
            f"{self._age} days, {self._trunk_diameter}cm diameter"
        )

    def produce_shade(self, shade: int):
        self._shade = shade
        print(f"Oak provides {self._shade} square meters of shade")


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self._harvest_season = harvest_season
        self._nutritional_value = nutritional_value

    def print_info(self):
        print(
            f"{self._name} (Vegetable): {self._height}cm, "
            f"{self._age} days, {self._harvest_season} harvest"
        )
        print(f"Tomato is rich in {self._nutritional_value}")


if __name__ == "__main__":
    flowers_attributes: list[tuple[str, int, int, str]] = [
        ("Rose", 25, 30, "red"),
        ("Lily", 40, 45, "white"),
    ]
    trees_attributes: list[tuple[str, int, int, int]] = [
        ("Oak", 500, 1825, 50),
        ("Pine", 1200, 3650, 80),
    ]
    vegetables_attributes: list[tuple[str, int, int, str, str]] = [
        ("Tomato", 80, 90, "summer", "vitamin C"),
        ("Onion", 70, 95, "winter", "vitamin B"),
    ]
    flowers = []
    trees = []
    vegetables = []
    print("=== Garden Plant Types ===\n")
    for att in flowers_attributes:
        flowers += [Flower(*att)]
        flowers[-1].print_info()
        flowers[-1].bloom()
    print()
    for att in trees_attributes:
        trees += [Tree(*att)]
        trees[-1].print_info()
        trees[-1].produce_shade(78)
    print()
    for att in vegetables_attributes:
        vegetables += [Vegetable(*att)]
        vegetables[-1].print_info()
