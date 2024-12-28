// Step 1: Create an interface for TicketingSystem
interface TicketingSystem {
    void addDisplay();
    void addController();
    void addInternetModule();
}

// Step 2: Create Concrete Classes for each Package
class BasicPackage implements TicketingSystem {
    @Override
    public void addDisplay() {
        System.out.println("ATMega32 with LCD display has been added.");
    }
    @Override
    public void addController() {
        System.out.println("ATMega32 controller has been added.");
    }
    @Override
    public void addInternetModule() {
        System.out.println("WiFi or GSM module has been added.");
    }
}

class StandardPackage implements TicketingSystem {
    @Override
    public void addDisplay() {
        System.out.println("Arduino Mega with LED display has been added.");
    }
    @Override
    public void addController() {
        System.out.println("Arduino Mega controller has been added.");
    }
    @Override
    public void addInternetModule() {
        System.out.println("WiFi or GSM module has been added.");
    }
}

class PremiumPackage implements TicketingSystem {
    @Override
    public void addDisplay() {
        System.out.println("Raspberry Pi with Touch Screen display has been added.");
    }
    @Override
    public void addController() {
        System.out.println("Raspberry Pi controller has been added.");
    }
    @Override
    public void addInternetModule() {
        System.out.println("Ethernet or WiFi has been added.");
    }
}

// Step 3: Factory to create Ticketing System
class TicketingSystemFactory {
    public static TicketingSystem getPackage(String packageType) {
        switch (packageType.toLowerCase()) {
            case "basic":
                return new BasicPackage();
            case "standard":
                return new StandardPackage();
            case "premium":
                return new PremiumPackage();
            default:
                throw new IllegalArgumentException("Invalid package type.");
        }
    }
}

// Step 4: Demonstrate Builder pattern for Internet and Web Server Selection
class TicketingSystemBuilder {
    private String internetModule;
    private String webServer;

    public TicketingSystemBuilder setInternetModule(String module) {
        this.internetModule = module;
        return this;
    }

    public TicketingSystemBuilder setWebServer(String framework) {
        this.webServer = framework;
        return this;
    }

    public void build() {
        System.out.println("Internet Module: " + internetModule);
        System.out.println("Web Server Framework: " + webServer);
    }
}

// Step 5: Demonstrate the system
public class task1 {
    public static void main(String[] args) {
        // Select package
        TicketingSystem system = TicketingSystemFactory.getPackage("premium");
        system.addDisplay();
        system.addController();
        system.addInternetModule();

        // Select Internet and Web Server
        TicketingSystemBuilder builder = new TicketingSystemBuilder()
                .setInternetModule("WiFi")
                .setWebServer("Django");
        builder.build();
    }
}