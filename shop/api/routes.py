import base64
from shop import app
from shop.products.models import Addproduct
import json


class MethodDict(dict):
    def __getitem__(self, item):
        if item in list(self.keys()):
            return super().__getitem__(item)
        else:
            return lambda: ('{"response": "method not allowed"}', 405)


def get_image(name):
    path = 'static/images/' + name
    with app.open_resource(path, "rb") as file:
        return base64.b64encode(file.read()).decode('utf-8')


def get():
    products = Addproduct.query.filter(Addproduct.stock > 0).order_by(Addproduct.id)
    response = {}
    for product in products:
        response[int(product.id)] = {"name": str(product.name),
                                     "stock": int(product.stock),
                                     "desc": str(product.desc),
                                     "image_1": get_image(str(product.image_1)),
                                     "brand": str(product.brand.name),
                                     "brand_id": int(product.brand_id),
                                     "category": str(product.category.name),
                                     "category_id": int(product.category_id),
                                     "colors": str(product.colors),
                                     "discount": int(product.discount),
                                     "price": float(product.price),
                                     "gender": str(product.gender),
                                     "size": int(product.size),
                                     "stock": int(product.stock)
                                     }
    return json.dumps({"response": response}), 200


@app.route("/api/<string:method>")
def api(method):
    allowed_methods = MethodDict({"get": get})
    return allowed_methods[method]()
