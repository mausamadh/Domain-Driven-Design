from randomthings.models import Product
from pydantic import ValidationError, BaseModel
import uuid

data_product = dict(
    id=uuid.uuid4().hex,
    category=uuid.uuid4().hex,
    batch=uuid.uuid4().hex,
    name="Dell inspiron 5000",
    price=85000,
    description="This is i5 10th generation intel core Laptop with 8GB RAM",
    slug="https://guthib.com/",
    brand="Dell",
    status=True,
    manufactured_date="2022-01-01T00:00",
    updated_date="2001-01-01T00:00",
)


try:
    m = Product(**data_product)
    print(m.dict())
except ValidationError as e:
    print(e)


from typing import Dict, Any

abc = {"abcd": "12334"}


class Abc(BaseModel):
    def update(self, mapping: Dict[int, Any]):
        print(mapping)


a = Abc()
a.update(abc)