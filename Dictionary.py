# Simple dictionary example

country_capitals = {
    "Germany": {"capital": "Berlin", "population": 84000000},
    "Canada": {"capital": "Ottawa", "population": 41000000},
    "France": {"capital": "Paris", "population": 68000000}
}

print("Country Capitals:", country_capitals)
print(country_capitals["Canada"]["capital"])

country_capitals["England"] = {"capital": "London", "population": 57000000}
print(country_capitals["England"])

print("Germany" in country_capitals)
print("Spain" not in country_capitals)