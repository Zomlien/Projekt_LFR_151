from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Recipe, Category

class RecipeViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.category = Category.objects.create(categoryname='Test Category')
        self.recipe = Recipe.objects.create(
            category_id=self.category,
            title='Test Recipe',
            ingredients='Test Ingredients',
            directions='Test Directions',
            creator=self.user
        )

    def test_recipe_list(self):
        response = self.client.get(reverse('recipe_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipe_list.html')

    def test_recipe_create(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('recipe_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipe_create.html')

