"""Classes for melon orders."""


class AbstractMelonOrder:
    
    order_type = None
    tax = 0
    shipped = False
    flat_fee = 0
    

    def __init__(self, species, qty):
        self.species = species
        self.qty = qty
        self.base_price = 5
        if species == 'Christmas melon':
            self.base_price = 1.5 * self.base_price

    def get_total(self):
        """Calculate price, including tax."""
        
        total = (1 + self.tax) * self.qty * self.base_price + self.flat_fee
        return round(total, 4)

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True



class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    
    order_type = "domestic"
    tax = 0.08
    country_code = 'US'


    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        super().__init__(species, qty)
        
   

 
class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    
    order_type = "international"
    tax = 0.17
    

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super().__init__(species, qty)        
        self.country_code = country_code
        if qty < 10:
            self.flat_fee = 3
          
    def get_country_code(self):
        """Return the country code."""

        return self.country_code
