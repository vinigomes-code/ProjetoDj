from .test_recipe_base import RecipeTestBase
from django.core.exceptions import ValidationError

class RecipeModelTeste(RecipeTestBase):
    def setUp(self) -> None:
        self.recipe = self.make_recipe()
        return super().setUp()
    
    def test_recipe_title_raises_error_if_title_has_more_than_65_chars(self):
        self.recipe.title = 'A' * 70

        with self.assertRaises(ValidationError):
            self.recipe.full_clean() # AQUI OCORRE A VALIDAÇÃO

        """ self.recipe.save() # o django vai salvar isso na base de dados
        self.fail(self.recipe.title) """

    def test_recipe_fields_max_length(self):
        fields = [
            ('title', 65),
            ('description', 165),
            ('preparation_time_unit', 65),
            ('servings_unit', 65),
        ]

        for field, max_length in fields:
            with self.subTest(field=field, max_length=max_length):
                setattr(self.recipe, field, 'A' * (max_length + 0))
                with self.assertRaises(ValidationError):
                        self.recipe.full_clean() 
            