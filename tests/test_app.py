from src.app import main, echo


def test_main():
    assert main() == 0
