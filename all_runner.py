import subprocess
from subprocess import TimeoutExpired

import sys

acps = [('Problem_1', 1), ('Problem_2', 2), ('Problem_3', 3)]
algos = [(1, 'breadth_first_search'),
          (2, 'breadth_first_tree_search'),
         (3, 'depth_first_graph_search'),
         (4, 'depth_limited_search'),
         (5, 'uniform_cost_search'),
         (6, 'recursive_best_first_search--h_1'),
         (7, 'greedy_best_first_graph_search--h_1'),
         (8, 'astar_search--h_1'),
         (9, 'astar_search--h_ignore_preconditions'),
         (10, 'astar_search--h_pg_levelsum')]

python_path = "/installs/anaconda3/envs/aind/bin/python"


def persist_output(stdout, output_file):
    file = open(output_file, "w")
    file.write(str(stdout))
    file.close()


def execute_process_with_timeout(sequence, command_array, output_file, timeout=15 * 60):
    try:
        cp = subprocess.run(command_array, timeout=timeout, stdout=subprocess.PIPE, universal_newlines=True)
        print(cp.stdout)
        persist_output(cp.stdout, output_file)
    except TimeoutExpired as to:
        print("Timeout occured for ", sequence)
        persist_output(to.stdout, output_file)
    except:
        print("Unknown error for ", sequence, sys.exc_info()[0])


for acp, algo in [(acp, algo) for acp in acps for algo in algos]:
    acp_name, acp_index = acp
    algo_index, algo_name = algo

    output_file = 'output-' + acp_name + "--" + algo_name + '.txt'
    command = [python_path, "run_search.py", "-p", str(acp_index), "-s", str(algo_index)]

    seq = (acp_name, algo_name)
    print("Executing", seq)

    execute_process_with_timeout(seq, command, output_file)
