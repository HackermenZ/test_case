// import java.util.HashMap;
// import java.util.Scanner;

// interface MenuComponent {
//     void add(MenuComponent menuComponent);
//     void remove(MenuComponent menuComponent);
//     String getName();
//     int getPrice();
//     void display();
// }

// class MenuItem implements MenuComponent {
//     private String name;
//     private int price;

//     public MenuItem(String name, int price) {
//         this.name = name;
//         this.price = price;
//     }

//     @Override
//     public void add(MenuComponent menuComponent) {
//         // This is a leaf node, so this method is not applicable
//     }

//     @Override
//     public void remove(MenuComponent menuComponent) {
//         // This is a leaf node, so this method is not applicable
//     }

//     @Override
//     public String getName() {
//         return name;
//     }

//     @Override
//     public int getPrice() {
//         return price;
//     }

//     @Override
//     public void display() {
//         System.out.println(name + " - " + price + "tk");
//     }
// }

// class Combo implements MenuComponent {
//     private String name;
//     private HashMap<String, MenuComponent> components = new HashMap<>();
//     private int discount;
//     private boolean hasFreeItem = false;

//     public Combo(String name) {
//         this.name = name;
//     }

//     @Override
//     public void add(MenuComponent menuComponent) {
//         components.put(menuComponent.getName(), menuComponent);
//     }

//     @Override
//     public void remove(MenuComponent menuComponent) {
//         components.remove(menuComponent.getName());
//     }

//     @Override
//     public String getName() {
//         return name;
//     }

//     @Override
//     public int getPrice() {
//         int total = components.values().stream().mapToInt(MenuComponent::getPrice).sum();
//         if (hasFreeItem) total -= 50; // Assuming a fixed discount for the free item
//         return total - (total * discount / 100);
//     }

//     public void setDiscount(int discount) {
//         this.discount = discount;
//     }

//     public void setFreeItem(boolean hasFreeItem) {
//         this.hasFreeItem = hasFreeItem;
//     }

//     @Override
//     public void display() {
//         System.out.println(name + " includes:");
//         components.values().forEach(MenuComponent::display);
//         System.out.println("Total - " + this.getPrice() + "tk (Discount - " + discount + "%)");
//     }
// }

// public class MenuManager {
//     public static void main(String[] args) {
//         Scanner scanner = new Scanner(System.in);
//         HashMap<String, MenuComponent> menuItems = new HashMap<>();
//         menuItems.put("Burger", new MenuItem("Burger", 300));
//         menuItems.put("Fries", new MenuItem("Fries", 100));
//         menuItems.put("Wedges", new MenuItem("Wedges", 150));
//         menuItems.put("Shawarma", new MenuItem("Shawarma", 200));
//         menuItems.put("Drink", new MenuItem("Drink", 25));
//         menuItems.put("Combo1", new Combo("Combo1"));
//         menuItems.put("Combo2", new Combo("Combo2"));
//         menuItems.get("Combo1").add(menuItems.get("Burger"));
//         menuItems.get("Combo1").add(menuItems.get("Fries"));
//         menuItems.get("Combo1").add(menuItems.get("Drink"));
//         menuItems.get("Combo2").add(menuItems.get("Shawarma"));
//         menuItems.get("Combo2").add(menuItems.get("Drink"));

//         boolean running = true;
//         while (running) {
//             System.out.println("Press 1 to create a combo, 2 to view menu, and 0 to exit");
//             int choice = scanner.nextInt();
//             scanner.nextLine(); // Consume the newline
//             switch (choice) {
//                 case 1:
//                     System.out.println("Enter the name of the combo:");
//                     String comboName = scanner.nextLine();
//                     Combo newCombo = new Combo(comboName);
//                     boolean editing = true;
//                     while (editing) {
//                         System.out.println("Available commands: Add [item], Remove [item], Free [item], Discount [percentage], Done");
//                         String command = scanner.nextLine();
//                         String[] parts = command.split(" ");
//                         switch (parts[0].toLowerCase()) {
//                             case "add":
//                                 newCombo.add(menuItems.get(parts[1]));
//                                 break;
//                             case "remove":
//                                 newCombo.remove(menuItems.get(parts[1]));
//                                 break;
//                             case "free":
//                                 newCombo.setFreeItem(true);
//                                 break;
//                             case "discount":
//                                 newCombo.setDiscount(Integer.parseInt(parts[1]));
//                                 break;
//                             case "done":
//                                 editing = false;
//                                 menuItems.put(comboName, newCombo);
//                                 break;
//                             default:
//                                 System.out.println("Invalid command");
//                                 break;
//                         }
//                     }
//                     newCombo.display();
//                     break;
//                 case 2:
//                     menuItems.values().forEach(MenuComponent::display);
//                     break;
//                 case 0:
//                     running = false;
//                     break;
//                 default:
//                     System.out.println("Invalid option");
//                     break;
//             }
//         }
//         scanner.close();
//     }
// }


import java.util.*;

interface MenuItem {
    String getName();
    double getPrice();
    void display();
}

class FoodItem implements MenuItem {
    private String name;
    private double price;

    public FoodItem(String name, double price) {
        this.name = name;
        this.price = price;
    }

    @Override
    public String getName() {
        return name;
    }

    @Override
    public double getPrice() {
        return price;
    }

    @Override
    public void display() {
        System.out.println(name + " - " + price + "tk");
    }
}

class Combo implements MenuItem {
    private String name;
    private List<MenuItem> items;
    private double discount;
    private List<MenuItem> freeItems;

    public Combo(String name) {
        this.name = name;
        this.items = new ArrayList<>();
        this.discount = 0;
        this.freeItems = new ArrayList<>();
    }

    public void addItem(MenuItem item) {
        items.add(item);
    }

    public void removeItem(String itemName) {
        items.removeIf(item -> item.getName().equalsIgnoreCase(itemName));
    }

    public void addFreeItem(MenuItem item) {
        freeItems.add(item);
    }

    public void applyDiscount(double discount) {
        this.discount = discount;
    }

    @Override
    public String getName() {
        return name;
    }

    @Override
    public double getPrice() {
        double totalPrice = items.stream().mapToDouble(MenuItem::getPrice).sum();
        return totalPrice * (1 - discount / 100);
    }

    @Override
    public void display() {
        System.out.println(name + ":");
        for (MenuItem item : items) {
            item.display();
        }
        for (MenuItem freeItem : freeItems) {
            System.out.println(freeItem.getName() + " (Free!!!)");
        }
        System.out.println("Total - " + getPrice() + "tk");
        if (discount > 0) {
            System.out.println("Discount - " + discount + "%");
        }
    }
}

public class MenuManager {
    private static Map<String, MenuItem> menu = new HashMap<>();

    public static void main(String[] args) {
        initializeMenu();
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.println("Press 1 to create a combo, 2 to view menu and 0 to exit");
            int choice = scanner.nextInt();
            scanner.nextLine();

            if (choice == 0) break;

            switch (choice) {
                case 1:
                    createCombo(scanner);
                    break;
                case 2:
                    viewMenu();
                    break;
                default:
                    System.out.println("Invalid option, please try again.");
            }
        }
        scanner.close();
    }

    private static void initializeMenu() {
        menu.put("Burger", new FoodItem("Burger", 300));
        menu.put("Fries", new FoodItem("Fries", 100));
        menu.put("Wedges", new FoodItem("Wedges", 150));
        menu.put("Shawarma", new FoodItem("Shawarma", 200));
        menu.put("Drink", new FoodItem("Drink", 25));

        Combo combo1 = new Combo("Combo1 (Burger + Fries + Drink)");
        combo1.addItem(menu.get("Burger"));
        combo1.addItem(menu.get("Fries"));
        combo1.addItem(menu.get("Drink"));
        combo1.applyDiscount(5.882352941); // 6.25% discount
        menu.put("Combo1", combo1);

        Combo combo2 = new Combo("Combo2 (Shawarma + Drink)");
        combo2.addItem(menu.get("Shawarma"));
        combo2.addItem(menu.get("Drink"));
        combo2.applyDiscount(4.44444444444444444444444);
        menu.put("Combo2", combo2);
    }

    private static void createCombo(Scanner scanner) {
        System.out.println("Enter the name of the combo:");
        String comboName = scanner.nextLine();
        Combo newCombo = new Combo(comboName);

        while (true) {
            System.out.println("Available commands: Add [item], Remove [item], Free [item], Discount [percentage], Done");
            String command = scanner.nextLine();
            String[] parts = command.split(" ", 2);

            if (parts[0].equalsIgnoreCase("Done")) {
                break;
            } else if (parts[0].equalsIgnoreCase("Add")) {
                MenuItem item = menu.get(parts[1]);
                if (item != null) {
                    newCombo.addItem(item);
                } else {
                    System.out.println("Item not found in menu.");
                }
            } else if (parts[0].equalsIgnoreCase("Remove")) {
                newCombo.removeItem(parts[1]);
            } else if (parts[0].equalsIgnoreCase("Free")) {
                MenuItem item = menu.get(parts[1]);
                if (item != null) {
                    newCombo.addFreeItem(item);
                } else {
                    System.out.println("Item not found in menu.");
                }
            } else if (parts[0].equalsIgnoreCase("Discount")) {
                try {
                    double discount = Double.parseDouble(parts[1]);
                    newCombo.applyDiscount(discount);
                } catch (NumberFormatException e) {
                    System.out.println("Invalid discount percentage.");
                }
            } else {
                System.out.println("Invalid command, please try again.");
            }
        }

        menu.put(comboName, newCombo);
        System.out.println("Your combo:");
        newCombo.display();
    }

    private static void viewMenu() {
        for (MenuItem item : menu.values()) {
            item.display();
            System.out.println();
        }
    }
}
