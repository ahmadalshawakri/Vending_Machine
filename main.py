from typing import Optional

from Machine.items import snacks, Snack
from Machine.units import jod_units

LINE_SIZE = 30


def calculate_dot_number(snack: Snack) -> int:
    dots = LINE_SIZE - len(f"{snack.name} {snack.price} {snack.currency}")
    if dots > 0:
        return dots
    return 0


def get_available_snacks() -> str:

    if not snacks:
        return "No Snacks currently available in the machine."

    items = ""

    for i, snack in enumerate(sorted(snacks)):
        dots = "." * calculate_dot_number(snack)
        displayed_snack = f"{i+1} - {snack.name} {dots} {snack.price} {snack.currency}s"
        if (i+1) % 2:
            items += f"{displayed_snack} \t\t"
        else:
            items += f"{displayed_snack} \n"

    return items


def current_balance(balance: float, currency: str = "JD") -> str:
    return f"Your current balance is: {balance} {currency}"


def insert_money_message() -> str:
    return "Press 'M' to insert Money"


def add_money_to_balance(balance: int) -> int:
    money_inserted = input(f"Insert Money ... {allowed_units()}\n")

    if money_inserted not in jod_units.keys():
        print(f"{money_inserted} is an invalid currency.")
        return 0

    balance += jod_units[money_inserted].value
    print(f"{money_inserted} is inserted ... {current_balance(balance)}")

    return balance


def allowed_units() -> str:
    return f"Allowed units: {', '.join(jod_units.keys())}"


def select_item() -> str:
    return "'I' to select an item"


def get_snack(item: id) -> Optional[Snack]:
    for snack in snacks:
        if item == snack.id:
            return snack
    return None


def run_vending_machine() -> None:
    while True:
        balance = 0
        currency = "JD"

        user_input = input(
                f"{insert_money_message()} ... {current_balance(balance)} \n{get_available_snacks()}\n"
            ).lower()

        if user_input != "m":
            print(f"{user_input} is not valid.")
            continue

        balance = add_money_to_balance(balance)

        if not balance:
            continue

        is_item_dropped = False
        item = None

        while not is_item_dropped:
            is_item_selected = False

            if not (is_item_selected or item):
                insert_money_or_select_item = input(
                    f"{insert_money_message()} / {select_item()} ... {current_balance(balance)}\n"
                ).lower()
            else:
                insert_money_or_select_item = input(
                    f"{insert_money_message()} ... {current_balance(balance)}\n"
                ).lower()

            if insert_money_or_select_item == "i":
                while not is_item_selected:
                    item_id = int(input("Please enter an item id: "))
                    item = get_snack(item_id)

                    if not item:
                        print(f"Inserted snack '{item_id}' doesn't exists.")
                        continue

                    is_item_selected = True
                    print(f"{item.name} has been selected.")
            elif insert_money_or_select_item == "m":
                balance = add_money_to_balance(balance)
                if not balance:
                    continue
            elif insert_money_or_select_item == "c":
                print("Cancelling order...!")
                break
            else:
                print(f"{insert_money_or_select_item} is not a valid option.")
                continue

            if not (is_item_selected or item):
                continue

            remaining = abs(item.price - balance)
            if balance >= item.price:
                print(f"{item.name} is dropped")
                print(f"{remaining} {currency}s returned")
                print(f"{'-'*30} Enjoy your '{item.name}' {'-'*30}")
                is_item_dropped = True
            else:
                print(f"Sorry, not enough credit {remaining} {currency} remaining.")


if __name__ == "__main__":
    run_vending_machine()
