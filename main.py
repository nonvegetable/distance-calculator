from tkinter import *
import APICall
from DistanceCalculate import calculate_distance

# Make a window
root = Tk()
root.title("Distance Calculator")
root.geometry('500x500')

place1_var = StringVar()
place2_var = StringVar()


# Function to calculate distance and display it
def calculateAndDisplay():
    # Take user inputs
    place1 = place1_var.get()
    place2 = place2_var.get()

    # Make a call to the API to get the coordinates
    coord1 = APICall.api_call(place1)
    coord2 = APICall.api_call(place2)

    # Calculate the distance
    distance = calculate_distance(coord1, coord2)

    # Update the label with the calculated distance
    distance_label.config(text=f"The distance between {place1} and {place2} is {distance:.2f} kilometers.")


place1_entry = Entry(root, textvariable=place1_var)
place1_entry.pack(pady=10)
place2_entry = Entry(root, textvariable=place2_var)
place2_entry.pack(pady=10)

calculate_button = Button(root, text="Calculate Distance", command=calculateAndDisplay)
calculate_button.pack(pady=10)

# Label to display the distance
distance_label = Label(root, text="")
distance_label.pack(pady=10)

# Execute Tkinter
root.mainloop()
