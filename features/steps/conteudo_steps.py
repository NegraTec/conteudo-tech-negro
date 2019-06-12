from behave import given, when, then, step

@given('que existe conteudos cadastrados')
def step_impl(context):
    # criar autora
    # criar conteudo
    raise AssertionError('Nao foi implementado')

@when('um sistema chama a url /conteudos com o token')
def step_impl(context):  # -- NOTE: number is converted into integer
    raise AssertionError('Nao foi implementado')

@then('a url retornara a lista de todos os conteudos cadastrados')
def step_impl(context):
    raise AssertionError('Nao foi implementado')