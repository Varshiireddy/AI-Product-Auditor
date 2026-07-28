import math


def cosine_similarity(
    vector1: list[float],
    vector2: list[float],
) -> float:
    if len(vector1) != len(vector2):
        raise ValueError("Vectors must have the same length.")

    dot_product = sum(
        value1 * value2
        for value1, value2 in zip(vector1, vector2)
    )

    magnitude1 = math.sqrt(
        sum(value * value for value in vector1)
    )

    magnitude2 = math.sqrt(
        sum(value * value for value in vector2)
    )

    if magnitude1 == 0 or magnitude2 == 0:
        raise ValueError(
            "Cosine similarity cannot be calculated for a zero vector."
        )

    return dot_product / (magnitude1 * magnitude2)