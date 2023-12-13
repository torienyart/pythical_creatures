import pytest
# from ..lib.unicorn import Unicorn
from creatures.unicorn import Unicorn

# Test cases for the Unicorn class
class TestUnicorn:

    def test_unicorn_name(self):
        unicorn = Unicorn("Sparkles")
        assert unicorn.name == "Sparkles"

    def test_unicorn_color(self):
        unicorn = Unicorn("Jangles")
        assert unicorn.color == "silver"

    def test_unicorn_doesnt_have_to_be_silver(self):
        unicorn = Unicorn("Rhonda", "purple")
        assert unicorn.color == "purple"
        assert unicorn.color != "silver"

    def test_unicorn_says_sparkly_stuff(self):
        unicorn = Unicorn("Glimmer")
        assert unicorn.say("Wonderful!") == "**;* Wonderful! *;**"
        assert unicorn.say("I don't like you very much.") == "**;* I don't like you very much. *;**"
# # Run the tests
# if __name__ == "__main__":
#     pytest.main()