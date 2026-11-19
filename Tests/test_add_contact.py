import random
from Models.Contact import Contact
from Pages.add_contact_page import ContactPage


def test_add_contact(authenticated_client):
    contact_page = ContactPage(authenticated_client)
    random_suffix = random.randint(1, 1000000)


    contact = Contact(
        "Nicole",
        f"test@gmail.com",
        f"05220{random_suffix}",
        "Haifa",
        "QA",
    )

    contact_page.open_contact_form()
    contact_page.fill_contact(contact)
    contact_page.submit_contact()

    assert contact_page.contact_card_visible(contact.phone)
