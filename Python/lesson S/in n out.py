class employee :
    def __init__(self):
        print ('Employee created')

    def __del__(self):
        print("Destructor called")

def create_obj():
    print('making object...')
    obj = employee()
    print('function end...')
    return obj

print ('calling Create-obj() function...')
obj = create_obj()
print('Program End...')