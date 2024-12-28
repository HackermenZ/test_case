interface payment{
    void processPayment();
}
class creditCard implements payment{

    @Override
    public void processPayment() {
        System.out.println("Payment Successful via creditCard");
    }
}

class paypal implements payment{

    @Override
    public void processPayment() {
        System.out.println("Payment Successful via paypal");
    }
}

class bitCoin implements payment{

    @Override
    public void processPayment() {
        System.out.println("Payment Successful via bitcoin");
    }
}

abstract class paymentFactory{
    abstract payment paymentMethod();
}
class creditFactory extends paymentFactory{

    @Override
    public payment paymentMethod(){
        return new creditCard();
    }
}

class paypalFactory extends paymentFactory{

    @Override
    public payment paymentMethod(){
        return new paypal();
    }
}

class BitcoinFactory extends paymentFactory{

    @Override
    public payment paymentMethod(){
        return new bitCoin();
    }
}


public class online {
    public static void main(String[] args) {
        System.out.println("Enter a payment method");
    }
}
