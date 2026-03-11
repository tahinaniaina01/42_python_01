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

    def grow(self):
        self.height += 1
        print(f"{self.name} grew 1cm")


class FloweringPlant(Plant):
    def __init__(self, name, height, color):
        super().__init__(name, height)
        self.color = color
        self.is_bloom = True


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, color, prize_point):
        super().__init__(name, height, color)
        self.prize_point = prize_point


class GardenManager:
    total_garder = 0

    class GardenStats:
        def __init__(self):
            pass

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
    def create_garden_network(cls):
        pass
