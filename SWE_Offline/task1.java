interface Account{
    double calculateInterest(double principle,int time);
}
interface Loan{
    double calculateInterest(double principle,int time);
}
class RegularAccount implements Account{
    @Override
    public double calculateInterest(double principle,int time){
        return principle*.025*time;
    }
}
class PremiumAccount implements Account{
    @Override
    public double calculateInterest(double principle,int time){
        return principle*.035*time;
    }
}


class VIPAccount implements Account{
    @Override
    public double calculateInterest(double principle,int time){
        return principle*.05*time;
    }
}
class RegularLoan implements Loan{
    @Override
    public double calculateInterest(double principle,int time){
        return principle*.14*time;
    }
}


class PremiumLoan implements Loan{
    @Override
    public double calculateInterest(double principle,int time){
        return principle*.12*time;
    }
}

class VIPLoan implements Loan{
    @Override
    public double calculateInterest(double principle,int time){
        return principle*.10*time;
    }
}


abstract class CustomerFactory{
    public abstract Account createAccount();
    public abstract Loan createLoan();
}

class RegularCustomerFactory extends CustomerFactory{

    @Override
    public Account createAccount() {
        return new RegularAccount();
    }

    @Override
    public Loan createLoan() {
        return new RegularLoan();
    }
}

class PremiumCustomerFactory extends CustomerFactory{

    @Override
    public Account createAccount() {
        return new PremiumAccount();
    }

    @Override
    public Loan createLoan() {
        return new PremiumLoan();
    }
}

class VIPCustomerFactory extends CustomerFactory{

    @Override
    public Account createAccount() {
        return new VIPAccount();
    }

    @Override
    public Loan createLoan() {
        return new VIPLoan();
    }
}

public class task1 {
    public static void main(String[] args) {
        //regular part
        CustomerFactory regularFactory = new RegularCustomerFactory();
        Account regularAccount = regularFactory.createAccount();
        Loan regularLoan = regularFactory.createLoan();
        System.out.println("Regular Account Interest: " + regularAccount.calculateInterest(1000, 2));
        System.out.println("Regular Loan Interest: " + regularLoan.calculateInterest(1000, 2));

        //Premium Part
        CustomerFactory premiumFactory = new PremiumCustomerFactory();
        Account premiumAccount = premiumFactory.createAccount();
        Loan premiumLoan = premiumFactory.createLoan();

        System.out.println("Premium Account Interest: " + premiumAccount.calculateInterest(1000, 2));
        System.out.println("Premium Loan Interest: " + premiumLoan.calculateInterest(1000, 2));


        //VIP part

        CustomerFactory VIPFactory = new VIPCustomerFactory();
        Account vipAccount = VIPFactory.createAccount();
        Loan vipLoan = VIPFactory.createLoan();

        System.out.println("VIP Account Interest: " + vipAccount.calculateInterest(1000, 2));
        System.out.println("VIP Loan Interest: " + vipLoan.calculateInterest(1000, 2));



    }
}
