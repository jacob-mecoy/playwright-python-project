from playwright.sync_api import expect
from pytest_bdd import given, then

from pages.rick_and_morty.about import RickAndMortyAboutPage
from pages.rick_and_morty.documentation import RickAndMortyDocumentationPage
from pages.rick_and_morty.homepage import RickAndMortyHomepage


@given("I navigate to the homepage")
def navigate_to_homepage(homepage_page: RickAndMortyHomepage):
    homepage_page.load()


@given("I navigate to the documents page")
def navigate_to_documents(homepage_page: RickAndMortyHomepage):
    homepage_page.navigate_to_docs()


@given("I navigate to the about page")
def navigate_to_about(homepage_page: RickAndMortyHomepage):
    homepage_page.about_link.click()


@then("the homepage is loaded")
def expect_homepage_loaded(homepage_page: RickAndMortyHomepage):
    expect(homepage_page.title).to_be_visible()


@then("the documents page is loaded")
def expect_document_page_loaded(documentation_page: RickAndMortyDocumentationPage):
    expect(documentation_page.title).to_be_visible()


@then("the about page is loaded")
def expect_about_page_loaded(about_page: RickAndMortyAboutPage):
    expect(about_page.title).to_be_visible()
