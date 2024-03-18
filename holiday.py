def hotel_cost(num_nights, destination):
    return num_nights * hotel[destination]

def plane_cost(destination):
    return city_flight[destination]

def car_rental_cost(rental_days, destination):
    return rental_days * car[destination]

def total_cost(hotel_cost, plane_cost, car_rental):
    return hotel_cost + plane_cost + car_rental

city = ["LA", "London", "Tokyo", "Hong Kong"]

city_flight = {"LA": 400, "London": 100, "Tokyo": 700, "Hong Kong": 600}
hotel = {"LA": 300, "London": 200, "Tokyo": 150, "Hong Kong": 100}
car = {"LA": 100, "London": 100, "Tokyo": 80, "Hong Kong": 60}

while True:
    destination = input("Please select your destination: (LA, London, Tokyo, Hong Kong) or 'q' to quit: ").capitalize()

    if destination == 'Q':
        break

    if destination in city_flight:
        try:
            nights = int(input("How many nights would you like to stay? "))
            days = int(input("How many days would you like to rent a car? "))

            if nights <= 0 or days <= 0:
                print("Please enter a positive number of nights and days.")
                continue

            flight_cost = city_flight[destination.lower()]  # Adjusting for the input case
            hotel_cost = hotel_cost(nights, destination)
            rental_cost = car_rental_cost(days, destination)
           
            total = total_cost(hotel_cost, flight_cost, rental_cost)

            print(f"Destination: {destination}")
            print(f"Flight Cost: {flight_cost}")
            print(f"Hotel Cost: {hotel_cost}")
            print(f"Rental Car Cost: {rental_cost}")
            print(f"Total Cost: {total}")

        except ValueError:
            print("Please enter a valid number of nights and days.")
    else:
        print("Invalid destination. Please choose from the provided list.")
