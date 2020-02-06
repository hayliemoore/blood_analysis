import pytest


def test_HDL_analysis_normal():
    from chol_analysis import HDL_analysis
    answer = HDL_analysis(80)
    expected = "Normal"
    assert answer == expected


def test_HDL_analysis_bl():
    from chol_analysis import HDL_analysis
    answer = HDL_analysis(40)
    expected = "Borderline Low"
    assert answer == expected


def test_LDL_analysis():
    from chol_analysis import LDL_analysis
    answer = LDL_analysis(165)
    expected = "High"
    assert answer == expected


def test_fever_check():
    from chol_analysis import fever_check
    new_data = [96.0, 100.5, 105.1, 97]
    answer = fever_check(new_data)
    expected = True
    assert answer == expected


# learning travis
def test_HDL_analysis():
    """Tests HDL_analysis method
    Args:
        HDL_level
    Returns:
        Passed if answer == expected
    """
    from chol_analysis import HDL_analysis
    input = 100
    answer = HDL_analysis(input)
    expected = 'Normal'
    assert answer == expected


def test_LDL_analysis():
    """Tests LDL_analysis method
    Args:
        LDL_level
    Returns:
        Passed if answer == expected
    """
    from chol_analysis import LDL_analysis
    input = 100
    answer = LDL_analysis(input)
    expected = 'Normal'
    assert answer == expected


@pytest.mark.parametrize("input, output", [
    (100, 'Normal'),
    (50, 'Borderline Low'),
    (20, 'Low'),
    (55.5, 'Borderline Low'),
])
def test_HDL_analysis_parametrize(input, output):
    """Parametrize Tests HDL_analysis method
    Args:
        HDL_level
    Returns:
        Passed if answer == expected
    """
    from chol_analysis import HDL_analysis
    answer = HDL_analysis(input)
    expected = output
    assert answer == expected


@pytest.mark.parametrize("input, output, expected", [
    (100, 'Normal', True),
    (50, 'Borderline Low', True),
    (20, 'Low', True),
    (100, 'Low', False),
    (55.5, 'Borderline Low', True),
])
def test_HDL_analysis_parametrize(input, output, expected):
    """Parametrize Tests HDL_analysis method
    Args:
        HDL_level
    Returns:
        Passed if answer == expected
    """
    from chol_analysis import HDL_analysis
    answer = HDL_analysis(input) == output
    assert answer == expected
