interface Coffee {
    String getIngredients();
    int getCost();
}

// Concrete component for black coffee
class BasicBlackCoffee implements Coffee {
    @Override
    public String getIngredients() {
        return "Water, Grinded Coffee Beans";
    }

    @Override
    public int getCost() {
        return 130; // 100 for the mug + 30 for coffee beans
    }
}

// Concrete component for milk coffee
class BasicMilkCoffee implements Coffee {
    @Override
    public String getIngredients() {
        return "Milk, Grinded Coffee Beans";
    }

    @Override
    public int getCost() {
        return 180; // 100 for the mug + 30 for coffee beans + 50 for milk
    }
}

// Decorator for additional grinded coffee beans in Americano
class Americano extends CoffeeDecorator {
    public Americano(Coffee coffee) {
        super(coffee);
    }

    @Override
    public String getIngredients() {
        return super.getIngredients() + ", Extra Grinded Coffee Beans";
    }

    @Override
    public int getCost() {
        return super.getCost() + 30; // additional 30 taka for extra beans
    }
}

// Decorator for cinnamon in Cappuccino
class Cappuccino extends CoffeeDecorator {
    public Cappuccino(Coffee coffee) {
        super(coffee);
    }

    @Override
    public String getIngredients() {
        return super.getIngredients() + ", Cinnamon Powder";
    }

    @Override
    public int getCost() {
        return super.getCost() + 50; // additional 50 taka for cinnamon
    }
}

// Abstract decorator class that implements Coffee
abstract class CoffeeDecorator implements Coffee {
    protected Coffee decoratedCoffee;

    public CoffeeDecorator(Coffee coffee) {
        this.decoratedCoffee = coffee;
    }

    @Override
    public String getIngredients() {
        return decoratedCoffee.getIngredients();
    }

    @Override
    public int getCost() {
        return decoratedCoffee.getCost();
    }
}

// Main class as provided
public class CoffeeTong {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Order order = new Order();

        while (true) {
            System.out.println("Select coffee type (1: Americano, 2: Cappuccino, 0: Finish): ");
            int choice = scanner.nextInt();
            if (choice == 0) break;

            Coffee coffee;
            switch (choice) {
                case 1:
                    coffee = new Americano(new BasicBlackCoffee());
                    break;
                case 2:
                    coffee = new Cappuccino(new BasicMilkCoffee());
                    break;
                default:
                    System.out.println("Invalid choice.");
                    continue;
            }
            order.addCoffee(coffee);
        }

        order.printOrderDetails();
        scanner.close();
    }
}
