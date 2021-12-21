def find_area(length, width, square_feet=43560):
    """
    Function takes values as area length and width, and coverts it into acre.
    Args:
        length: float or int
        width: float or int
        sqaure_feet: default value 43560
    return:
        converted value of total area in acre 
    """
    area_in_acre = length * width / square_feet
    return area_in_acre
