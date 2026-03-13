#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_garden_analytics.py                               :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: trakotos <trakotos@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/11 16:50:27 by trakotos            #+#    #+#            #
#   Updated: 2026/03/11 18:00:39 by trakotos           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from typing import Self


class Plant:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height
        self.type = "regular"

    def grow(self) -> None:
        self.height += 1
        print(f"{self.name} grew 1cm")

    def print_info(self) -> None:
        print(f"{self.name}: {self.height}cm")


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, color: str):
        super().__init__(name, height)
        self.type = "flowering"
        self.color = color
        self.is_bloom = True

    def print_info(self) -> None:
        print(
            f"{self.name}: {self.height}cm, {self.color} flowers "
            f"{'(blooming)' if self.is_bloom else ''}"
        )


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, color: str, prize_point: int):
        super().__init__(name, height, color)
        self.prize_point = prize_point
        self.type = "prize flowers"

    def print_info(self) -> None:
        print(
            f"{self.name}: {self.height}cm, {self.color} flowers "
            f"{'(blooming)' if self.is_bloom else ''}, "
            f"Prize points: {self.prize_point}"
        )


class GardenManager:
    total_garder = 0

    def __init__(self, owner: str):
        self.owner = owner
        self.plants = []
        self.total_plants = 0
        self.total_grow = 0
        self.score = 0

    def add_plant(self, plant: Plant) -> None:
        self.plants += [plant]
        self.total_plants += 1
        print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_all_plants(self) -> None:
        for plant in self.plants:
            plant.grow()
            self.total_grow += 1

    @classmethod
    def create_garden_network(
        cls: type[Self], owners: list[str]
    ) -> list[Self]:
        gardens = []
        for o in owners:
            gardens += [cls(o)]
            cls.total_garder += 1
        return gardens

    @staticmethod
    def validate_height(gardens: list[Self]) -> bool:
        for garden in gardens:
            for plant in garden.plants:
                if plant.height < 0:
                    return False
        return True

    class GardenStats:
        @staticmethod
        def count_plant_type(plants: list[Plant]) -> tuple[int, int, int]:
            regular = 0
            flowering = 0
            prize_flowers = 0
            for plant in plants:
                if plant.type == "regular":
                    regular += 1
                elif plant.type == "flowering":
                    flowering += 1
                elif plant.type == "prize flowers":
                    prize_flowers += 1
            return regular, flowering, prize_flowers


if __name__ == "__main__":
    owners = ["Alice", "Bob"]
    gardens = GardenManager.create_garden_network(owners)

    print("=== Garden Management System Demo ===\n")
    gardens[0].add_plant(Plant("Oak tree", 30))
    gardens[0].add_plant(FloweringPlant("Rose", 26, "red"))
    gardens[0].add_plant(PrizeFlower("Sunflower", 51, "yellow", 10))

    print("\nAlice is helping all plants grow...")
    gardens[0].grow_all_plants()

    print(f"\n=== {gardens[0].owner}'s Garden Report ===")
    print("Plants in garden:")
    for plant in gardens[0].plants:
        print(end="- ")
        plant.print_info()
    print()

    print(
        f"Plants added: {gardens[0].total_plants}, "
        f"Total growth: {gardens[0].total_grow}cm"
    )
    r, f, p = GardenManager.GardenStats.count_plant_type(
        gardens[0].plants
    )
    print(
        f"Plant types: {r} regular, {f} "
        f"flowering, {p} prize flowers"
    )
    print()

    print(f"Height validation test: {GardenManager.validate_height(gardens)}")
    print("Garden scores - ", end="")
    scores = [218, 92]
    i = 0
    for garden in gardens:
        garden.score = scores[i]
        print(f"{garden.owner}: {garden.score}", end="")
        if garden != gardens[-1]:
            print(end=", ")
        i += 1
    print()
    print(f"Total gardens managed: {GardenManager.total_garder}")
