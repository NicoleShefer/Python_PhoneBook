from faker import Faker

from Models.Contact import Contact
from Pages.add_contact_page import ContactPage
from Pages.contacts_page import ContactsPage

fake = Faker()
def create_contact():
    return Contact(
        fake.first_name(),
        fake.last_name(),
        fake.numerify("05#########"),
        fake.email(),
        fake.street_address(),
    )
        #fake.sentence(nb_words=2)



def test_edit_contact_name_field(authentification):
    contact_page = ContactPage(authentification)
    contacts_page = ContactsPage(authentification)

    contact = create_contact()

    contact_page.create_contact(contact)

    new_name = fake.first_name()