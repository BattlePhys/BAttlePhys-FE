import pytest
import os


def run_tests():
    os.environ["ENV"] = "testing"
    os.chdir("tests")
    pytest.main(["-v", "-s"])


if __name__ == "__main__":
    run_tests()