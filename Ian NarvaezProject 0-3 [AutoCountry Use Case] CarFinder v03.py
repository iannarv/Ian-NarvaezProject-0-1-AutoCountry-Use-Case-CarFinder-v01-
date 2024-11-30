AllowedVehiclesList = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan']

def main():
    # Display header
    print('**')
    print('AutoCountry Vehicle Finder v0.3')
    print('**')
    print("\nPlease Enter the following number below from the following menu:\n")
    
    while True:
        # Display Menu
        print("1. PRINT all Authorized Vehicles")
        print("2. SEARCH for a Vehicle")
        print("3. ADD a New Vehicle")
        print("4. Exit")
        
        # Get user choice
        choice = input("\nPlease select an option: ")
        
        # Process user choice
        if choice == '1':
            print_vehicles()
        elif choice == '2':
            search_vehicles()
        elif choice == '3':
            add_vehicle()
        elif choice == '4':
            print("\nThank you for using AutoCountry Vehicle Finder. Goodbye!")
            break
        else:
            print("\nInvalid selection. Please try again.")

def print_vehicles():
    """
    Function to print authorized vehicles in the specified format
    """
    print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
    for vehicle in AllowedVehiclesList:
        print(f"- {vehicle}")

def search_vehicles():
    """
    Function to search for vehicles in the AllowedVehiclesList with exact match
    """
    # Get search query from user
    search_query = input("\nEnter the FULL vehicle name to search: ").strip()
    
    # Search for exact matching vehicle
    if search_query in AllowedVehiclesList:
        print("\nVehicle Found:")
        print(f"- {search_query}")
    else:
        print("\nNo vehicle found. Please enter the FULL vehicle name exactly as listed.")
        print("Authorized vehicles are:")
        for vehicle in AllowedVehiclesList:
            print(f"- {vehicle}")

def add_vehicle():
    """
    Function to add a new vehicle to the AllowedVehiclesList
    """
    # Prompt for Sales Manager password
    password = input("\nEnter Sales Manager Password (psst the password is Sales Manager): ")
    
    # Check password (you might want to replace this with a more secure method)
    if password == "Sales Manager":
        # Prompt for new vehicle name
        new_vehicle = input("\nEnter the FULL name of the new vehicle to add: ").strip()
        
        # Check if vehicle already exists
        if new_vehicle in AllowedVehiclesList:
            print("\nError: This vehicle is already in the authorized list.")
        else:
            # Add the new vehicle to the list
            AllowedVehiclesList.append(new_vehicle)
            print(f"\nVehicle '{new_vehicle}' has been added to the authorized list.")
    else:
        print("\nAccess Denied: Incorrect Sales Manager Password.")

# Run the main program
if __name__ == "__main__":
    main()