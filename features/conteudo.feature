Feature: Listar Conteudos

  Scenario: Retornar todos os conteudos
    Given que existe conteudos cadastrados
    When um sistema chama a url /conteudos com o token
    Then a url retornara a lista de todos os conteudos cadastrados