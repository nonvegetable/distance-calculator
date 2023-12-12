# Distance Calculator

This simple Python program calculates the distance between two places using the Haversine formula and the OpenCage Geocoding API. (I made this program as to practice implemetation of API's)

## Prerequisites

Before running the program, you need to obtain an API key from the OpenCage Geocoding API. You can sign up and get your API key [here](https://opencagedata.com/).

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/DistanceCalculator.git
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Replace 'YOUR-API-KEY' in `APICall.py` with your actual OpenCage API key.

## Usage

1. Run the program:
   ```bash
   python main.py
   ```

2. Enter the names of two places when prompted.

3. The program will fetch the coordinates using the OpenCage API and calculate the distance between the two places.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [OpenCage Geocoding API](https://opencagedata.com/) for providing geocoding services.
- [Haversine formula](https://en.wikipedia.org/wiki/Haversine_formula)
