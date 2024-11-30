# a library of utility functions for Rosalind exercises

#import rosalind input (first line)
def read_input(filepath):
    with open(filepath, "r") as infile:
        lines = infile.readlines()
        stripped = []
        for line in lines:
            stripped.append(line.strip())
    return stripped

#import entire file content
def import_file (filepath):
    with open(filepath, "r") as imp:
        imp_file = imp.read()
    return imp_file