def find_unreachable_cities(cities, storages, pipelines):
    """
    Знаходить міста, до яких неможливо доставити газ із кожного газосховища.
    """
    graph = {node: [] for node in (cities + storages)}
    for start, end in pipelines:
        if start in graph:
            graph[start].append(end)

    results = []

    for storage in storages:
        visited = set()
        queue = [storage]
        visited.add(storage)

        while queue:
            current = queue.pop(0)
            for neighbor in graph.get(current, []): 
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        unreachable = [city for city in cities if city not in visited]

        if unreachable:
            results.append([storage, unreachable])

    return results
