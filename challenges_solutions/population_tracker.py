"""
Requirements:

add_county(population_data, county_info) - tuple is (county_name, population)
    County names should be title case (use .title())
    Example: "nairobi" becomes "Nairobi"
"""
def add_county(population_data, county_info):
    county_name = county_info[0].title()
    population = county_info[1]

    if county_name in population_data:
        return f"{county_name} already exists!"
    else:
        # Storing the value in the dictionary
        population_data[county_name] = population
        return f"{county_name} has been added successfully!" 

"""
update_population(population_data, county_info)
"""
def update_population(population_data, county_info):
    county_name = county_info[0].title()
    population = county_info[1]

    if county_name in population_data:
        # Store key and value
        population_data[county_name] = population
        return f"{county_name} has been updated successfully!"
    else:
        return f"{county_name} does not exist!"

"""
remove_county(population_data, county_name)
"""
def remove_county(population_data, county_name):
    county_name = county_name.title()

    if county_name in population_data:
        del population_data[county_name]
        return f"{county_name} deleted successfully!"
    else:
        return f"{county_name} not found!"

"""
get_largest_county(population_data) - NEW CHALLENGE!
    Return the county with highest population
    Format: "[County Name] has the largest population: [number]"
    If empty: "No data available."
"""
def get_largest_county(population_data):
    # Checks if empty
    if not population_data:
        return "No data available."
    
    # Starts with the first county as the largest
    largest_county = None
    max_population = 0

    # Check each county
    for county_name, population in population_data.items():
        # If population is bigger
        if population > max_population:
            # Update max
            max_population = population
            # Remember this county
            largest_county = county_name
            
    return f"{largest_county} has the largest population: {max_population:,}"


"""
get_total_population(population_data) - NEW FUNCTION!
    Return sum of all populations
"""
def get_total_population(population_data):
    if not population_data:
        return 0
    return sum(population_data.values())  # sum() adds all values!

"""
view_counties(population_data) - display all counties sorted by population (highest first)
"""
def view_counties(population_data):
    if not population_data:
        return "No county names in the population data"
    
    sorted_counties = sorted(
        population_data.items(),
        key = lambda x: x[1],
        reverse = True
    )

    result = "All Counties' Population:\n"

    for county_name, population in sorted_counties:
        # :, adds commas to numbers ie 1000 will be 1,000
        result += f"{county_name.title()}: {population:,}\n"
    return result

counties = {}

print(add_county(counties, ("nairobi", 4397073)))
print(add_county(counties, ("mombasa", 1208333)))
print(add_county(counties, ("kisumu", 4607073)))
print(add_county(counties, ("nyeri", 5397073)))
print(update_population(counties, ("nairobi", 5000000)))
print(view_counties(counties))
print(remove_county(counties, "nairobi"))
print(get_largest_county(counties))
print(get_total_population(counties))

