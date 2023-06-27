def teste_args_kwargs(arg1, arg2, arg3, arg4):
    print('arg1: ', arg1)
    print('arg2: ', arg2)
    print('arg3: ', arg3)
    print('arg4: ', arg4)


args = ('um', 2, 3, 4)
teste_args_kwargs(*args)
kwargs = {'arg4': 4, 'arg3': 3, 'arg2': 2, 'arg1': 'um'}
teste_args_kwargs(**kwargs)
