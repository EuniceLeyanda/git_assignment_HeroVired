import math

class GeometryCalculator:
    def calculate_circle_area1(self, radius):
        return math.pi * radius ** 2
    
    def calculate_circle_area2(self, diameter):
        return math.pi * radius

    def calculate_rectangle_area(self, length, width):
        return length * width

if __name__ == "__main__":
    calculator = GeometryCalculator()

    # TODO: Implement the feature to calculate the area of a circle

    radius = 5
    print(f"The area of the circle with radius {radius} ={calculator.calculate_circle_area1(radius)}")

    diameter = 6
    print(f"The area of the circle with radius {diameter} ={calculator.calculate_circle_area2(diameter)}")


    # TODO: Implement the feature to calculate the area of a rectangle # length = 10

    length = 5
    width = 6
    print(f"The area of the rectangle with length {length} and width {width} = {calculator.calculate_rectangle_area(length, width)}")
