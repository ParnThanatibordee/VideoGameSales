from model.models import Sale
from model.update_models import UpdateSale


class SaleDao:
    def __init__(self, session):
        self.session = session

    def get(self, GameID):
        return self.session.query(Sale).filter_by(GameID=GameID).first()

    def get_all(self):
        return self.session.query(Sale).all()

    def update(self, GameID, sale: UpdateSale):
        this_sale = self.get(GameID)

        try:
            if sale.NA_Sales_in_millions:
                this_sale.NA_Sales_in_millions = sale.NA_Sales_in_millions
            if sale.EU_Sales_in_millions:
                this_sale.EU_Sales_in_millions = sale.EU_Sales_in_millions
            if sale.JP_Sales_in_millions:
                this_sale.JP_Sales_in_millions = sale.JP_Sales_in_millions
            if sale.JP_Sales_in_millions:
                this_sale.JP_Sales_in_millions = sale.JP_Sales_in_millions
            if sale.Global_Sales_in_millions:
                this_sale.Global_Sales_in_millions = sale.Global_Sales_in_millions
            self.session.commit()
        except:
            self.session.rollback()
            raise
