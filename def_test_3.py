def format_address(street, city, province, postal_code):
    return  f"street: {street}, city: {city}, province: {province}, postal_code: {postal_code}"
address = format_address(
    "Gg. Nangka.2",
    "Sukabumi",
    "Jawa barat",
    "43194"
)
print(address)