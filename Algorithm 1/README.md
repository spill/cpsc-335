# Wildlife Monitoring Cycle Detection  

**AUTHOR:** Ryan Trinh  
**LICENSE:** MIT License  
**CONTACT:** rtrinh02@csu.fullerton.edu  

## Algorithm Overview  
This implementation creates a cycle detection system for a wildlife monitoring system. The objective is to determine whether an animal has returned to a previously visited location by monitoring its movement data, represented as a series of coordinates.  

The algorithm models each coordinate as a node and each movement as an edge, using a **union-find data structure with path compression** to efficiently detect cycles.  

### Approach:
- Each coordinate is treated as a **node**.  
- Movements (edges) connect these nodes.  
- The algorithm uses the **union-find technique**:  
  - Initializes each node to be its own parent.  
  - Iterates over each edge and applies union operations.  
  - Uses **path compression** during the find operation.  
- A cycle is detected when an edge connects two nodes that belong to the same set.  

## Files Included  
- **`main.py`** — Python script containing the algorithm implementation.  
- **`README.md`** — Provides an overview and instructions for the project.  

## Requirements  
- **Python 3.11**  

## How To Run  
1. Download Python 
2. Clone repo  
   ```bash
   git clone <repository_url>
   cd <repository_name>
