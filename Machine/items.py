from dataclasses import dataclass


# hash the class to avoid duplicate
@dataclass(unsafe_hash=True, eq=False)
class Snack:
    id: int
    name: str
    price: float
    currency: str = "JD"

    # Order snacks based on the id
    def __lt__(self, other):
        return self.id < other.id


# As a set to avoid  duplicate entries.
snacks = {
    Snack(1, "Coffee Latte", 0.85),
    Snack(2, "Tuna Sandwich", 1.5),
    Snack(3, "Lays Chips", 0.6),
    Snack(4, "Snicker", 0.5),
    Snack(5, "Turkey Sandwich", 1.3),
    Snack(6, "Peanuts", 0.7)
}
