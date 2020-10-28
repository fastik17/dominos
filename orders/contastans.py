from dominos.enum import DjangoEnum


class PizzaFlavorChoices(DjangoEnum):
    MARGARITA = "Margarita"
    TEXAS = "Texas"
    MARINARA = "Marinara"
    SALAMI = "Salami"
    PAPPERONI = "Papperoni"


class PizzaSizeChoices(DjangoEnum):
    SMALL = "Small"
    MEDIUM = "Medium"
    LARGE = "Large"


class StatusChoices(DjangoEnum):
    ORDER_PLACED = "Order placed"
    PREPARE = "Prepare"
    BAKE = "Bake"
    BOX = "Box"
    Delivery = "Delivery"
