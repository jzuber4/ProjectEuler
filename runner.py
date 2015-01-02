"""
    Script to run the solvers for each problem.
    Contains options for timing, selection of specific problems, and selection
    of implementation language (current options are python and rust)
"""
import inspect
import argparse
import os
import time
from subprocess import Popen, PIPE
from hashlib import sha256

# number of zeroes in filenames (e.g. 2 means Problem9.py is Problem09.py)
r_just_zeroes = 2

def problem_string_to_num(problem_string):
    return int(problem_string[len("Problem") : len("Problem") + r_just_zeroes])


def main():

    # construct argument parser
    parser = argparse.ArgumentParser(description="Script to run the solvers. \
            Contains options for timing, selection of specific problems, and selection \
            of implementation language (current options are python and rust. Timing \
            functionality is not intended as a robust profiling tool, rather just a fun \
            feature.")

    parser.add_argument('--time', action='store_true',
                        help='time the execution of the solutions')
    parser.add_argument('--test', action='store_true',
                        help='test the solutions of each problem')
    parser.add_argument('-l', '--lang', required=False,
                        choices=['python', 'rust'],
                        default='python',
                        help='choose language implementation')
    parser.add_argument('-p', '--problems', type=int, nargs='*',
                        help='the numbers of problems to be run, defaults to all')
    parser.add_argument('-q', '--quiet', action='store_true',
                        help='reduce the output of this script')
    parser.add_argument('--just_answers', action='store_true',
                        help='Only output the answers.')
    args = parser.parse_args();

    # read in answers if checking
    # hashes.txt is a file of sha256 hexdigests
    hashed_answers = []
    if args.test:
        hashed_answers = open("hashed_answers.txt").read().split("\n")
        hashed_answers = hashed_answers[:-1] # split takes one too many


    # select implementation
    directory = ""
    if args.lang == 'python':
        directory = 'PythonImplementations'
    elif args.lang == 'rust':
        directory = 'RustImplementations'

    # change directory to allow naive .txt file paths in solutions
    os.chdir(directory)
    # choose appropriate files
    files = [f for f in os.listdir(".") if "Problem" in f]

    # specify details about languages
    invocation = []
    file_ending = ""
    bad_file_endings = [".txt"]
    if args.lang == 'python':
        invocation = ["python"]
        file_ending = ".py"
    elif args.lang == 'rust':
        invocation = []
        file_ending = ""
        bad_file_endings.append(".rs") # source

    # filter out source and other non-executable files
    # going for clarity of code rather than speed of implementation
    # this is obviously inefficient if taken to the extreme
    for ending in bad_file_endings:
        files = [f for f in files if not ending in f]

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
    # run all selected problems
    correct = 0
    wrong = 0
    errors = 0

    if not args.quiet and not args.just_answers:
        print "Testing {} solutions.".format(args.lang)

    for f in files:
        if not args.quiet and not args.just_answers:
            print "Running {}:".format(f)

        # format invocation - can differ by language
        # i.e. python will have invocation = ["python", "Problem###.py"]
        #    and rust will have invocation = ["./Problem###"]
        call = invocation[:]
        call.append("./" + f)

        # not meant to be robust timing
        if args.time:
            individual_start_time = time.time()

        p = Popen(call, stdin=PIPE, stdout=PIPE, stderr=PIPE)

        output, err = p.communicate()

        if args.time:
            individual_end_time = time.time()

        output = output.strip() # remove extraneous whitespace

        # check if there was an error
        if err or p.returncode:
            print "{} encountered error: {}.".format(f, err)
            print "Return code: {}".format(p.returncode)
            errors += 1
        else:
            # echo solution
            if not args.quiet or args.just_answers:
                print output
            # check correctness
            if args.test and not args.just_answers:
                check, applicable = check_correct(hashed_answers, problem_string_to_num(f), output)
                if not check:
                    if not applicable:
                        print "{} could not be verified, no answer in answer file.".format(f)
                    else:
                        print "{} with output \"{}\" is incorrect.".format(f, output)
                elif not args.quiet:
                    print "Correct!"
                    correct += 1

        if args.time and not args.quiet and not args.just_answers:
            print "Ran in {:.4f} seconds".format(individual_end_time - individual_start_time)

    if args.time and not args.just_answers:
        print "{} solutions ran in a total {:.4f} seconds".format(len(files), time.time() - start_time)
    if args.test and not args.just_answers:
        print "{} out of {} solutions terminated without error".format(len(files)-errors,len(files))
        print "{} wrong answers, {} correct answers".format(wrong, correct)

"""
 Helper to check the solution of a problem given the list
 of solution hashes.
"""
def check_correct(hashed_answers, num, output):
    # not applicable - can't be checked
    if len(hashed_answers[num-1]) == 0:
        return (False, False)

    # calculate hash
    m = sha256()
    m.update(output)

    # check if hashes are the same
    return m.hexdigest() == hashed_answers[num-1], True

main()
