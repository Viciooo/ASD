def dont_disconnect_the_graph_pls(G):
    n = len(G)
    row_sums = [0 for _ in range(n)]
    whole_sum = 0
    for i in range(n):
        for j in range(n):
            row_sums[i] += G[i][j]
            whole_sum += G[i][j]

    sprytnie = sum(range(n))
    while whole_sum != 0:
        min_index = 0
        min_value = float("inf")
        for i in range(n):
            if 0 < row_sums[i] < min_value:
                min_value = row_sums[i]
                min_index = i

        for i in range(n):
            if G[i][min_index] == 1:
                G[i][min_index], G[min_index][i] = 0, 0
                row_sums[min_index] -= 1
                row_sums[i] -= 1
                whole_sum -= 2

        sprytnie -= min_index
        print(min_index, end=" ")

    print(sprytnie)


G = [[0, 1, 1, 0, 0, 0],
     [1, 0, 1, 1, 0, 1],
     [1, 1, 0, 0, 1, 1],
     [0, 1, 0, 0, 0, 1],
     [0, 0, 1, 0, 0, 1],
     [0, 1, 1, 1, 1, 0]]

dont_disconnect_the_graph_pls(G)

#czasy przetworzenia a nie jakieś bzdury bo wtedy mamy O(V+E)