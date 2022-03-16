import glob
import re
import os

def grab_all_files(args,rests,root_dir='.'):
    wildcard = translate_rule_to_glob(args,rests,root_dir=root_dir)
    full_wildcard = os.path.join(root_dir,wildcard)
    fns = [os.path.basename(fn) for fn in glob.glob(full_wildcard)]
    return fns

def separate_arg_and_rest(rule):
    args_container = []
    rest_container  =[]
    arg_tmp = []
    rest_tmp = []
    arg_started = False
    for i in rule:
        if i == "}":
            arg_started = False
            args_container.append("".join(arg_tmp))
            arg_tmp = []
        elif i == "{":
            arg_started = True
            rest_container.append("".join(rest_tmp))
            rest_tmp = []
        else:
            if arg_started:
                arg_tmp.append(i)
            else:
                rest_tmp.append(i)
    if rule[-1] == "}":
        # if rule ends with an arg,
        pass
    else:
        # if rule doesn't end with an arg, meaning theres a little tail
        rest_container.append("".join(rest_tmp))
    if len(args_container) > len(set(args_container)):
        raise ValueError('Argument Names are duplicated!')
    return args_container, rest_container

def translate_rule_to_pyregex(args,rests):
    to_be_matched = "^"
    for arg, rest in zip(args, rests):
        to_be_matched += re.escape(rest) + "(?P<" + arg + ">.*?)"
    if len(rests) == len(args):
        # if rule end with an arg,
        to_be_matched += "$"
    else:
        # if rule doesn't end with an arg, meaning theres a little tail
        to_be_matched += rests[-1] + "$"
    return to_be_matched

def translate_rule_to_glob(args,rests,root_dir='.'):
    to_be_matched = ""
    for rest in rests[:-1]:
        to_be_matched += rest + "*"
    if len(rests) == len(args):
        # if rule end with an arg,
        pass
    else:
        # if rule doesn't end with an arg, meaning theres a little tail
        to_be_matched += rests[-1]
    return to_be_matched


def parse_and_match(regexable,fns):
    """
    Input is a rule. This function finds all the files that fits the rule in root_dir.
    It also labels all graphs.
    - Example: "filename_stems_{arg1}_{arg2}_stems_{args3}.{args4}"
    """
    pattern = re.compile(regexable)
    fn2labels = {fn:pattern.match(fn).groupdict() for fn in fns}
    return fn2labels

def parse_and_grab(rule,root_dir='.'):
    args, rests = separate_arg_and_rest(rule)
    regexable = translate_rule_to_pyregex(args, rests)
    fns = grab_all_files(args, rests, root_dir=root_dir)
    fn2labels = parse_and_match(regexable,fns)
    return fn2labels
    