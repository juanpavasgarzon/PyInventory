from core.counter.entities.counter import Counter


async def get_next_sequence_repo(name: str) -> int:
    """
    Retrieves the next sequential value for a given counter. If the counter does not exist, it is created.

    This function fetches the counter by its name from the database. If the counter is not found, a new
    counter is created with an initial value of 1. After retrieving or creating the counter, the value
    is incremented by 1 and returned.

    Args:
        name (str): The name of the counter for which to get the next sequential value.

    Returns:
        int: The next sequential value for the given counter.

    Raises:
        Exception: If there is an issue updating or saving the counter.

    Example:
        next_value = await get_next_sequence_repo("invoice_number")
        print(next_value)  # Output: next sequential value for "invoice_number" counter
    """
    counter = await Counter.objects(name=name).first()
    if not counter:
        counter = Counter(name=name, value=1)
        await counter.save()

    await counter.update(inc__value=1)
    return counter.value
