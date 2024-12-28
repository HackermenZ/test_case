// Ticketing System Components
interface Component {
    void add();
}

class Microcontroller implements Component {
    private String name;

    public Microcontroller(String name) {
        this.name = name;
    }

    @Override
    public void add() {
        System.out.println(name + " has been added to the system");
    }
}

class Display implements Component {
    private String type;

    public Display(String type) {
        this.type = type;
    }

    @Override
    public void add() {
        System.out.println(type + " display has been added to the system");
    }
}

class IdentificationSystem implements Component {
    private String type;

    public IdentificationSystem(String type) {
        this.type = type;
    }

    @Override
    public void add() {
        System.out.println(type + " identification system has been added");
    }
}

class InternetConnection implements Component {
    private String type;

    public InternetConnection(String type) {
        this.type = type;
    }

    @Override
    public void add() {
        System.out.println(type + " internet connection has been added");
    }
}

class Storage implements Component {
    private String type;

    public Storage(String type) {
        this.type = type;
    }

    @Override
    public void add() {
        System.out.println(type + " storage has been added");
    }
}

class WebServer implements Component {
    private String framework;

    public WebServer(String framework) {
        this.framework = framework;
    }

    @Override
    public void add() {
        System.out.println(framework + " web server has been added");
    }
}

// Abstract Factory for Ticketing System
interface TicketingSystemFactory {
    Microcontroller createMicrocontroller();
    Display createDisplay();
    IdentificationSystem createIdentificationSystem();
    Storage createStorage();
}

// Concrete Factories
class BasicPackageFactory implements TicketingSystemFactory {
    @Override
    public Microcontroller createMicrocontroller() {
        return new Microcontroller("ATMega32");
    }

    @Override
    public Display createDisplay() {
        return new Display("LCD");
    }

    @Override
    public IdentificationSystem createIdentificationSystem() {
        return new IdentificationSystem("RFID");
    }

    @Override
    public Storage createStorage() {
        return new Storage("SD card");
    }
}

class StandardPackageFactory implements TicketingSystemFactory {
    @Override
    public Microcontroller createMicrocontroller() {
        return new Microcontroller("Arduino Mega");
    }

    @Override
    public Display createDisplay() {
        return new Display("LED");
    }

    @Override
    public IdentificationSystem createIdentificationSystem() {
        return new IdentificationSystem("RFID");
    }

    @Override
    public Storage createStorage() {
        return new Storage("SD card");
    }
}

class AdvancedPackageFactory implements TicketingSystemFactory {
    @Override
    public Microcontroller createMicrocontroller() {
        return new Microcontroller("Raspberry Pi");
    }

    @Override
    public Display createDisplay() {
        return new Display("OLED");
    }

    @Override
    public IdentificationSystem createIdentificationSystem() {
        return new IdentificationSystem("NFC");
    }

    @Override
    public Storage createStorage() {
        return new Storage("Built-in");
    }
}

class PremiumPackageFactory implements TicketingSystemFactory {
    @Override
    public Microcontroller createMicrocontroller() {
        return new Microcontroller("Raspberry Pi");
    }

    @Override
    public Display createDisplay() {
        return new Display("Touch Screen");
    }

    @Override
    public IdentificationSystem createIdentificationSystem() {
        return new IdentificationSystem("NFC");
    }

    @Override
    public Storage createStorage() {
        return new Storage("Built-in");
    }
}

// Builder for Ticketing System
class TicketingSystemBuilder {
    private TicketingSystemFactory factory;
    private InternetConnection internetConnection;
    private WebServer webServer;

    public TicketingSystemBuilder(TicketingSystemFactory factory) {
        this.factory = factory;
    }

    public TicketingSystemBuilder setInternetConnection(String type) {
        this.internetConnection = new InternetConnection(type);
        return this;
    }

    public TicketingSystemBuilder setWebServer(String framework) {
        this.webServer = new WebServer(framework);
        return this;
    }

    public void build() {
        factory.createMicrocontroller().add();
        factory.createDisplay().add();
        factory.createIdentificationSystem().add();
        factory.createStorage().add();
        internetConnection.add();
        webServer.add();
    }
}

// Main class for demonstration
public class task1B {
    public static void main(String[] args) {
        // Simulate user input
        String packageChoice = "Premium";
        String internetOption = "WiFi";
        String webFramework = "Django";

        TicketingSystemFactory factory;
        switch (packageChoice) {
            case "Basic":
                factory = new BasicPackageFactory();
                break;
            case "Standard":
                factory = new StandardPackageFactory();
                break;
            case "Advanced":
                factory = new AdvancedPackageFactory();
                break;
            case "Premium":
                factory = new PremiumPackageFactory();
                break;
            default:
                throw new IllegalArgumentException("Invalid package choice");
        }

        TicketingSystemBuilder builder = new TicketingSystemBuilder(factory);
        builder.setInternetConnection(internetOption)
               .setWebServer(webFramework)
               .build();
    }
}