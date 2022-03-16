abstract class Item(public val id: Int, public val name: String, public val value: Double)


class Potion(id: Int, name: String, value: Double, public val healAmount: Double) : Item(id, name, value)


fun <T: Item> sortItems(items: List<T>): List<T>
    = items.sortedWith(compareBy({ it.name }, { -it.value }))


fun main() {
    val potions = listOf(
        Potion(1, "Healing potion", 10.0, 50.0),
        Potion(2, "Max heal", 1000.0, 9999.9),
        Potion(3, "Decent potion", 30.0, 120.0)
    )
    val potionsSorted = sortItems(potions)
    print(potionsSorted[1].healAmount)
}
