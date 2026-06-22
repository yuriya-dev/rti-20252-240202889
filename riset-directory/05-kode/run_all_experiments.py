import os
import sys
import json
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

def load_config():
    default_config = {
        "notebook_path": "BBRI_Stock_Prediction.ipynb",
        "start_run": 1,
        "end_run": 10,
        "timeout_seconds": 900,
        "kernel_name": "python3"
    }
    config_path = 'config_run.json'
    if os.path.exists(config_path):
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                user_config = json.load(f)
                default_config.update(user_config)
                print(f"📖 Loaded configuration from {config_path}")
        except Exception as e:
            print(f"⚠️ Error loading {config_path}, using defaults: {e}")
    else:
        print("ℹ️ No config_run.json found, using default configurations.")
    return default_config

def run_notebook(run_id, config):
    notebook_path = config["notebook_path"]
    timeout = config["timeout_seconds"]
    kernel = config["kernel_name"]
    
    print(f"\n==================================================")
    print(f"🚀 STARTING RUN {run_id} / {config['end_run']}...")
    print(f"==================================================")
    
    # Read the notebook
    if not os.path.exists(notebook_path):
        print(f"❌ Error: Notebook file not found at {notebook_path}")
        return False
        
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)
    
    # Modify CONFIG cell
    config_modified = False
    for cell in nb.cells:
        if cell.cell_type == 'code' and 'CONFIG = {' in cell.source:
            # Modify run_id in CONFIG
            lines = cell.source.splitlines()
            for idx, line in enumerate(lines):
                if "'run_id':" in line:
                    # preserve indentation
                    indent = len(line) - len(line.lstrip())
                    lines[idx] = f"{' ' * indent}'run_id':        {run_id},           # default run 1 (dapat diubah 1-10)"
                    config_modified = True
                    break
            cell.source = '\n'.join(lines)
            break
            
    if not config_modified:
        print("⚠️ Warning: Could not find CONFIG cell to modify run_id.")
    
    # Execute the notebook
    ep = ExecutePreprocessor(timeout=timeout, kernel_name=kernel)
    try:
        # Since the notebook is in 05-kode/, its working directory is '.' (which is 05-kode/)
        ep.preprocess(nb, {'metadata': {'path': '.'}})
        print(f"✅ RUN {run_id} completed successfully!")
    except Exception as e:
        print(f"❌ Error executing RUN {run_id}: {e}")
        return False
        
    # Save the executed notebook inside ../06-output/run-{run_id}/
    out_dir = f"../06-output/run-{run_id}"
    os.makedirs(out_dir, exist_ok=True)
    out_nb_path = os.path.join(out_dir, 'BBRI_Stock_Prediction_executed.ipynb')
    with open(out_nb_path, 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)
    print(f"💾 Executed notebook saved to: {out_nb_path}")
    return True

if __name__ == '__main__':
    # Ensure working directory is the script's directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    config = load_config()
    
    start_run = config["start_run"]
    end_run = config["end_run"]
    
    # Command line args can override start/end run
    if len(sys.argv) > 1:
        try:
            start_run = int(sys.argv[1])
            end_run = start_run
            if len(sys.argv) > 2:
                end_run = int(sys.argv[2])
            print(f"🔄 Overriding runs to: {start_run} to {end_run}")
        except ValueError:
            print("Usage: python3 run_all_experiments.py [run_id] or [start_run_id] [end_run_id]")
            sys.exit(1)
            
    success_count = 0
    for r in range(start_run, end_run + 1):
        if run_notebook(r, config):
            success_count += 1
            
    print(f"\nCompleted {success_count} runs successfully out of {end_run - start_run + 1}.")
