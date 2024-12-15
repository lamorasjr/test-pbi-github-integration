import os
import subprocess
import sys

def check_pbi_datasets(pbi_dataset_dir):
    pbi_datasets = []
    for root, dirs, _ in os.walk(pbi_dataset_dir):
        semantic_model_folders = [d for d in dirs if d.endswith(".SemanticModel")]
        
        for folder in semantic_model_folders:
            tmdl_path = os.path.join(root, folder, "definition", "model.tmdl")
            if os.path.exists(tmdl_path):
                pbi_datasets.append(tmdl_path)

    return pbi_datasets

def exec_tabular_editor_bpa(tabular_editor_path, bpa_rules_path, pbi_dataset):
    prompt_args = [ tabular_editor_path, pbi_dataset, "-A", bpa_rules_path, "-V" ]
    try:
        subprocess.run( prompt_args, check=True, shell=True, )
    except subprocess.CalledProcessError as e:
        # print(f"Error while executing: {e}")
        sys.exit(1)

if __name__ == "__main__":
    path = os.getenv("Build_SourcesDirectory", "")

    tabular_editor_path = os.path.join(path, "pbi_tests\\tabular_editor\\TabularEditor.exe")
    bpa_rules_path = os.path.join(path, "pbi_tests\\bpa_rules\\BPARules.json")
    pbi_dataset_dir = os.path.join(path, "pbi_dm")

    pbi_datasets = check_pbi_datasets(pbi_dataset_dir)

    for pbi_model in pbi_datasets:
        exec_tabular_editor_bpa(tabular_editor_path, bpa_rules_path, pbi_model)
