from functools import wraps
from typing import List

CommandList: List[str] = []
CommandFunction: dict = {}
HelpList: dict = {}
ArgsList: dict = {}

def EnforceKwargs(**defaultKwargs):
    def decorator(f):
        @wraps(f)
        def g(*args, **kwargs):
            new_args = {}
            new_kwargs = defaultKwargs
            varnames = f.__code__.co_varnames
            new_kwargs.update(kwargs)
            for k, v in defaultKwargs.items():
                if k in varnames:
                    i = varnames.index(k)
                    new_args[(i, k)] = new_kwargs.pop(k)
            full_args = list(args)
            for i, k in sorted(new_args.keys()):
                if i <= len(full_args): full_args.insert(i, new_args.pop((i, k)))
                else: break
            for (i, k), val in new_args.items():
                new_kwargs[k] = val
            return f(*tuple(full_args), **new_kwargs)
        return g
    return decorator

@EnforceKwargs(help="")
def RegisterCommand(*nonkwargs, **args):
    CommandList.append(args["command"])
    HelpList[args["command"]] = args["help"]
    ArgsList[args["command"]] = args["arguments"]
    def function(func):
        CommandFunction[args["command"]] = func
        return func
    return function

