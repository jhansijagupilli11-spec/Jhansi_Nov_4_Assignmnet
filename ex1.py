# Movie ticket prices
action_movie_price = 200
comedy_movie_price = 150

def book_tickets():
    movie_choice = input("Which movie would you like to watch? (action/comedy): ").lower()
    print(f"You have selected: {movie_choice}")

    movies_available = ["action", "comedy"]

    if movie_choice in movies_available:
        if movie_choice == "action":
            num_tickets = int(input("How many Action movie tickets do you need?: "))
            total_price = num_tickets * action_movie_price
            print(f"The total price for {num_tickets} ticket(s) is: {total_price}")
            
            generate_receipt = input("Would you like to generate a receipt? (yes/no): ")
            if generate_receipt.lower() == "yes":
                print(f"Generating receipt for {num_tickets} {movie_choice} ticket(s) with total price: {total_price}\n")
                with open("receipt.txt", "w") as f:
                    f.write(f"Receipt for {num_tickets} {movie_choice} ticket(s): Total {total_price}\n")
                    
        elif movie_choice == "comedy":
            num_tickets = int(input("How many Comedy movie tickets do you need?: "))
            total_price = num_tickets * comedy_movie_price
            print(f"The total price for {num_tickets} ticket(s) is: {total_price}")
            
            generate_receipt = input("Would you like to generate a receipt? (yes/no): ")
            if generate_receipt.lower() == "yes":
                print(f"Generating receipt for {num_tickets} {movie_choice} ticket(s) with total price: {total_price}\n")
                with open("receipt.txt", "w") as f:
                    f.write(f"Receipt for {num_tickets} {movie_choice} ticket(s): Total {total_price}\n")
    else:
        print("Sorry, that movie is not currently showing.")

book_tickets()