# Python program to find
# maximal Bipartite matching.
# Found from https://www.geeksforgeeks.org/maximum-bipartite-matching/

from itertools import permutations


class GFG:
    def __init__(self, graph):

        # residual graph
        self.graph = graph
        self.ppl = len(graph)
        self.jobs = len(graph[0])

    # A DFS based recursive function
    # that returns true if a matching
    # for vertex u is possible
    def bpm(self, u, matchR, seen):

        # Try every job one by one
        for v in range(self.jobs):

            # If applicant u is interested
            # in job v and v is not seen
            if self.graph[u][v] and seen[v] == False:

                # Mark v as visited
                seen[v] = True

                '''If job 'v' is not assigned to
                   an applicant OR previously assigned
                   applicant for job v (which is matchR[v])
                   has an alternate job available.
                   Since v is marked as visited in the
                   above line, matchR[v]  in the following
                   recursive call will not get job 'v' again'''
                if matchR[v] == -1 or self.bpm(matchR[v],
                                               matchR, seen):
                    matchR[v] = u
                    return True
        return False

    # Returns maximum number of matching
    def maxBPM(self):
        '''An array to keep track of the
           applicants assigned to jobs.
           The value of matchR[i] is the
           applicant number assigned to job i,
           the value -1 indicates nobody is assigned.'''
        matchR = [-1] * self.jobs

        # Count of jobs assigned to applicants
        result = 0
        for i in range(self.ppl):

            # Mark all jobs as not seen for next applicant.
            seen = [False] * self.jobs

            # Find if the applicant 'u' can get a job
            if self.bpm(i, matchR, seen):
                result += 1
        return result


def main():
    params = input().strip().split(" ")
    num_states = int(params[0])
    num_raw_material_sites = int(params[1])
    num_factories = int(params[2])
    num_transportation_companies = int(params[3])

    raw_material_sites = input().strip().split(" ")
    factories = input().strip().split(" ")

    transportation_companies = []

    for i in range(num_transportation_companies):
        transportation_companies.append(input().strip().split(" "))

    graph = {}
    all_others = set([])

    for site in raw_material_sites:
        graph[site] = set([])

    for transportation_company in transportation_companies:
        current_raw_material_sites = []
        current_factories = []
        current_other = []

        for i in range(int(transportation_company[0])):
            current_state = transportation_company[i + 1]

            if current_state in raw_material_sites:
                current_raw_material_sites.append(current_state)
            elif current_state in factories:
                current_factories.append(current_state)
            else:
                graph[current_state] = set([])

                current_other.append(current_state)
                all_others.add(current_state)

        for raw_material_site in current_raw_material_sites:
            for factory in current_factories:
                graph[raw_material_site].add(factory)

            for other in current_other:
                graph[raw_material_site].add(other)

        for factory in current_factories:
            for other in current_other:
                graph[other].add(factory)

        # TODO: Figure out how to connect others, since this isn't working
        # for pair in permutations(current_other, r=2):
        #     graph[pair[0]].add(pair[1])

    for other in all_others:
        for value in graph.values():
            if other in value and graph[other] is not None:
                value.update(graph[other])
                value.remove(other)
            elif other in value:
                value.remove(other)
        graph.pop(other)

    for key, value in graph.items():
        if key in value:
            value.remove(key)

    adjacency_matrix = [[0] * num_raw_material_sites for _ in range(num_factories)]

    for key, value in graph.items():
        for vertex in value:
            try:
                adjacency_matrix[raw_material_sites.index(key)][factories.index(vertex)] = 1
            except:
                pass

    print(GFG(adjacency_matrix).maxBPM())


main()
