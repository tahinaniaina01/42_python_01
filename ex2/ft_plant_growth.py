#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_plant_growth.py                                   :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: trakotos <trakotos@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/06 10:33:30 by trakotos            #+#    #+#            #
#   Updated: 2026/03/06 10:57:00 by trakotos           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.__name = name
        self.__height = height
        self.__age = age
        self.__grow = 0

    def print_info(self):
        print(f"{self.__name}: {self.__height}cm, {self.__age} days old")

    def grow(self):
        self.__grow += 1
        self.__height += 1

    def age(self):
        self.__age += 1

    def get_info(self):
        return (self.__name, self.__height, self.__age, self.__grow)


if __name__ == "__main__":
    plant = Plant("Rose", 25, 30)
    days = 7
    for day in range(1, days):
        if day == 1:
            print("=== Day 1 ===")
            plant.print_info()
        plant.age()
        plant.grow()
    print(f"=== Day {days} ===")
    plant.print_info()
    _, _, _, grow = plant.get_info()
    print(f"Growth this week: +{grow}cm")
