############
# Part 1   #
############


class MelonType:
    """A species of melon at a melon farm."""

    def __init__(
        self, code, name, first_harvest, color, is_seedless, is_bestseller
    ):
        """Initialize a melon."""

        self.pairings = []

        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name
        

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        # Fill in the rest
        self.pairings.append(pairing)
        
    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        # Fill in the rest
        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    # Fill in the rest
    musk = MelonType("musk", "Muskmelon", 1998, "green", True, True)
    musk.add_pairing("mint")
    all_melon_types.append(musk)
    cas = MelonType("cas", "Casaba", 2003, "orange", True, False)
    all_melon_types.append(cas)
    cas.add_pairing("strawberrys")
    cas.add_pairing("mint")
    cren = MelonType("cren", "Crenshaw", 1996, "green", True, False)  
    cren.add_pairing("prosciutto")  
    all_melon_types.append(cren)
    yw = MelonType("yw", "Yellow Watermelon", 2013, "yellow", True, True)
    yw.add_pairing("ice cream")
    all_melon_types.append(yw)
    

    return all_melon_types

make_melon_types()

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    # Fill in the rest
    for melon in melon_types:
        print(f"{melon.name} pairs with")
        for pairing in melon.pairings:
            print(f"- {pairing}")

print_pairing_info(make_melon_types())

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melon_dict = {}

    for melon in melon_types:
        melon_dict[melon.code] = melon.name
    
    print(melon_dict)
    return melon_dict

make_melon_type_lookup(make_melon_types())

############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods
    def __init__(self, code, shape, color, field_num, harvested_by):

        self.code = code
        self.shape = shape
        self.color = color
        self.field_num = field_num
        self.harvested_by = harvested_by


    def is_sellable(self):
        if self.shape > 5 and self.color > 5 and self.field_num != 3:
            return True







def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest
    Melon_1 = Melon("yw", 8, 7, 2, "Sheila")


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest
