import sys
import os


parent_path = os.path.dirname(sys.argv[0])
print(parent_path)

parent_path = os.path.dirname(parent_path)
print(parent_path)

parent_path = os.path.dirname(parent_path)
print(parent_path)
sys.path.append(parent_path)

