from django.test import TestCase
from diary.models import Page, Diary, Tag


class TestingModels(TestCase):

    def setUp(self):
        """
        Set up creating database's objects
        """

        Diary.objects.create(username='tony')
        Diary.objects.create(username='tintin')
        diary = Diary.objects.all()
        Tag.objects.create(name='happy')
        Tag.objects.create(name='sad')
        tag = Tag.objects.all()
        Page.objects.create(
            diary=diary[0], title='title' ,tag=tag[0], story='This was awesome', date='today', picture='pic1.jpg')
        Page.objects.create(
            diary=diary[1], title='title', tag=tag[1], story='This was awesome', date='today', picture='pic1.jpg')

    def test_diary_username(self):
        """
        Test the diary object's username.
        """

        diary = Diary.objects.all()
        self.assertEqual(diary[0].username, 'tony')
        self.assertEqual(diary[1].username, 'tintin')

    def test_tag_name(self):
        """
        Test the tag object' name.
        """

        tag = Tag.objects.all()
        self.assertEqual(tag[0].name, 'happy')
        self.assertEqual(tag[1].name, 'sad')

    def test_page_data(self):
        """
        Test the page object's data
        """

        page = Page.objects.all()
        self.assertEqual(page[0].diary.username, 'tony' )
        self.assertEqual(page[0].title, 'title')
        self.assertEqual(page[0].tag.name, 'happy')
        self.assertEqual(page[0].story, 'This was awesome')
        self.assertEqual(page[0].date, 'today')
        self.assertEqual(page[0].picture, 'pic1.jpg')


    def test_diary_string_representation(self):
        """
        Test that the string is correctly represented in diary.
        """

        diary = Diary.objects.all()
        self.assertEqual(str(diary[0]), diary[0].username)
        self.assertEqual(str(diary[1]), diary[1].username)

    def test_tag_string_representation(self):
        """
        Test that the string is correctly represented in diary's tag.
        """

        tag = Tag.objects.all()
        self.assertEqual(str(tag[0]), tag[0].name)
        self.assertEqual(str(tag[1]), tag[1].name)

    def test_diary_max_length(self):
        """
        Test that the max length of the field is equal or not.
        """

        diary = Diary(username='tony')
        max_length = diary._meta.get_field('username').max_length
        self.assertEquals(max_length, 30)

    def test_get_absolute_url(self):
        """
        Test that it get the correct absolue url or not.
        """
        page = Page.objects.all()
        diary = Diary.objects.all()
        self.assertEquals(page[0].get_absolute_url(), '/diary/')
        self.assertEquals(diary[0].get_absolute_url(), '/diary/')
    
    def test_diary_type_error(self):
        """
        Test that diary can't call field username.
        """
        diary = Diary.objects.create(username='user')
        self.assertRaises(TypeError, diary)
    
    def test_tag_type_error(self):
        """
        Test that tag can't call field name.
        """
        tag = Tag.objects.create(name='')
        self.assertRaises(TypeError, tag)
    
    def test_page_type_error(self):
        """
        Test that page objects should not be callable.
        """
        diary = Diary.objects.all()
        tag = Tag.objects.all()
        page = Page.objects.create(
            diary=diary[0], title='title' ,tag=tag[0], story='This was awesome', date='today', picture='pic1.jpg')
        self.assertRaises(TypeError, page)
        
    def test_query_choosen_data(self):
        """
        Test that object can query the choosen object. 
        """
        self.assertTrue(Diary.objects.filter(username='tony'))
        self.assertTrue(Page.objects.filter(title='title'))
