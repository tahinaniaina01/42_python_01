#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_garden_security.py                                :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: trakotos <trakotos@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/09 13:52:20 by trakotos            #+#    #+#            #
#   Updated: 2026/03/09 14:37:52 by trakotos           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


class Plant:
    def __init__(self, name: str, age: int, height: int) -> None:
        self.__name = name
        self.__height = None
        self.__age = None
        print(f"Plant created: {self.__name}")
        self.set_height(height)
        self.set_age(age)

    def set_height(self, height: int) -> None:
        if height >= 0:
            self.__height = height
            print(f"Height updated: {self.__height}cm [OK]")
        else:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")

    def set_age(self, age: int) -> None:
        if age >= 0:
            self.__age = age
            print(f"Age updated: {self.__age} days [OK]")
        else:
            print(f"Invalid operation attempted: age {age}cm [REJECTED]")
            print("Security: Negative age rejected")

    def get_height(self) -> int:
        return self.__height

    def get_age(self) -> int:
        return self.__age


if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant = Plant("Rose", 25, 30)
    print()
    plant.set_height(-5)
    print()
    print(
        f"Current plant: Rose ({plant.get_height()}cm, "
        f"{plant.get_age()} days)"
    )
