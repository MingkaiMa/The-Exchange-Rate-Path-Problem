#
#
# written by Mingkai Ma
#

import sys
import dateutil.parser
from collections import defaultdict


#
# Floyd-Warshall algorithm implementation

def bestRates(rate, next_table, node_nb):

    for k in range(node_nb):
        for i in range(node_nb):
            for j in range(node_nb):
                if rate[i][j] < rate[i][k] * rate[k][j]:
                    rate[i][j] = rate[i][k] * rate[k][j]
                    next_table[i][j] = next_table[i][k]


#
# get path

def getPath(u, v, next_table):
    if next_table[u][v] == None:
        return []

    path = [u]
    while u != v:
        #print(f'u: {u}  v: {v}')
        u = next_table[u][v]
        path.append(u)

    return path


#
# V is vertex list

V = []

#
# adjacent matrix

matrix = defaultdict(dict)



#
# parsing the stdin

for line in sys.stdin:


    inputs = line.split()

    #
    # empty line, do nothing

    if len(inputs) == 0:
        continue
    
    #
    # invalid input, output error and continue

    if not line[0].isdigit() and inputs[0] != 'EXCHANGE_RATE_REQUEST':
        print('Invalid input, continue...')
        continue

    #
    # price updates
    
    if inputs[0] != 'EXCHANGE_RATE_REQUEST':

        time_in_seconds = dateutil.parser.parse(inputs[0]).timestamp()
        exchange = inputs[1]
        source_currency = inputs[2]
        destination_currency = inputs[3]
        forward_factor = inputs[4]
        backward_factor = inputs[5]


        if (exchange, source_currency) in V and (exchange, destination_currency) in V:

            previous = matrix[(exchange, source_currency)][(exchange, destination_currency)]

            prev_time = previous[0]
            prev_factor = previous[1]


            #
            # updates
            if prev_time < time_in_seconds:
                matrix[(exchange, source_currency)][(exchange, destination_currency)] = (time_in_seconds, forward_factor)
                matrix[(exchange, destination_currency)][(exchange, source_currency)] = (time_in_seconds, backward_factor)

            else:
                continue
                

        elif (exchange, source_currency) in V and (exchange, destination_currency) not in V:
            V.append((exchange, destination_currency))
            matrix[(exchange, source_currency)][(exchange, destination_currency)] = (time_in_seconds, forward_factor)
            matrix[(exchange, destination_currency)][(exchange, source_currency)] = (time_in_seconds, backward_factor)


        elif (exchange, source_currency) not in V and (exchange, destination_currency) in V:
            V.append((exchange, source_currency))
            matrix[(exchange, source_currency)][(exchange, destination_currency)] = (time_in_seconds, forward_factor)
            matrix[(exchange, destination_currency)][(exchange, source_currency)] = (time_in_seconds, backward_factor)

        elif (exchange, source_currency) not in V and (exchange, destination_currency) not in V:
            V.append((exchange, source_currency))
            V.append((exchange, destination_currency))
            matrix[(exchange, source_currency)][(exchange, destination_currency)] = (time_in_seconds, forward_factor)
            matrix[(exchange, destination_currency)][(exchange, source_currency)] = (time_in_seconds, backward_factor)
            
            
        
    #
    # exchange rate request
    
    else:

        source_exchange = inputs[1]
        source_currency = inputs[2]
        destination_exchange = inputs[3]
        destination_currency = inputs[4]

        source_node = (source_exchange, source_currency)
        dest_node = (destination_exchange, destination_currency)

        source_node_id = -1
        dest_node_id = -1


        #
        # construct graph and get the result by using provided algorithms

        id_to_node = {}

        node_nb = 0


        for node in V:
            if node == source_node:
                source_node_id = node_nb

            if node == dest_node:
                dest_node_id = node_nb
                
                
            
            id_to_node[node_nb] = node
            node_nb += 1



        if source_node_id == -1 or dest_node_id == -1:
            print('Unknown currency, continue...')
            continue
        


        rate = [[0] * node_nb for _ in range(node_nb)]

        next_table = [[None] * node_nb for _ in range(node_nb)]
                
        for i in range(node_nb):
            for j in range(node_nb):

                next_table[i][j] = j
                
                if i == j:
                    rate[i][j] = 1
                    rate[j][i] = 1
##                    continue

                node_1 = id_to_node[i]
                node_2 = id_to_node[j]

                

                #
                # set factor
            
                if node_2 in matrix[node_1] or node_1 in matrix[node_2]:
                    rate[i][j] = float(matrix[node_1][node_2][1])
                    rate[j][i] = float(matrix[node_2][node_1][1])

                elif node_1[1] == node_2[1]:
                    rate[i][j] = 1
                    rate[j][i] = 1




            

        bestRates(rate, next_table, node_nb)
        



        print(f'BEST_RATES_BEGIN {source_exchange} {source_currency} {destination_exchange} {destination_currency} {rate[source_node_id][dest_node_id]}')

        path = getPath(source_node_id, dest_node_id, next_table)


        for p in path:
            print(id_to_node[p])


        print('BEST_RATES_END')


        
