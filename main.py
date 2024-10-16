import APICall
from DistanceCalculate import calculate_distance, get_unit_name

def main():
    print("Welcome to the Distance Calculator!")
    
    while True:
        # Get input for the first place
        place1 = input("Enter the first place: ")
        
        # Get input for the second place
        place2 = input("Enter the second place: ")
        
        # Get input for the unit
        unit = input("Enter the unit (km/mi/nm): ").lower()
        
        # Validate unit input
        if unit not in ['km', 'mi', 'nm']:
            print("Invalid unit. Defaulting to kilometers (km).")
            unit = 'km'
        
        try:
            # Make API calls to get coordinates
            print("Fetching coordinates...")
            coord1 = APICall.api_call(place1)
            coord2 = APICall.api_call(place2)
            
            # Calculate the distance
            distance = calculate_distance(coord1, coord2, unit)
            
            # Get the full unit name
            unit_name = get_unit_name(unit)
            
            # Print the result
            print(f"\nThe distance between {place1} and {place2} is {distance:.2f} {unit_name}.")
        
        except Exception as e:
            print(f"An error occurred: {str(e)}")
        
        # Ask if the user wants to calculate another distance
        another = input("\nDo you want to calculate another distance? (yes/no): ").lower()
        if another != 'yes':
            print("Thank you for using the Distance Calculator. Goodbye!")
            break

if __name__ == "__main__":
    main()