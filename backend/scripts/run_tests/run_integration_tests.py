import pytest
import os


def run_integration_tests():
    os.environ["ENV"] = "testing"
    os.chdir("tests/integration_tests")
    pytest.main(["-v", "-s", "test_user_routes.py"])


if __name__ == "__main__":
    run_integration_tests()
