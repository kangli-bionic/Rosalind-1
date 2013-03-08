import sys
from rosalind import *

problems = {k: v for k, v in [(item[len('problem_'):], item)
                              for item in dir()
                              if item.startswith('problem_')]}

def help():
    print "Type 'help' to display this text at any time."
    print "Type 'prob' to display a list of problems."
    print "Type 'exit' to exit."

if __name__ == "__main__":
    help()

    while True:
        problem_code = raw_input('Please choose a problem to solve:  ').strip()
        try:
            problem = problems[problem_code]
            eval('{}()'.format(problem))
        except:
            if problem_code == 'help':
                help()

            elif problem_code in ('prob', 'problems'):
                print "Here is a list of problems."
                for i in problems:
                    print i

            elif problem_code == 'exit':
                eval('exit()')

            else:
                print "I'm sorry, that's not a valid problem."
