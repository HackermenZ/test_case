// Step 1: Create an interface for InterestStrategy
interface InterestStrategy {
    double calculateInterest(double amount, int timePeriod);
}

// Step 2: Create concrete classes for each customer type's interest strategy
class RegularAccountInterest implements InterestStrategy {
    @Override
    public double calculateInterest(double amount, int timePeriod) {
        return amount * 0.025 * timePeriod;
    }
}

class PremiumAccountInterest implements InterestStrategy {
    @Override
    public double calculateInterest(double amount, int timePeriod) {
        return amount * 0.035 * timePeriod;
    }
}

class VIPAccountInterest implements InterestStrategy {
    @Override
    public double calculateInterest(double amount, int timePeriod) {
        return amount * 0.05 * timePeriod;
    }
}

class RegularLoanInterest implements InterestStrategy {
    @Override
    public double calculateInterest(double amount, int timePeriod) {
        return amount * 0.14 * timePeriod;
    }
}

class PremiumLoanInterest implements InterestStrategy {
    @Override
    public double calculateInterest(double amount, int timePeriod) {
        return amount * 0.12 * timePeriod;
    }
}

class VIPLoanInterest implements InterestStrategy {
    @Override
    public double calculateInterest(double amount, int timePeriod) {
        return amount * 0.10 * timePeriod;
    }
}

// Step 3: Create the BankAccount class that uses the strategy
class BankAccount {
    private InterestStrategy interestStrategy;

    public BankAccount(InterestStrategy strategy) {
        this.interestStrategy = strategy;
    }

    public double calculateInterest(double amount, int timePeriod) {
        return interestStrategy.calculateInterest(amount, timePeriod);
    }
}

// Step 4: Demonstrate the system
public class task2 {
    public static void main(String[] args) {
        // Regular Account with Regular Interest Rate
        BankAccount regularAccount = new BankAccount(new RegularAccountInterest());
        System.out.println("Regular Account Interest: " + regularAccount.calculateInterest(1000, 2));

        // VIP Loan with VIP Loan Interest Rate
        BankAccount vipLoan = new BankAccount(new VIPLoanInterest());
        System.out.println("VIP Loan Interest: " + vipLoan.calculateInterest(5000, 1));
    }
}