from . import (
    user,
    promotion,
    order,
    payment,
    review,
    menu,
    menu_category,
    menu_item,
    order_item
)

from dependencies.database import engine


def index():
    user.Base.metadata.create_all(engine)
    promotion.Base.metadata.create_all(engine)
    order.Base.metadata.create_all(engine)
    payment.Base.metadata.create_all(engine)
    review.Base.metadata.create_all(engine)
    menu.Base.metadata.create_all(engine)
    menu_category.Base.metadata.create_all(engine)
    menu_item.Base.metadata.create_all(engine)
    order_item.Base.metadata.create_all(engine)