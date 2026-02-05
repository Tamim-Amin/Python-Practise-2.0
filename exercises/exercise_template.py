"""
Exercise template

Description:
- Briefly describe the exercise here.

Usage:
- Run this file from the project root:

    python exercises\exercise_template.py

"""

import math


def sphere_volume(radius: float) -> float:
    """Return volume of a sphere with given radius."""
    return (4.0 / 3.0) * math.pi * radius ** 3


def main() -> None:
    try:
        r = float(input("Enter radius: "))
    except Exception:
        print("Invalid input; please enter a number.")
        return
    print(f"Volume for radius {r}: {sphere_volume(r):.4f}")


if __name__ == "__main__":
    main()
