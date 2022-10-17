import subprocess
import ast
import json
import sys

query = "{query}" or 2
indent_to = int(query)
raw_input = subprocess.check_output(['pbpaste'])
decoded_input = raw_input.decode('utf-8')
try:
	as_dict = ast.literal_eval(decoded_input)
	json.dump(as_dict, sys.stdout, indent=indent_to)
except ValueError:
    json.dump(json.loads(decoded_input), sys.stdout, indent=indent_to)
except:
	sys.stdout.write(decoded_input)
