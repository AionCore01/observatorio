import pytest

from observatory.transformers.kaprekar import UniversalKaprekarTransformer


def test_classic_decimal_transform_matches_expected_values():
    transformer = UniversalKaprekarTransformer(n_digits=4, base=10)

    assert transformer.transform(1234) == (3087, 4321, 1234)


def test_classic_decimal_orbit_converges_to_6174():
    transformer = UniversalKaprekarTransformer(n_digits=4, base=10)

    result = transformer.orbit(6174)

    assert result["converged"] is True
    assert result["fixed_point"] == 6174
    assert result["steps"] == 1


def test_digit_round_trip_preserves_value_across_bases():
    transformer = UniversalKaprekarTransformer(n_digits=4, base=3)

    value = 42
    assert transformer.from_digits(transformer.to_digits(value)) == value
