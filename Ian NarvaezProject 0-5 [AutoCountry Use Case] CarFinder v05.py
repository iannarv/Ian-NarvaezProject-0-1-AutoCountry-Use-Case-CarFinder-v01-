# Global list of allowed vehicles
AllowedVehiclesList = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Rivian R1T', 'Ram 1500']

def main():
    while True:
        # Display header with formatting
        print('********************************')
        print('AutoCountry Vehicle Finder v0.4')
        print('********************************')
        print('Please Enter the following number below from the following menu:\n')
        
        # Display Menu
        print('1. PRINT all Authorized Vehicles')
        print('2. SEARCH for Authorized Vehicle')
        print('3. ADD Authorized Vehicle')
        print('4. DELETE Authorized Vehicle')
        print('5. Exit')
        print('********************************')
        
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
            remove_vehicle()
        elif choice == '5':
            print("\nThank you for using the AutoCountry Vehicle Finder, good-bye!")
            input("Press Enter to close the program...")
            break
        else:
            print("\nInvalid selection. Please try again.")

def print_vehicles():
    """
    Function to print authorized vehicles in the specified format
    """
    print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
    for vehicle in AllowedVehiclesList:
        print(vehicle)

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

def remove_vehicle():
    """
    Function to remove a vehicle from the AllowedVehiclesList
    """
    # Prompt for Sales Manager password
    password = input("\nEnter Sales Manager Password (psst the password is Sales Manager): ")
    
    # Check password
    if password == "Sales Manager":
        # Print current list of vehicles
        print("\nCurrent Authorized Vehicles:")
        for vehicle in AllowedVehiclesList:
            print(f"- {vehicle}")
        
        # Prompt for vehicle to remove
        remove_vehicle = input("\nEnter the FULL name of the vehicle you want to remove: ").strip()
        
        # Check if vehicle exists in the list
        if remove_vehicle in AllowedVehiclesList:
            # Confirmation prompt
            confirm = input(f"Are you sure you want to remove \"{remove_vehicle}\" from the Authorized Vehicles List? (yes/no): ").strip().lower()
            
            # Remove vehicle if confirmed
            if confirm == 'yes':
                AllowedVehiclesList.remove(remove_vehicle)
                print(f"\nVehicle '{remove_vehicle}' has been removed from the authorized list.")
            else:
                print("\nVehicle removal cancelled.")
        else:
            print("\nError: Vehicle not found in the Authorized Vehicles List.")
    else:
        print("\nAccess Denied: Incorrect Sales Manager Password.")

# Run the main program
if __name__ == "__main__":
    main()