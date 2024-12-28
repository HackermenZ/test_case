import java.util.ArrayList;
import java.util.List;

// Interface for menu components (both individual items and combos)
interface MenuComponent {
    void add(MenuComponent component);
    void remove(MenuComponent component);
    String getName();
    int getPrice();
    void display();
}

// Leaf component representing individual menu items
class MenuItem implements MenuComponent {
    private String name;
    private int price;

    public MenuItem(String name, int price) {
        this.name = name;
        this.price = price;
    }

    public void add(MenuComponent component) {
        // Leaf nodes do not support this operation
        throw new UnsupportedOperationException();
    }

    public void remove(MenuComponent component) {
        // Leaf nodes do not support this operation
        throw new UnsupportedOperationException();
    }

    public String getName() {
        return name;
    }

    public int getPrice() {
        return price;
    }

    public void display() {
        System.out.println(name + " - " + price + "tk");
    }
}

// Composite component representing a combination of items
class MenuCombo implements MenuComponent {
    private List<MenuComponent> components = new ArrayList<>();
    private String name;
    private int discount;

    public MenuCombo(String name, int discount) {
        this.name = name;
        this.discount = discount;
    }

    public void add(MenuComponent component) {
        components.add(component);
    }

    public void remove(MenuComponent component) {
        components.remove(component);
    }

    public String getName() {
        return name;
    }

    public int getPrice() {
        int total = components.stream().mapToInt(MenuComponent::getPrice).sum();
        return total - (total * discount / 100);
    }

    public void display() {
        System.out.println(name + " includes:");
        for (MenuComponent component : components) {
            component.display();
        }
        System.out.println("Total - " + getPrice() + "tk (Discount - " + discount + "%)");
    }
}

// Main class to run the example
public class RestaurantMenu {
    public static void main(String[] args) {
        // Create individual menu items
        MenuItem burger = new MenuItem("Burger", 300);
        MenuItem fries = new MenuItem("Fries", 100);
        MenuItem drink = new MenuItem("Drink", 25);

        // Create a combo
        MenuCombo combo1 = new MenuCombo("Combo1", 10); // 10% discount
        combo1.add(burger);
        combo1.add(fries);
        combo1.add(drink);

        // Displaying the combo
        combo1.display();
    }
}
