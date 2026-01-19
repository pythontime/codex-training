# Legacy Data Processor - Needs Refactoring!
# This code works but has many issues. Use Codex to improve it.

import json
import os

def process(d, t):
    # process data
    r = []
    for i in d:
        if t == 'filter':
            if i['status'] == 'active':
                r.append(i)
        elif t == 'transform':
            i['processed'] = True
            i['timestamp'] = '2024-01-01'
            r.append(i)
        elif t == 'validate':
            if 'id' in i and 'name' in i:
                if len(i['name']) > 0:
                    if i['id'] > 0:
                        r.append(i)
    return r

def load_and_process(f, t):
    try:
        file = open(f, 'r')
        data = json.load(file)
        file.close()
        result = process(data, t)
        return result
    except:
        return []

def save_results(data, filename):
    f = open(filename, 'w')
    f.write(json.dumps(data))
    f.close()

def main():
    # hardcoded paths
    input_file = '/tmp/input.json'
    output_file = '/tmp/output.json'
    
    if os.path.exists(input_file):
        data = load_and_process(input_file, 'filter')
        data = process(data, 'transform')
        data = process(data, 'validate')
        save_results(data, output_file)
        print('Done! Processed ' + str(len(data)) + ' items')
    else:
        print('File not found')

if __name__ == '__main__':
    main()
