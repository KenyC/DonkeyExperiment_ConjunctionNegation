import os
import argparse

parser = argparse.ArgumentParser(description="Creates completion code for experiment")
parser.add_argument("--dir", help='Path to the PCIbex directory')
parser.add_argument("--code", help='Prolific completion code', required = True)
parser.add_argument("--link", help='Prolific link to completion code')
args = parser.parse_args()



main_dir = "./"
if args.dir:
	main_dir = args.dir
completion_code = args.code
completion_code_link = f"https://app.prolific.com/submissions/complete?cc={completion_code}"
if args.link:
	completion_code_link = args.link
data_includes_dir = os.path.join(main_dir, "data_includes")


with open(os.path.join(data_includes_dir, "_codes.js"), "w") as f:
	js_file = f"""
	const completion_code      = "{completion_code}";
	const completion_code_link = "{completion_code_link}";
	"""
	f.write(js_file)
