from project.bakery import Bakery


b = Bakery("test_bakery")
print(b.add_food("Bread", "test_food_bread", 100))
print(b.add_food("Cake", "test_food_cake", 100))
print(b.add_drink("Tea", "test_drink_tea", 150, "test_brand_tea"))
print(b.add_drink("Water", "test_drink_water", 150, "test_brand_water"))
print(b.add_table("InsideTable", 10, 10))
# print(b.add_table("OutsideTable", 51, 12))
# print(b.reserve_table(10))
# b.order_food(10, "test_food_bread")
# print(b.order_food(10, "mahmut"))
# b.order_drink(10, "test_drink_tea")
# print(b.order_drink(10, "tuncer"))
# print(b.leave_table(10))
# print(b.get_total_income())
