

import heapq

campus_graph = {
    "Main Gate": {
        "First Year Block": 200,
        "Central Ground": 200
    },

    "First Year Block": {
        "Main Gate": 200,
        "IT Department": 100,
        "Admin Block": 150
    },

    "Central Ground": {
        "Main Gate": 200
    },

    "IT Department": {
        "First Year Block": 100,
        "AI & Data Science Department": 100,
        "Library": 180
    },

    "AI & Data Science Department": {
        "IT Department": 100,
        "Mechanical Department": 60,
        "E&TC Department": 50
    },

    "Mechanical Department": {
        "AI & Data Science Department": 60,
        "Canteen": 70
    },

    "E&TC Department": {
        "AI & Data Science Department": 50,
        "Canteen": 40,
        "Library": 100
    },

    "Canteen": {
        "Mechanical Department": 70,
        "E&TC Department": 40,
        "Library": 80
    },

    "Library": {
        "IT Department": 180,
        "E&TC Department": 100,
        "Canteen": 80,
        "Admin Block": 120
    },

    "Admin Block": {
        "First Year Block": 150,
        "Library": 120
    }
}


def dijkstra(graph, start):
    distances = {location: float('inf') for location in graph}
    previous = {location: None for location in graph}

    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:

        current_distance, current_location = heapq.heappop(priority_queue)

        if current_distance > distances[current_location]:
            continue

        for neighbor, distance in graph[current_location].items():

            new_distance = current_distance + distance

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous[neighbor] = current_location

                heapq.heappush(
                    priority_queue,
                    (new_distance, neighbor)
                )

    return distances, previous


def get_shortest_path(previous, start, destination):
    path = []
    current = destination

    while current is not None:
        path.append(current)
        current = previous[current]

    path.reverse()

    if path[0] != start:
        return []

    return path


source = "Main Gate"
destination = "Library"
distances, previous = dijkstra(campus_graph, source)

path = get_shortest_path(previous, source, destination)


def display_locations(graph):
    print("\n========================================")
    print("        CAMPUS LOCATIONS")
    print("========================================")

    locations = list(graph.keys())

    for i, location in enumerate(locations, start=1):
        print(f"{i}. {location}")


def display_connections(graph):
    print("\n========================================")
    print("        CAMPUS CONNECTIONS")
    print("========================================")

    displayed = set()

    for location in graph:

        for neighbor, distance in graph[location].items():

            connection = tuple(sorted([location, neighbor]))

            if connection not in displayed:
                print(
                    f"{location} <-> {neighbor} : "
                    f"{distance} meters"
                )

                displayed.add(connection)


def find_shortest_route(graph):
    locations = list(graph.keys())

    display_locations(graph)

    try:
        source_choice = int(
            input("\nEnter source location number: ")
        )

        destination_choice = int(
            input("Enter destination location number: ")
        )

        if source_choice < 1 or source_choice > len(locations):
            print("\nInvalid source location.")
            return

        if destination_choice < 1 or destination_choice > len(locations):
            print("\nInvalid destination location.")
            return

        if source_choice == destination_choice:
            print("\nSource and destination cannot be the same.")
            return

        source = locations[source_choice - 1]
        destination = locations[destination_choice - 1]

        distances, previous = dijkstra(
            graph,
            source
        )

        path = get_shortest_path(
            previous,
            source,
            destination
        )

        if path:

            print("\n========================================")
            print("             ROUTE RESULT")
            print("========================================")

            print("\nSource:", source)
            print("Destination:", destination)

            print("\nShortest Route:")
            print(" -> ".join(path))

            print(
                "\nTotal Distance:",
                distances[destination],
                "meters"
            )

        else:
            print("\nNo route found.")

    except ValueError:
        print("\nPlease enter valid numbers.")

    # Main program


while True:

    print("\n\n========================================")
    print("          CAMPUS ROUTE FINDER")
    print("========================================")

    print("\n1. Find Shortest Route")
    print("2. Display Campus Locations")
    print("3. Display Campus Connections")
    print("4. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":

        find_shortest_route(campus_graph)

    elif choice == "2":

        display_locations(campus_graph)

    elif choice == "3":

        display_connections(campus_graph)

    elif choice == "4":

        print("\nThank you for using Campus Route Finder!")
        break

    else:

        print("\nInvalid choice. Please try again.")