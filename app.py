from docker.yaml.utils import read_yaml_file

# Read YAML file
yaml_file = read_yaml_file('config.yaml')
print(yaml_file)

# Access the dictionary
build_yaml = yaml_file['build']
predict_yaml = yaml_file['predict']

# Build the image
gpu_status = build_yaml['gpu']
if gpu_status:
    print('Building the image with GPU support')
else:
    print('Building the image without GPU support')
system_packages = build_yaml['system_packages']
python_version = build_yaml['python_version']
python_packages = build_yaml['python_packages']
python_source = build_yaml['python_source']