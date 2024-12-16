import yaml


def write_prompt_to_yaml(file_path, prompt_content):
    with open(file_path, "w") as yaml_file:
        yaml.dump({"prompt": prompt_content}, yaml_file)

def read_prompt_from_yaml(file_path):
    with open(file_path, "r") as yaml_file:
        content = yaml.safe_load(yaml_file)
    return content.get("prompt", "")