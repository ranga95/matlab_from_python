import matlab.engine
def matlab_start():
    eng=matlab.engine.start_matlab("-desktop")
l=['r',67]
eng.workspace['y'] = l
print(eng.workspace['y'])
print(type(eng.workspace['y']))
