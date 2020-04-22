from copy import copy

#	is_connected-проверяет, связан ли граф в виде словаря или нет, используя алгоритм поиска по ширине (BFS)

def is_connected(G):
	start_node = list(G)[0]
	color = {v: 'белый' for v in G}
	color[start_node] = 'серый'
	S = [start_node]
	while len(S) != 0:
		u = S.pop()
		for v in G[u]:
			if color[v] == 'белый':
				color[v] = 'серый'
				S.append(v)
			color[u] = 'черный'
	return list(color.values()).count('черный') == len(G)

#	odd_degree_nodes-возвращает список всех узлов G нечетных степеней

def odd_degree_nodes(G):
	odd_degree_nodes = []
	for u in G:
		if len(G[u]) % 2 != 0:
			odd_degree_nodes.append(u)
	return odd_degree_nodes

#	from_dict-возвращает список кортежей ссылок из графа G в формате словаря
	
def from_dict(G):
	links = []
	for u in G:
		for v in G[u]:
			links.append((u,v))
	return links

#	fleury(G) - возврат эйлерова следа из графа G или строки "не Эйлеров Граф", если невозможно проследить путь

def fleury(G):
	#	проверяет, имеет ли G Эйлеров цикл или след
	odn = odd_degree_nodes(G)
	if len(odn) > 2 or len(odn) == 1:
		return 'Не Эйлеров Граф'
	else:
		g = copy(G)
		trail = []
		if len(odn) == 2:
			u = odn[0]
		else:
			u = list(g)[0]
		while len(from_dict(g)) > 0:
			current_vertex = u
			for u in g[current_vertex]:
				g[current_vertex].remove(u)
				g[u].remove(current_vertex)
				bridge = not is_connected(g)
				if bridge:
					g[current_vertex].append(u)
					g[u].append(current_vertex)
				else:
					break
			if bridge:
				g[current_vertex].remove(u)
				g[u].remove(current_vertex)
				g.pop(current_vertex)
			trail.append((current_vertex, u))
	return trail

# испытание семи мостов Кенигсберга
print('Кенигсберг')
G = {0: [2, 2, 3], 1: [2, 2, 3], 2: [0, 0, 1, 1, 3], 3: [0, 1, 2]}
print(fleury(G))

# тестирование эйлерова цикла
print('1-й Эйлеров цикл')
G = {0: [1, 4, 6, 8], 1: [0, 2, 3, 8], 2: [1, 3], 3: [1, 2, 4, 5], 4: [0, 3], 5: [3, 6], 6: [0, 5, 7, 8], 7: [6, 8], 8: [0, 1, 6, 7]}
print(fleury(G))

# тестирование еще одного эйлерова цикла
print('2-й Эйлеров цикл')
G = {1: [2, 3, 4, 4], 2: [1, 3, 3, 4], 3: [1, 2, 2, 4], 4: [1, 1, 2, 3]}
print(fleury(G))

# тестирование эйлерова следа
print('Эйлера След')
G = {1: [2, 3], 2: [1, 3, 4], 3: [1, 2, 4], 4: [2, 3]}
print(fleury(G))