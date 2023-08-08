import os
import stripe

stripe.api_key = os.getenv("API_KEY")


class StripeProduct:
    def __init__(self, name, price, img_url):
        self.name = name
        self.price = int(price * 100)
        self.images = [img_url]

    def register_new_stripe(self):
        product = stripe.Product.create(name=self.name,
                                        default_price_data={
                                            'unit_amount': self.price,
                                            'currency': 'eur'
                                        },
                                        images=self.images
                                        )
        return product.get('id')

    def update_product(self, prod_id):
        new_price_id = stripe.Price.create(product=prod_id,
                                           unit_amount=self.price,
                                           currency="eur"
                                           )
        stripe.Product.modify(prod_id,
                              name=self.name,
                              default_price=new_price_id,
                              images=self.images
                              )

    @staticmethod
    def archive_product(prod_id):
        stripe.Product.modify(prod_id, active=False)
