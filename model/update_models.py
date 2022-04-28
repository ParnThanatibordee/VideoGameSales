class Update:
    pass


class UpdateVideoGame(Update):
    def __init__(self, Name=None, Platform=None, Year=None, Genre=None, Publisher=None):
        self.Name = Name
        self.Platform = Platform
        self.Year = Year
        self.Genre = Genre
        self.Publisher = Publisher


class UpdateSale(Update):
    def __init__(self, NA_Sales_in_millions=None, EU_Sales_in_millions=None, JP_Sales_in_millions=None,
                 Other_Sales_in_millions=None, Global_Sales_in_millions=None):
        self.NA_Sales_in_millions = NA_Sales_in_millions
        self.EU_Sales_in_millions = EU_Sales_in_millions
        self.JP_Sales_in_millions = JP_Sales_in_millions
        self.Other_Sales_in_millions = Other_Sales_in_millions
        self.Global_Sales_in_millions = Global_Sales_in_millions
