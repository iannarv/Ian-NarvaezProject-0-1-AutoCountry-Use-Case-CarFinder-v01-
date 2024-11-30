AllowedVehiclesList = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan']

def main():
    # Display header
    print('********************************')
    print('AutoCountry Vehicle Finder v0.1')
    print('********************************')
    print("\nPlease Enter the following number below from the following menu:\n")
    
    while True:
        # Display Menu
        print("1. PRINT all Authorized Vehicles")
        print("2. Exit")
        
        # Get user choice
        choice = input("\nPlease select an option: ")
        
        # Process user choice
        if choice == '1':
            print_vehicles()
        elif choice == '2':
            print("\nThank you for using AutoCountry Vehicle Finder. Goodbye!")
            break
        else:
            print("\nInvalid selection. Please try again.")

def print_vehicles():
    """
    Function to print authorized vehicles in the specified format
    """
    print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
    print((AllowedVehiclesList))

# Run the main program
if __name__ == "__main__":
    main()

    