#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math


def square_root(a: float) -> float:
    return a**(1/2)


def square(a: float) -> float:
    return a**2


def average(a: float, b: float, c: float) -> float:
    return sum([a, b, c]) / 3


#1 degre = 60 minutes, 1 minute = 60 secondes
def to_radians(angle_degs: float, angle_mins: float, angle_secs: float) -> float:
    convDegToRad = math.pi/180
    angle_mins += angle_secs/60
    angle_degs += angle_mins/60
    
    #return math.radians(angle_degs)
    return angle_degs*convDegToRad


#1 degre = 60 minutes, 1 minute = 60 secondes
def to_degrees(angle_rads: float) -> tuple:
    degs = round(180/math.pi * angle_rads, 0)
    minutes = 60 * 180/math.pi * angle_rads
    seconds = 60 * minutes
    
    return degs, minutes, seconds


def to_celsius(temperature: float) -> float:
    return (temperature - 32)/(9/5)


def to_farenheit(temperature: float) -> float :
    return temperature * (9/5) + 32


def main() -> None :
    print(f"La racine carré de 144 est : {square_root(144)}")

    print(f"Le carré de 12 est : {square(12)}")

    print(f"Moyenne des nombres 2, 4, 6: {average(2, 4, 6)}")

    print(f"Conversion de 100 degres, 2 minutes et 45 secondes en radians: {to_radians(180, 2, 45)}")

    degrees, minutes, seconds = to_degrees(1.0)
    print(f"Conversion de 1 radian en degres: {degrees} degres, {minutes} minutes et {seconds} secondes")

    print(f"Conversion de 100 Celsius en Farenheit: {to_farenheit(100.0)}")
    print(f"Conversion de 451 Farenheit en Celsius: {to_celsius(451.0)}")


if __name__ == '__main__':
    main()
