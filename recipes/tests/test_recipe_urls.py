from django.test import TestCase
from django.urls import reverse
""" TESTCASE DERIVA DE UNITTEST DO PYTHON """

class RecipeURLsTest(TestCase):
    
    #def test_the_pytest_is_ok(self):
    #    assert 1 == 1, 'Um é igual a um'
    #    assert : dizer que é verdade - assert 1 = 2
    
    # A função resolve é usada para converter uma URL em uma view
    # A função reverse é usada para converter o view em url.

    # São considerados Test Fixtures quaisquer informações que dão suporte aos testes. Podem ser arquivos externos, bases de dados, dados, código Python e várias outras coisas.

    # NÃO TESTAMOS COISAS DE FUNCIONALIDADES DO PRÓPRIO DJANGO, OS PRÓPRIOS DESENVOLVEDORES JÁ TESTARAM
    # TESTAMOS A NOSSA LÓGICA DO SITE

    def test_recipe_home_url_is_correct(self):
        url = reverse('recipes:home')
        self.assertEqual(url, '/')

    def test_recipe_category_home_url_is_correct(self):
        url = reverse('recipes:category', kwargs={'category_id': 1})
        self.assertEqual(url, '/recipes/category/1/')
    
    def test_recipe_detail_home_url_is_correct(self):
        url = reverse('recipes:recipe', kwargs={'id': 1})
        self.assertEqual(url, '/recipes/1/')
    
    def test_recipe_search_url_is_correct(self):
        url = reverse('recipes:search')
        self.assertEqual(url, '/recipes/search/')

    # TDD: RED - GREEN - REFACTOR