# campus_root_project
CampusRoute — Campus Shortest Path Finder
Overview
CampusRoute is a DAA mini project that finds the shortest route between different locations on a college campus using Dijkstra's Shortest Path Algorithm.

The project represents the campus as a weighted graph, where campus locations are represented as vertices and the distances between connected locations are represented as weighted edges.

Note: The campus locations and distances used in this project are hypothetical and created for academic demonstration.

Problem Statement
Finding the shortest route between two locations on a large campus can be difficult when multiple paths are available.

The objective of this project is to design an efficient system that determines the shortest path and minimum travel distance between two selected campus locations.

Objectives
Represent campus locations using a weighted graph.
Find the shortest route between any two campus locations.
Calculate the minimum travel distance.
Demonstrate the practical application of Dijkstra's Algorithm.
Analyze the time and space complexity of the algorithm.
Provide a simple menu-driven interface for users.
Features
Display all campus locations.
Display campus connections and their distances.
Find the shortest route between two locations.
Display the total shortest distance.
Reconstruct and display the complete route.
Display information about the algorithm and its complexity.
Input validation for invalid locations and selecting the same source and destination.
Campus Locations
The project contains the following locations:

Main Gate
First Year Block
Central Ground
IT Department
AI & Data Science Department
Mechanical Department
E&TC Department
Canteen
Library
Admin Block
Algorithm Used
Dijkstra's Shortest Path Algorithm
Dijkstra's Algorithm is used to find the shortest path from a selected source location to all other locations in a weighted graph with non-negative edge weights.

The implementation uses:

Adjacency List — to represent the campus graph.
Priority Queue (Min-Heap) — to efficiently select the next location with the smallest known distance.
Previous Node Tracking — to reconstruct the shortest route from the source to the destination.
Basic Working
Select the source location.
Initialize the distance of the source as 0 and all other distances as infinity.
Insert the source into the priority queue.
Select the location with the smallest current distance.
Check all its connected locations.
Update distances if a shorter route is found.
Continue until the shortest distances are determined.
Reconstruct the route using the previous-node information.
Technologies Used
Programming Language: Python 3
Algorithm: Dijkstra's Shortest Path Algorithm
Data Structures: Graph, Adjacency List, Dictionary, List, Set
Priority Queue: Python heapq
Development Environment: VS Code
Version Control: Git and GitHub
Project Structure
DAA mini project (Campus route)/
│
├── campus_route.py
└── README.md
campus_route.py
Contains the complete implementation of:

Campus graph
Dijkstra's Algorithm
Shortest path reconstruction
Campus location display
Campus connection display
Menu-driven interface
Algorithm information
How to Run
1. Install Pycharm from JetBrains PyCharm
2. Intall it normally
3. Open PyCharm

4. Clone the Repository
git clone <https://github.com/supriyachamat/campus_root_project>
5. Open the Project Folder
cd campus-route-finder
6. Run the Program
python campus_route.py
Sample Execution
Example
Source: Main Gate

Destination: Library

Shortest Route:

Main Gate -> First Year Block -> Admin Block -> Library
Total Distance:

470 meters
The route is calculated automatically using Dijkstra's Algorithm.

Complexity Analysis
For a graph represented using an adjacency list and a priority queue:

Time Complexity
O((V + E) log V)
where:

V = number of vertices (campus locations)
E = number of edges (campus connections)
Space Complexity
O(V + E)
The space is used for the graph, distance information, previous-node information, and priority queue.

Test Cases
Test Case	Source	Destination	Expected Result
1	Main Gate	Library	Shortest route with total distance 470 meters
2	Main Gate	IT Department	Shortest route with total distance 300 meters
3	IT Department	Canteen	Shortest route with total distance 200 meters
4	First Year Block	Admin Block	Shortest route with total distance 150 meters
5	Same Location	Same Location	Invalid input message
Future Scope
The project can be enhanced in the future by adding:

Interactive campus map visualization.
Graphical User Interface (GUI).
Real campus map and location data.
Estimated walking time.
Multiple route suggestions.
Dynamic route updates.
Comparison with other shortest-path algorithms.
Conclusion
CampusRoute demonstrates how Dijkstra's Algorithm can be applied to a practical campus navigation problem.

The project uses a weighted graph and priority queue to efficiently calculate the shortest route between selected campus locations. It provides a simple way to understand the practical application of graph algorithms and their complexity in solving real-world routing problems.

Author
Supriya Chamat

Roll no:123

B.Tech Information Technology Priyadarshini College of Engineering, Nagpur

License
This project was developed for academic and educational purposes.
