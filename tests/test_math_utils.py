from app.utils.math_utils import cosine_similarity


def test_same_vectors():
    result = cosine_similarity(
        [1.0, 2.0, 3.0],
        [1.0, 2.0, 3.0],
    )

    assert round(result, 5) == 1.0


def test_perpendicular_vectors():
    result = cosine_similarity(
        [1.0, 0.0],
        [0.0, 1.0],
    )

    assert round(result, 5) == 0.0