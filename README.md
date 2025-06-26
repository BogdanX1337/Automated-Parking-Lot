# Automated-Parking-Lot

This is a Parking lot system designed using object oriented principles in Python.
* The parking lot have a capacity of n slots.
* Each slot can only hold a car with a registration number and color.
* Available commands:
  1. Parcare masina
  2. Plecare masina
  3. Status parcare
  4. Iesire
  5. Exportă status parcare în fișier text
 
## Requirements
1. Latest PyCharm

## Installing the application (required before other steps)
Create on desktop a file "parcare_status.txt"

# Setup
1. Clone the repository
2. Locate The "def __init__(self, nr_locuri=X):" in parking_lot.py and change te X with the number of Parking Spaces you want.
3. To run with a file execute "Main.py"
4. You will have 5 options, 1 for Parking a car and 2 for leaving the parking-lot.
5. You can check the parking-lot status and see how much you have to pay by presing 3.
6. You can export the status of the parking-lot with 5.
7. You cand exit the menue with 4.
