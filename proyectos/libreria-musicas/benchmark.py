import sys

def parse_to_dict(s):
    end = s.find('\n')
    s = s[end+1:]

    d = {}
    while s:
        end = s.find(':')
        key = s[:end]
        s = s[end+1:]

        sep1 = s.find(',')
        sep2 = s.find('\n')
        if sep1 != -1 and sep2 != -1:
            if sep1 < sep2:
                end = sep1
            else: 
                end = sep2
        elif sep1 != -1 and sep2 == -1:
            end = sep1
        elif sep1 == -1 and sep2 != -1:
            end = sep2
        else:
            end = len(s) - 1
        value = s[:end]
        if s:
            s = s[end+1:]
        
        if key not in d:
            d[key] = []
        d[key].append(float(value))
    
    return d

def average_of_list(l: list):
    sum = 0
    for e in l:
        sum += e
    return sum / len(l)

def stat_of_list(l: list):
    return (average_of_list(l), max(l), min(l))

def memory_stat(mem_data):
    s = "Memory Benchmark\n"
    memory_dict = parse_to_dict(mem_data)
    keys = list(memory_dict)
    current_stats = stat_of_list(memory_dict[keys[0]])
    peak_stats = stat_of_list(memory_dict[keys[1]])
    s += (
        f"Prom.: {(
            current_stats[0] / 1024
        ):.3f}kb, Max.: {(
            peak_stats[1] / 1024
        ):.3f}kb, Min.: {(
            current_stats[2] / 1024
        ):.3f}kb.\n"
        )
    return s

def time_stat(time_data):
    s = 'Time Benchmark\n'
    time_dict = parse_to_dict(time_data)
    keys = list(time_dict)

    for k in keys:
        stats = stat_of_list(time_dict[k])
        s += f"{k}:\n"
        s += f"Prom.: {stats[0]:.8f}s, Max.: {stats[1]:.8f}s, Min.: {stats[2]:.8f}s\n"
    return s


if __name__ == '__main__':
    fileroot = sys.path[0] + '/libreria_musicas/benchmark/'

    memory_file = fileroot + 'memory-benchmark.txt'
    with open(memory_file, 'r') as f:
       memory_bench = f.read()
    
    time_file = fileroot + 'time-benchmark.txt'
    with open(time_file, 'r') as f:
       time_bench = f.read()
       
    result_bench = memory_stat(memory_bench) + time_stat(time_bench)
    result_file = fileroot + 'result-benchmark.txt'
    with open(result_file, 'w') as f:
        f.write(result_bench)