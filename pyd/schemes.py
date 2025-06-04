from .base_models import *
from typing import List

class SchemeProduct(BaseProduct):
    category: BaseCategory

class SchemeOrder(BaseOrder):
    user: BaseUser
    status: BaseStatus

class SchemeReview(BaseReview):
    user: BaseUser
    product: SchemeProduct


class SchemeUser(BaseUser):
    role: BaseRole