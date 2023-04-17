https://tutorcs.com
WeChat: cstutorcs
QQ: 749389476
Email: tutorcs@163.com
https://tutorcs.com
WeChat: cstutorcs
QQ: 749389476
Email: tutorcs@163.com
https://tutorcs.com
WeChat: cstutorcs
QQ: 749389476
Email: tutorcs@163.com
https://tutorcs.com
WeChat: cstutorcs
QQ: 749389476
Email: tutorcs@163.com
https://tutorcs.com
WeChat: cstutorcs
QQ: 749389476
Email: tutorcs@163.com
import sys, os, re, json, shutil, traceback
import notebook_convert as nbconv


ws_path = '/home/codio/workspace'
ts_path = '{}/.guides/test'.format(ws_path)
sub_path = '{}'.format(ws_path)
log_path = '{}/log'.format(ts_path)


def get_dir_contents(path_to_dir):
    ''' This method will return all files and directories in a path as a tuple of lists
    '''
    current_files, current_dirs = [], []
    for (_, dirnames, filenames) in os.walk('{}'.format(path_to_dir)):
        current_files.extend(filenames)
        current_dirs.extend(dirnames)
        break
    return current_files, current_dirs


def clear_out_dir(path_to_dir, exclude=[]):
    ''' This method will remove all files and folders in a path
    '''
    current_files, current_dirs = get_dir_contents(path_to_dir)
    
    # File removal
    for direc in current_dirs:
        if direc not in exclude:
            shutil.rmtree('{}/{}'.format(path_to_dir, direc), ignore_errors=True)
    for file in current_files:
        if file not in exclude:
            os.remove('{}/{}'.format(path_to_dir, file))


def copy_files_from_dir(source_dir, dest_dir, include_types=[], exclude_types=[]):
    ''' This method will copy all files in a source folder to a destination folder.
    Anything specified in include types (file extensions) will be copied. If blank,
    all will be copied, less any exclude types
    '''
    current_files, current_dirs = get_dir_contents(source_dir)
    to_copy = []
    
    for file in current_files:
        if len(include_types) == 0 and len(exclude_types) == 0:
            to_copy = current_files + current_dirs
            break
        elif len(include_types) > 0:    
            if get_file_ext(file) in include_types:
                to_copy.append(file)
        else:
            if get_file_ext(file) not in exclude_types and file not in exclude_types:
                to_copy.append(file)
    for elt in to_copy:
        os.system('cp {}/{} {}'.format(source_dir, elt, dest_dir))


def get_file_ext(filename):
    ''' Return the file extension of a filename passed in
    '''
    f = filename.split('.')
    return f[len(f) - 1]
        

def test_java(cfg_settings):
    ''' This method will perform actions needed to clear the testing library (test location),
    copy in all test cases, copy in the submission, then execute the test cases for java
    submissions
    '''
    test_lib_path = '{}/execution-environment/java'.format(ts_path)
    
    # Clear test location
    clear_out_dir(test_lib_path)

    # Copy in the appropriate files (submissions, tests, libraries)
    dont_copy = []
    dont_copy += cfg_settings['assignment_overview']['ignore_files']
    dont_copy += ['py', 'class', 'ipynb']
    copy_files_from_dir(sub_path, test_lib_path, exclude_types=dont_copy)
    copy_files_from_dir('{}/test-cases/java'.format(ts_path), test_lib_path)
    copy_files_from_dir('{}/libs'.format(ws_path), test_lib_path)
    
    # Compile the submission
    print(' > Attempting to compile submission')
    os.chdir(test_lib_path)
    files_present, _ = get_dir_contents(test_lib_path)
    jar_files = ''
    for file in files_present:
        if get_file_ext(file) == 'jar':
            jar_files += file        
    res = os.system('javac -cp {}:{} {}/*.java'.format(test_lib_path, jar_files, test_lib_path))
    if res != 0:
        print(" > ERROR: Could not compile submission")
        exit(res)
    else:
        print(" > Successfully compiled")
        
    print("\n > Running test cases")
    res = os.system("""java -jar junit-platform-console-standalone-1.3.2.jar \
        --disable-ansi-colors \
        --classpath="{}:{}" \
        --reports-dir="{}" \
        --scan-class-path 2>&1 | tee -a {}/results_java.txt""".format(test_lib_path, jar_files, log_path, log_path))
    


def test_python(cfg_settings):
    ''' This method will perform actions needed to clear the testing library (test location),
    copy in all test cases, copy in the submission, then execute the test cases for python
    submissions
    '''
    test_lib_path = '{}/execution-environment/python'.format(ts_path)
    
    # Clear test location
    clear_out_dir(test_lib_path)
    
    # Copy in the appropriate files
    dont_copy = []
    dont_copy += cfg_settings['assignment_overview']['ignore_files']
    dont_copy += ['java', 'class', 'ipynb']
    copy_files_from_dir(sub_path, test_lib_path, exclude_types=dont_copy)
    copy_files_from_dir('{}/test-cases/python'.format(ts_path), test_lib_path)
    
    # Execute test cases
    os.chdir(test_lib_path)
    os.system('python3 {}/runner.py 2>&1 | tee -a {}/results_python.txt'.format(test_lib_path, log_path))


def test_jupyter(cfg_settings):
    ''' This method will perform actions needed to clear the testing library (test location),
    copy in all test cases, copy in the submission, then execute the test cases for Jupyter NB
    submissions
    '''
    test_lib_path = '{}/execution-environment/jupyter'.format(ts_path)
    
    # Clear test location, get submission files to see which need to be converted
    # using runipy
    clear_out_dir(test_lib_path)
    
    # Copy in the appropriate files
    dont_copy = []
    dont_copy += cfg_settings['assignment_overview']['ignore_files']
    dont_copy += ['java', 'class', 'py']
    copy_files_from_dir(sub_path, test_lib_path, exclude_types=dont_copy)
    copy_files_from_dir('{}/test-cases/jupyter'.format(ts_path), test_lib_path)
    
    files_present, _ = get_dir_contents(test_lib_path)
    
    # Execute each file using runipy, then parse to a .py file for actual testing
    # also copy in all additional files
    for file in files_present:
        infile = '{}/{}'.format(test_lib_path, file)

        if file[-6:] == '.ipynb':
            outfile = '{}/{}.py'.format(test_lib_path, file.split('.')[0])
            os.system('/home/codio/.local/bin/runipy -o -q {}'.format(infile))
            nbconv.convert_notebook(infile, outfile)
    
    # Execute test cases
    os.chdir(test_lib_path)
    os.system('python3 {}/runner.py 2>&1 | tee -a {}/results_jupyter.txt'.format(test_lib_path, log_path))
    
    
def test_c(cfg_settings):
    ''' This method will clear out the testing environment, copy in the test cases along with the submission,
    then execute the tests using the Aceunit framework
    '''
    test_lib_path = '{}/execution-environment/c'.format(ts_path)
    
    # Clear test location for compilation
    clear_out_dir(test_lib_path, exclude=['src', 'tests', 'Makefile'])
    clear_out_dir('{}/src'.format(test_lib_path))
    clear_out_dir('{}/tests'.format(test_lib_path))
    
    # Copy in the appropriate files (extra credit agnostic)
    dont_copy = []
    dont_copy += cfg_settings['assignment_overview']['ignore_files']
    dont_copy += ['java', 'class', 'py', 'ipynb', 'Makefile']
    copy_files_from_dir(sub_path, '{}/src'.format(test_lib_path), exclude_types=dont_copy)
    copy_files_from_dir('{}/test-cases/c'.format(ts_path), '{}/tests'.format(test_lib_path), exclude_types=['Makefile'])
    copy_files_from_dir('{}/test-cases/c'.format(ts_path), test_lib_path, include_types=['Makefile'])
    
    # If there are extra credit implementations, parse through the test cases
    ec_implementations = check_files_for_ec_funcs(cfg_settings['assignment_overview'])
    
    files_present, _ = get_dir_contents(test_lib_path)
    os.chdir(test_lib_path)
    os.system('make compile 2>&1 | tee -a {}/log_c.txt'.format(log_path))
    os.system('make program3_test 2>&1 | tee -a {}/log_c.txt'.format(log_path))
    
    """ NEED TO SWITCH THIS COMPILE COMMAND TO FIT:
    os.chdir(test_lib_path)
    os.system('make compile 2>&1 | tee -a {}/log_c.txt'.format(log_path))
    os.system('make program3_test 2>&1 | tee -a {}/log_c.txt'.format(log_path))
    os.system('python3 /home/codio/workspace/.guides/secure/control/clean_program_3.py /home/codio/workspace/.guides/secure/execution-environment/c/src/program3_output.txt')
    os.system('make test 2>&1 | tee -a {}/log_c.txt'.format(log_path))
    os.system('mv results_c.xml {}/test_results_c.xml'.format(log_path))
    """

# https://codereview.stackexchange.com/questions/148305/remove-comments-from-c-like-source-code
# revisit next semester with other variants
COMMENTS = re.compile(r'''
    (//[^\n]*(?:\n|$))    # Everything between // and the end of the line/file
    |                     # or
    (/\*.*?\*/)           # Everything between /* and */
''', re.VERBOSE)


def remove_comments_re(content):
    return COMMENTS.sub('\n', content)

def remove_comments(content):
    index = 0
    comment_line_inside = False
    comment_block_level = 0
    result = []
    while index < len(content):
        if content[index] == '/' and index + 1 < len(content) and content[index+1] == '*':
            comment_block_level += 1
        elif content[index] == '/' and content[index-1] == '*':
            comment_block_level -= 1
        elif content[index] == '/' and index + 1 < len(content) and content[index + 1] == '/':
            comment_line_inside = True
        elif content[index] == '\n' and comment_line_inside == True:
            comment_line_inside = False
        elif not comment_line_inside and comment_block_level == 0:
            result.append(content[index])
        index += 1

    return ''.join(result)


def check_files_for_required_funcs(asg_overview):
    ''' This function will confirm that all required functions are present
    for student submission, then return the number of missing (if any)
    '''
    missing = 0
    required_funcs_files = asg_overview['required_functions']
    for file in required_funcs_files:
        print("\n\n >\tLooking for required functions in {}".format(file))
        try:
            fd = open('{}/{}'.format(sub_path, file), 'r')
            contents = fd.read()
            contents = remove_comments_re(contents)
            req_funcs = required_funcs_files[file]
            for req_func in req_funcs:
                print(" >\t\t - Searching for function {} ".format(req_func), end='')
                if req_func not in contents:
                    print("\033[91m☒\033[0m")
                    missing += 1
                else:
                    print("☑")  
            fd.close()
        except IOError as e:
            print("Unable to open file: {}".format(file))
            return -1
    return missing


def check_for_required_files(asg_overview):
    ''' This function will confirm that all required files are present
    for student submission, then return the number of missing (if any)
    '''
    required_files = asg_overview['required_files']
    files_present = []
    for (_, _, filenames) in os.walk('{}'.format(sub_path)):
        files_present.extend(filenames)
        break
    print("\n >\tVerifying presence of required submission files in {}".format(sub_path))
    missing = 0
    for req_file in required_files:
        print(" >\t\t - Searching for {} ".format(req_file), end='')
        if req_file not in files_present:
            print("\033[91m☒\033[0m")
            missing += 1
        else:
            print("☑")
    return missing


def execute_language_specific_tests(cfg_settings):
    ''' This function will scan for the included languages in the assignment, then execute 
    the relevant process for autograding
    '''
    assignment_types = cfg_settings['assignment_overview']['assignment_types']
    if 'jupyter' in assignment_types:
        print("\n======================================================================")    
        print(" > Running jupyter notebook tests")
        test_jupyter(cfg_settings)
    if 'java' in assignment_types:
        print("\n======================================================================")    
        print(" > Running java tests")
        print("======================================================================")    
        test_java(cfg_settings)
    if 'python' in assignment_types:
        print("\n======================================================================")    
        print(" > Running python tests")
        print("======================================================================")    
        test_python(cfg_settings)
    if 'c' in assignment_types:
        print("\n======================================================================")    
        print(" > Running C tests")
        print("======================================================================")    
        test_c(cfg_settings)
    print("\n======================================================================")

    
def check_files_for_ec_funcs(asg_overview):
    ''' This function will check whether the student attempted any of the extra credit
    implementations. It will then return a dictionary with those that were attempted
    '''
    ec_func_files = asg_overview['extra_credit_functions']
    implementations = {}
    for file in ec_func_files:
        print("\n\n >\tLooking for extra credit functions in {}".format(file))
        try:
            submission_file = open('{}/{}'.format(sub_path, file), 'r')
            contents = submission_file.read()
            contents = remove_comments_re(contents)
            submission_file.close()
            ec_funcs = ec_func_files[file] # Student function names in student submission file

            for ec_func in ec_funcs:
                print(" >\t\t - Searching for function {} ".format(ec_func), end='')
                if ec_func not in contents:
                    print("\033[91m☒\033[0m")
                else:
                    print("☑")
                    if file not in implementations:
                        implementations[file] = ec_func_files[file]
        except IOError as e:
            print("Unable to open file: {}".format(file))
            return []
    return implementations

    
def parse_ec_tests(cfg_settings, path_to_excec_env, ec_funcs_included):
    ''' This function will go through the extra credit tests and uncomment them
    based on specified regular expression below. It currently is only implemented
    for C language.
    '''    
    regex = ['BEGIN_EC_TEST_', 'END_EC_TEST_']
    
    ec_files_and_funcs = {}
    for student_file in ec_funcs_included:
        for student_func in ec_funcs_included[student_file]:
            ec_file = ec_funcs_included[student_file][student_func]
            for key in ec_file:
                if key not in ec_files_and_funcs:
                    ec_files_and_funcs[key] = [ec_file[key]]
                else:
                    ec_files_and_funcs[key].append(ec_file[key])
    
    # In each test case file that's included, look for the regex indicating the
    # start and end of a conditional test case.
    for file in ec_files_and_funcs:
        parsed_file = []
        ec_file = open('{}/{}'.format(path_to_excec_env, file), 'r').read().split('\n')
        for line in ec_file:
            skip = False
            for expression in regex:
                if expression in line:
                    split_line = line.replace('/*', '').replace('*/', '').strip().split(expression)
                    test_name = split_line[1]
                    # If it's a test case regex, we're deleting the comment, so set skip flag to be true
                    if test_name in ec_files_and_funcs[file]:
                        skip = True
            # Base case, add the line as is
            if skip:
                continue
            parsed_file.append(line)
        
        # Overwrite existing file if there are changes
        if len(parsed_file) != len(ec_file):
            write_to = open('{}/{}'.format(path_to_excec_env, file), 'w+')
            write_to.write('\n'.join(parsed_file))
            write_to.close()
    
        
def main():
    print("OK")
    try:
        print("\n======================================================================")    
        print(" >\tChecking submission")
        cfg_file = open('{}/config/assignment_manifest.json'.format(ts_path), 'r')
        cfg_settings = json.loads(cfg_file.read())
        asg_overview = cfg_settings['assignment_overview']

        # Check for all required files and functions as well as extra credit function implementations.
        # If any of the requirements are missing, exit. 
        missing = check_for_required_files(asg_overview)
        if missing != 0:
            print(" > Detected ({}) missing required file(s)".format(missing))
            sys.exit(1)
        missing = check_files_for_required_funcs(asg_overview)
        if missing != 0:
            print(" > Detected ({}) missing required function(s)".format(missing))
            sys.exit(1)
        
        # Run the actual tests
        execute_language_specific_tests(cfg_settings)        
    except Exception:
        print(traceback.format_exc())
        
        
if __name__ == '__main__':
    main()