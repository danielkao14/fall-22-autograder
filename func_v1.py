from intbase import InterpreterBase

# FuncInfo is a class that represents information about a function
# Right now, the only thing this tracks is the line number of the first executable instruction
# of the function (i.e., the line after the function prototype: func foo)
class FuncInfo:
  def __init__(self, start_ip):
    self.start_ip = start_ip # line number, zero-based
    self.paramlist = []
    self.returntype = None

  def set_param(self, paramtype):
    self.paramlist.append(paramtype)
  
  def get_param(self):
    return self.paramlist
  
  def set_returntype(self, returntype):
    self.returntype = returntype
  
  def get_returntype(self):
    return self.returntype
# FunctionManager keeps track of every function in the program, mapping the function name
# to a FuncInfo object (which has the starting line number/instruction pointer) of that function.
class FunctionManager:
  def __init__(self, tokenized_program):
    self.func_cache = {}
    self._cache_function_line_numbers(tokenized_program)
    #write function to parse function parameters: store inside a tuple?
    #write function to parse function return type

  def get_function_info(self, func_name):
    if func_name not in self.func_cache:
      return None
    return self.func_cache[func_name]

  def _cache_function_line_numbers(self, tokenized_program):
    for line_num, line in enumerate(tokenized_program):
      if line and line[0] == InterpreterBase.FUNC_DEF:
        func_name = line[1]
        func_info = FuncInfo(line_num + 1)   # function starts executing on line after funcdef
        self.func_cache[func_name] = func_info
  
  def _parse_return_type(self, tokenize_program):
    for line in tokenized_program:
      if line and line[0] == InterpreterBase.FUNC_DEF:
        func_name - line[1]
        if (func_name not in self.func_cache):
          super().error(ErrorType.SYNTAX_ERROR,"function does not exist to get return type") #no
        func_type = line[-1]
        self.func_cache[func_name].set_returntype(func_type)

  def _parse_param(self, tokenize_program):
    for line in tokenized_program:
      if line and line[0] == InterpreterBase.FUNC_DEF:
        func_name - line[1]
        if (func_name not in self.func_cache):
          super().error(ErrorType.SYNTAX_ERROR,"function does not exist to get return type") #no
        for token in line[2:-1]:
          paramtype = token.split(":")[1]
          self.func_cache[func_name].set_param(paramtype)