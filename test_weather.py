from weather import get_weather

def test_get_weather():
    city = "London"
    temperature = get_weather(city)
    assert isinstance(temperature, float)