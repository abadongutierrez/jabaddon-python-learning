from models import GroceryItem, MealPlan, ShoppingCategory, GroceryShoppingPlan

sample_item = GroceryItem(
    name="Chicken Breast",
    quantity="2 lbs",
    estimated_price="$8-12",
    category="Meat"
)

type(sample_item)
print(sample_item.model_dump_json(indent=2))

try:
    invalid_item = GroceryItem(
        name="Chicken Breast",
        quantity="2 lbs",
        estimated_price="$8-12",
        category=12.0
    )
except Exception as e:
    print("Error creating invalid GroceryItem:")
    print(e)

# Display structured data
# print("🛒 Sample Grocery Item Structure:")
# print(JSON(sample_item.model_dump()))

sample_meal = MealPlan(
    meal_name="Chicken Stir Fry",
    difficulty_level="Easy",
    servings=4,
    researched_ingredients=["chicken breast", "broccoli", "bell peppers", "garlic", "soy sauce", "rice"]
)
print("\n🍽️ Sample Meal Plan Structure:")
print(sample_meal.model_dump_json(indent=2))

sample_section = ShoppingCategory(
    section_name="Produce",
    items=[
        GroceryItem(name="Bell Peppers", quantity="3 pieces", estimated_price="$3-4", category="Produce"),
        GroceryItem(name="Onions", quantity="2 lbs", estimated_price="$2-3", category="Produce")
    ],
    estimated_total="$5-7"
)

print("\n🏪 Sample Shopping Section:")
print(sample_section.model_dump_json(indent=2))

# Display structured data
print("\n🏬 Sample Shopping Section as Dictionary:")
print(sample_section.model_dump())  # Display as dictionary
print(sample_section.model_dump_json(indent=2))  # Display as JSON string

