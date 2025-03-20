# Wildlife Monitoring Cycle Detection  

**AUTHOR:** Ryan Trinh  
**LICENSE:** MIT License  
**CONTACT:** rtrinh02@csu.fullerton.edu  

## Algorithm Overview  
This implementation creates a greedy algorithm to determine the preferred starting city for a circular trip. The cities arranged on a circle with known distances between them, and each city has a gas station with a specified amount of fuel. Given the car's MPG, the algorithm finds a unique starting city the car can travel the entire circle and return to the starting point with more than 0 gallons left. 


### Approach:
- Compute the fuel gain at each using: net_gain = (fuel[i] * mpg) - city_distance[i]

---

## Files Included  
- **`main.py`** — Python script containing the algorithm implementation.  
- **`README.md`** — Provides an overview and instructions for the project.  

## Requirements  
- **Python 3.11**  

## How To Run  
1. Ensure Python is installed.  
2. Download or clone the repository:  
   ```bash
   git clone <repository_url>
   cd <repository_name>
