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


class Plant:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height
        self.type = "regular"

    def grow(self):
        self.height += 1
        print(f"{self.name} grew 1cm")


class FloweringPlant(Plant):
    def __init__(self, name, height, color):
        super().__init__(name, height)
        self.type = "flowering"
        self.color = color
        self.is_bloom = True


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, color, prize_point):
        super().__init__(name, height, color)
        self.prize_point = prize_point
        self.type = "prize flowers"


class GardenManager:
    total_garder = 0

    def __init__(self, owner: str):
        self.owner = owner
        self.plants = []
        self.total_plants = 0
        self.total_grow = 0

    def add_plant(self, plant: Plant):
        self.plants += [plant]
        self.total_plants += 1
        print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_all_plants(self):
        for plant in self.plants:
            plant.grow()
            self.total_grow += 1

    @classmethod
    def create_garden_network(cls, owners: list[str]):
        gardens = [cls(o) for o in owners]
        return gardens

    class GardenStats:
        @staticmethod
        def count_plant_type(plants):
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
    print()
    print(GardenManager.GardenStats.count_plant_type(gardens[0].plants))
