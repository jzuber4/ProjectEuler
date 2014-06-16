"""
    Script to run the solvers for each problem.
    Contains options for timing, selection of specific problems, and selection
    of implementation language (current options are python and rust)
"""
import inspect
import argparse
import subprocess
import os
import time

def main():
    # number of zeroes in filenames (e.g. 2 means Problem9.py is Problem09.py)
    r_just_zeroes = 2

    # construct argument parser
    parser = argparse.ArgumentParser(description="Script to run the solvers. \
            Contains options for timing, selection of specific problems, and selection \
            of implementation language (current options are python and rust. Timing \
            functionality is not intended as a robust profiling tool, rather just a fun \
            feature.")

    parser.add_argument('-t', '--time', action='store_true',
                        help='time the execution of the solutions')
    parser.add_argument('-l', '--lang', required=False,
                        choices=['python', 'rust'],
                        default='python',
                        help='choose language implementation')
    parser.add_argument('-p', '--problems', type=int, nargs='*',
                        help='the numbers of problems to be run, defaults to all')
    args = parser.parse_args();

    # select implementation
    # https://stackoverflow.com/questions/50499/in-python-how-do-i-get-the-path-and-name-of-the-file-that-is-currently-executin
    directory_string = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) + os.sep
    if args.lang == 'python':
        directory_string += 'PythonImplementations' + os.sep
    elif args.lang == 'rust':
        directory_string += 'RustImplementations' + os.sep

    # choose appropriate files
    files = [f for f in os.listdir(directory_string) if "Problem" in f and not ".txt" in f]
    # python dir already done
    invocation =  ""
    file_ending = ""
    if args.lang == 'python':
        invocation = "python "
        file_ending = ".py"
    elif args.lang == 'rust':
        invocation = ""
        file_ending = ""
        # filter out source
        files = [f for f in files if not ".rs" in f]

    # choose selected problems
    if not args.problems is None:
        # match input to correct rjust format
        selected = [str(number).rjust(r_just_zeroes, '0') for number in args.problems]
        # only select files that match
        files = [f for f in files if f[len("Problem"):len("Problem")+r_just_zeroes] in selected]

        # warn for all files that don't exist
        for selection in selected:
            filename = "Problem" + selection + file_ending
            if not filename  in files:
                print "Warning: " + filename + " does not exist."

        # if no files selected
        if len(files) == 0:
            print "No files match!"
            return

    files = sorted(files)

    start_time = time.time()
    # run all scripts
    for f in files:
        individual_start_time = time.time()
        print "Running {}:".format(f)
        # chdir to run scripts in current directory, some solutions assume a text file
        # in the same directory
        subprocess.call("cd " + directory_string + " && "
                + invocation + directory_string + f, shell=True)
        if args.time:
            print "Ran in {:.4f} seconds".format(time.time() - individual_start_time)
        print

    if args.time:
        print "All {} solutions ran in a total {:.4f} seconds".format(len(files), time.time() - start_time)

main()
