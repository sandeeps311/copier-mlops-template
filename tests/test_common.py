import numpy as np
import pandas as pd

try:
    from common_pkg import common
except ImportError:
    from src.common import common


def test_return2():
    assert common.return2() == 2


# numpy and pandas test cases to check version compatibility
def generate_random_numbers():
    return np.random.randint(1, 101, size=5)  # Generate 5 random integers between 1 and 100


def test_mean():
    arr = np.array([1, 2, 3, 4, 5])

    result = np.mean(arr)

    assert result == 3.0


def test_reshape():
    arr = np.arange(12)

    result = arr.reshape(3, 4)

    assert np.array_equal(result, np.array([[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]]))


def test_generate_random_numbers():
    result = generate_random_numbers()

    assert len(result) == 5
    assert all(1 <= x <= 100 for x in result)


def test_addition():
    arr1 = np.array([1, 2, 3, 4, 5])
    arr2 = np.array([10, 20, 30, 40, 50])

    result = arr1 + arr2

    assert np.array_equal(result, np.array([11, 22, 33, 44, 55]))


# Test case for square root function
def test_square_root_function():
    x = np.array([1, 4, 9])

    result = np.sqrt(x)

    expected_result = np.array([1.0, 2.0, 3.0])

    assert np.array_equal(result, expected_result)


# Test case for absolute function
def test_absolute_function():
    x = np.array([-1, -2, -3])

    result = np.abs(x)

    expected_result = np.array([1, 2, 3])

    assert np.array_equal(result, expected_result)


# Convert NumPy array to Pandas DataFrame
def test_numpy_to_dataframe():
    # Create a sample NumPy array
    np_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    # Convert the NumPy array to a Pandas DataFrame
    df = pd.DataFrame(np_array, columns=["A", "B", "C"])

    # Assert that the resulting object is a DataFrame
    assert isinstance(df, pd.DataFrame)

    # Assert the shape of the DataFrame
    assert df.shape == (3, 3)

    # Assert the column names
    assert df.columns.tolist() == ["A", "B", "C"]


# Convert Pandas DataFrame to NumPy array
def test_dataframe_to_numpy():
    # Create a sample Pandas DataFrame
    data = {"A": [1, 2, 3], "B": [4, 5, 6], "C": [7, 8, 9]}
    df = pd.DataFrame(data)

    # Convert the Pandas DataFrame to a NumPy array
    np_array = df.to_numpy()

    # Assert that the resulting object is a NumPy array
    assert isinstance(np_array, np.ndarray)

    # Assert the shape of the NumPy array
    assert np_array.shape == (3, 3)
