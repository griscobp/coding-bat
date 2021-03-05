'''
the Warmup-1/monkey_trouble from Coding Bat
'''
def monkey_trouble(a_smile: bool, b_smile: bool):
  '''
  Takes two parameter that indicate if the 2 monkeys are
  smiling or not. If both or neither are smiling, we are in 
  trouble, otherwise, we're ok.
  '''
  #                      Both          or               Neither
  return True if (a_smile and b_smile) or (not a_smile and not b_smile) else False