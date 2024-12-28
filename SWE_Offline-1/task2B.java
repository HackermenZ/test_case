// Customer types
enum CustomerType {
    REGULAR, PREMIUM, VIP
}

// Abstract Operation class
abstract class BankOperation {
    protected CustomerType customerType;

    public BankOperation(CustomerType customerType) {
        this.customerType = customerType;
    }

    public abstract double calculateInterest(double amount, int years);
}

// Concrete SavingsAccount class
class SavingsAccount extends BankOperation {
    public SavingsAccount(CustomerType customerType) {
        super(customerType);
    }

    @Override
    public double calculateInterest(double amount, int years) {
        double rate = switch (customerType) {
            case REGULAR -> 0.025;
            case PREMIUM -> 0.035;
            case VIP -> 0.05;
        };
        return amount * rate * years; // Simple interest formula
    }
}

// Concrete Loan class
class Loan extends BankOperation {
    public Loan(CustomerType customerType) {
        super(customerType);
    }

    @Override
    public double calculateInterest(double amount, int years) {
        double rate = switch (customerType) {
            case REGULAR -> 0.14;
            case PREMIUM -> 0.12;
            case VIP -> 0.10;
        };
        return amount * rate * years; // Simple interest formula
    }
}

// Factory for creating bank operations
class BankOperationFactory {
    public static BankOperation createOperation(String operationType, CustomerType customerType) {
        return switch (operationType.toLowerCase()) {
            case "savings" -> new SavingsAccount(customerType);
            case "loan" -> new Loan(customerType);
            default -> throw new IllegalArgumentException("Invalid operation type");
        };
    }
}

// Main class for demonstration
public class task2B {
    public static void main(String[] args) {
        // Simulate user input
        CustomerType customerType = CustomerType.VIP;
        String operationType = "savings";
        double amount = 10000;
        int years = 5;

        BankOperation operation = BankOperationFactory.createOperation(operationType, customerType);
        double interest = operation.calculateInterest(amount, years);

        System.out.println("Customer Type: " + customerType);
        System.out.println("Operation Type: " + operationType);
        System.out.println("Amount: $" + amount);
        System.out.println("Years: " + years);
        System.out.println("Total Interest: $" + interest);
    }
}