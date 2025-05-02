def calculate_discount(price: float, discount: float) -> float:
    """
    Calculate discounted price with input validation.

    :param price: Original price, must be positive
    :param discount: Discount percentage (0-100)
    :return: Discounted price
    """
    if price < 0:
        raise ValueError("Price must be non-negative.")
    if not 0 <= discount <= 100:
        raise ValueError("Discount must be between 0 and 100.")

    return price * (1 - discount / 100)


# Example usage
if __name__ == "__main__":
    original = 120.0
    final = calculate_discount(original, 15)
    print(f"Final price after 15% discount: €{final:.2f}")
