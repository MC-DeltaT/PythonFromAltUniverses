import java.time.LocalDate

data class Address(
    val country: String,
    val state: String,
    val suburb: String,
    val street: String,
    val houseNumber: Int,
    val unitNumber: Int? = null
)

data class Person(
    val name: String,
    val dob: LocalDate
)


fun main() {
    val addressbook = mutableMapOf<Address, List<Person>>()
    val address1 = Address("Australia", "WA", "Baywater", "Guildford Rd", 25)
    val person = Person("Foo Bar", LocalDate.of(2022, 3, 1))
    addressbook[address1] = listOf(person)

    val address2 = address1.copy(houseNumber=26)
    addressbook[address2] = listOf(person)

    print(addressbook)
}
