// Define the components
abstract class Microcontroller {
    abstract void addMicrocontroller();
}

class ATMega32 extends Microcontroller {
    void addMicrocontroller() {
        System.out.println("ATMega32 has been added to the system");
    }
}

class ArduinoMega extends Microcontroller {
    void addMicrocontroller() {
        System.out.println("Arduino Mega has been added to the system");
    }
}

class RaspberryPi extends Microcontroller {
    void addMicrocontroller() {
        System.out.println("Raspberry Pi has been added to the system");
    }
}

abstract class Display {
    abstract void addDisplay();
}

class LCD extends Display {
    void addDisplay() {
        System.out.println("LCD display has been added to the system");
    }
}

class LED extends Display {
    void addDisplay() {
        System.out.println("LED display has been added to the system");
    }
}

class OLED extends Display {
    void addDisplay() {
        System.out.println("OLED display has been added to the system");
    }
}

class TouchScreen extends Display {
    void addDisplay() {
        System.out.println("Touch screen display has been added to the system");
    }
}

// Factory Method Pattern
abstract class PackageFactory {
    abstract Microcontroller createMicrocontroller();
    abstract Display createDisplay();
}

class BasicPackageFactory extends PackageFactory {
    Microcontroller createMicrocontroller() {
        return new ATMega32();
    }
    Display createDisplay() {
        return new LCD();
    }
}

class StandardPackageFactory extends PackageFactory {
    Microcontroller createMicrocontroller() {
        return new ArduinoMega();
    }
    Display createDisplay() {
        return new LED();
    }
}

class AdvancedPackageFactory extends PackageFactory {
    Microcontroller createMicrocontroller() {
        return new RaspberryPi();
    }
    Display createDisplay() {
        return new OLED();
    }
}

class PremiumPackageFactory extends PackageFactory {
    Microcontroller createMicrocontroller() {
        return new RaspberryPi();
    }
    Display createDisplay() {
        return new TouchScreen();
    }
}

// Builder Pattern
class TicketingSystem {
    private Microcontroller microcontroller;
    private Display display;
    private String internetConnection;
    private String webFramework;

    public void setMicrocontroller(Microcontroller microcontroller) {
        this.microcontroller = microcontroller;
    }

    public void setDisplay(Display display) {
        this.display = display;
    }

    public void setInternetConnection(String internetConnection) {
        this.internetConnection = internetConnection;
    }

    public void setWebFramework(String webFramework) {
        this.webFramework = webFramework;
    }

    public void showDetails() {
        microcontroller.addMicrocontroller();
        display.addDisplay();
        System.out.println("Internet connection: " + internetConnection);
        System.out.println("Web framework: " + webFramework);
    }
}

class TicketingSystemBuilder {
    private TicketingSystem system;

    public TicketingSystemBuilder() {
        system = new TicketingSystem();
    }

    public void buildPackage(PackageFactory factory) {
        system.setMicrocontroller(factory.createMicrocontroller());
        system.setDisplay(factory.createDisplay());
    }

    public void setInternetConnection(String internetConnection) {
        system.setInternetConnection(internetConnection);
    }

    public void setWebFramework(String webFramework) {
        system.setWebFramework(webFramework);
    }

    public TicketingSystem getSystem() {
        return system;
    }
}

// Main class to demonstrate the implementation
public class task2Demo {
    public static void main(String[] args) {
        java.util.Scanner scanner = new java.util.Scanner(System.in);

        System.out.println("Choose a package: Basic, Standard, Advanced, Premium");
        String packageChoice = scanner.nextLine();

        System.out.println("Choose an internet connection: WiFi, Ethernet, SIM card");
        String internetChoice = scanner.nextLine();

        System.out.println("Choose a web framework: Django, NodeJS, Ruby");
        String frameworkChoice = scanner.nextLine();

        PackageFactory factory;
        switch (packageChoice.toLowerCase()) {
            case "basic":
                factory = new BasicPackageFactory();
                break;
            case "standard":
                factory = new StandardPackageFactory();
                break;
            case "advanced":
                factory = new AdvancedPackageFactory();
                break;
            case "premium":
                factory = new PremiumPackageFactory();
                break;
            default:
                throw new IllegalArgumentException("Invalid package choice");
        }

        TicketingSystemBuilder builder = new TicketingSystemBuilder();
        builder.buildPackage(factory);
        builder.setInternetConnection(internetChoice);
        builder.setWebFramework(frameworkChoice);

        TicketingSystem system = builder.getSystem();
        system.showDetails();
    }
}