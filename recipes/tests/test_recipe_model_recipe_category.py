from .test_recipe_base import RecipeTestBase, Recipe
from django.core.exceptions import ValidationError
from parameterized import parameterized

class RecipeModelTeste(RecipeTestBase):
    def setUp(self) -> None:
        self.category = self.make_category(
            name='Category Testing'
        )
        return super().setUp()
    
    def test_recipe_category_model_string_representarion(self):
        self.assertEqual(
            str(self.category),
            self.category.name
        )

    def test_recipe_category_model_name_max_length_is_65_chars(self):
        self.category.name = 'A' * 66
        with self.assertRaises(ValidationError): 
            self.category.full_clean()
    

    # assertRaises(): Ela é usada para verificar se um bloco de código gera uma exceção específica.
    # Isso é útil para garantir que seu código  # trata os erros corretamente.

    # ValidationError é uma exceção no Django usada para sinalizar que os dados fornecidos para um modelo ou formulário são 
    # inválidos. É comumente usada em métodos de validação personalizados para campos de modelos e formulários.
    # Exemplo: 
    
    