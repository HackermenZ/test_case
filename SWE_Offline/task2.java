interface Microprocessor{
    void process();
}
interface Display{
    void showMessage(String message);
}
interface Cards{
    void cardMessage();
}
interface InternetConnection{
    void connection();
}
interface Storage{
    void store();
}
interface Controller{
    void control();
}
interface WebServer{
    void serve();
}
//Microprocessor
class ATMega32 implements Microprocessor{

    @Override
    public void process() {
        System.out.println("Processing On ATMega32");
    }
}

class ArduinoMega implements Microprocessor{

    @Override
    public void process() {
        System.out.println("Processing On ArduinoMega");
    }
}


class RaspberryPI implements Microprocessor{

    @Override
    public void process() {
        System.out.println("Processing On Raspberry PI");
    }
}


//Display
class LCDDisplay implements Display{
    @Override
    public void showMessage(String message) {
        System.out.println("LCD Display: " + message);
    }
}

class LEDDisplay implements Display{
    @Override
    public void showMessage(String message) {
        System.out.println("LED Display: " + message);
    }
}

class OLEDDisplay implements Display{
    @Override
    public void showMessage(String message) {
        System.out.println("OLED Display: " + message);
    }
}


class TouchDisplay implements Display{
    @Override
    public void showMessage(String message) {
        System.out.println("Touch Display: " + message);
    }
}

//cards
class RFID implements Cards{

    @Override
    public void cardMessage() {
        System.out.println("Using RFID cards for Identification");
    }
}

class NFC implements Cards{

    @Override
    public void cardMessage() {
        System.out.println("Using NFC cards for Identification");
    }
}

//Internet
class WiFiOrGSM implements InternetConnection{

    @Override
    public void connection() {
        System.out.println("Using WiFi or GSM for Internet");
    }
}

//Payment
class Payment{
    void collect(){
        System.out.println("Collect Money");
    }
    void change(){
        System.out.println("Give Change");
    }
}

class Ethernet implements InternetConnection{

    @Override
    public void connection() {
        System.out.println("Using Ethernet for Internet");
    }
}

//storage
class SDCard implements Storage{

    @Override
    public void store() {
        System.out.println("Using SD card");
    }
}

//controller
class ExternalController implements Controller{

    @Override
    public void control() {
        System.out.println("Using External Controller");
    }
}


//server
class Django implements WebServer{

    @Override
    public void serve() {
        System.out.println("Developed Using Django");
    }
}

class NodeJS implements WebServer{
    @Override
    public void serve() {
        System.out.println("Developed Using NodeJS");
    }
}

class Ruby implements WebServer{
    @Override
    public void serve() {
        System.out.println("Developed Using Ruby");
    }
}


abstract class ComponentFactory{
    abstract Microprocessor createMicroProcessor();
    abstract Display createDisplay();
    abstract Cards createCards();
    abstract InternetConnection createInternetConnection();
    abstract Storage createStorage();
    abstract Controller createController();
    abstract WebServer createWebServer();
    abstract Payment createPayment();
}

// Factory for Basic Package
class BasicPackageFactory extends ComponentFactory {
    @Override
    Microprocessor createMicroProcessor() {
        return new ATMega32(); // Basic uses ATMega32
    }

    @Override
    Display createDisplay() {
        return new LCDDisplay(); // Basic uses LCD Display
    }

    @Override
    Cards createCards() {
        return new RFID(); // Basic uses RFID cards
    }

    @Override
    InternetConnection createInternetConnection() {
        return new WiFiOrGSM(); // Basic uses WiFi or GSM
    }

    @Override
    Storage createStorage() {
        return new SDCard();
    }

    @Override
    Controller createController() {
        return new ExternalController();
    }

    @Override
    WebServer createWebServer() {
        return new Django(); // Basic uses Django
    }

    @Override
    Payment createPayment() {
        return new Payment(); // Default payment system for Basic
    }
}

// Factory for Standard Package
class StandardPackageFactory extends ComponentFactory {
    @Override
    Microprocessor createMicroProcessor() {
        return new ArduinoMega(); // Standard uses ArduinoMega
    }

    @Override
    Display createDisplay() {
        return new LEDDisplay(); // Standard uses LED Display
    }

    @Override
    Cards createCards() {
        return new RFID(); // Standard uses NFC cards
    }

    @Override
    InternetConnection createInternetConnection() {
        return new WiFiOrGSM(); // Standard uses Ethernet
    }

    @Override
    Storage createStorage() {
        return new SDCard();
    }

    @Override
    Controller createController() {
        return new ExternalController();
    }

    @Override
    WebServer createWebServer() {
        return new NodeJS(); // Standard uses NodeJS
    }

    @Override
    Payment createPayment() {
        return new Payment(); // Default payment system for Standard
    }
}



// Factory for Advanced Package
class AdvancedPackageFactory extends ComponentFactory {
    @Override
    Microprocessor createMicroProcessor() {
        return new RaspberryPI(); // Advanced uses ArduinoMega
    }

    @Override
    Display createDisplay() {
        return new OLEDDisplay(); // Advanced uses OLED Display
    }

    @Override
    Cards createCards() {
        return new NFC(); // Advanced uses NFC cards
    }

    @Override
    InternetConnection createInternetConnection() {
        return new Ethernet(); // Advanced uses Ethernet
    }

    @Override
    Storage createStorage() {
        return null; // Advanced uses SDCard for storage
    }

    @Override
    Controller createController() {
        return null; // Advanced uses external controller
    }

    @Override
    WebServer createWebServer() {
        return new Ruby(); // Advanced uses NodeJS
    }

    @Override
    Payment createPayment() {
        return new Payment(); // Default payment system for Advanced
    }
}


// Factory for Premium Package
class PremiumPackageFactory extends ComponentFactory {
    @Override
    Microprocessor createMicroProcessor() {
        return new RaspberryPI(); // Premium uses Raspberry Pi
    }

    @Override
    Display createDisplay() {
        return new TouchDisplay(); // Premium uses Touch Display
    }

    @Override
    Cards createCards() {
        return new NFC(); // Premium uses NFC cards
    }

    @Override
    InternetConnection createInternetConnection() {
        return new Ethernet(); // Premium uses WiFi or GSM
    }

    @Override
    WebServer createWebServer() {
        return new NodeJS(); // Premium uses NodeJS
    }

    @Override
    public Storage createStorage() {
        return null; // Premium has internal storage
    }

    @Override
    public Controller createController() {
        return null; // No external controller needed for Premium (touch display)
    }

    @Override
    Payment createPayment() {
        return new Payment(); // Default payment system for Premium
    }
}



// TicketingSystem class that uses all components
class TicketingSystem {
    private Microprocessor microprocessor;
    private Display display;
    private Cards cards;
    private InternetConnection internetConnection;
    private Storage storage;
    private Controller controller;
    private WebServer webServer;

    // Constructor
    public TicketingSystem(Microprocessor microprocessor, Display display, Cards cards, InternetConnection internetConnection, Storage storage, Controller controller, WebServer webServer) {
        this.microprocessor = microprocessor;
        this.display = display;
        this.cards = cards;
        this.internetConnection = internetConnection;
        this.storage = storage;
        this.controller = controller;
        this.webServer = webServer;
    }

    // Operate method to simulate the system working
    public void operate() {
        microprocessor.process();
        display.showMessage("Welcome to the Ticketing System");
        cards.cardMessage();
        internetConnection.connection();

        if (storage != null) {
            storage.store();
        } else {
            System.out.println("Using built-in storage.");
        }

        if (controller != null && !(display instanceof TouchDisplay)) {
            controller.control();
        } else {
            System.out.println("No external controller required.");
        }

        webServer.serve();
    }
}

// Builder pattern for assembling a ticketing system with various components
class TicketingSystemBuilder {
    private Microprocessor microprocessor;
    private Display display;
    private Cards cards;
    private InternetConnection internetConnection;
    private Storage storage;
    private Controller controller;
    private WebServer webServer;

    // Setters for each component
    public TicketingSystemBuilder setMicroprocessor(Microprocessor microprocessor) {
        this.microprocessor = microprocessor;
        return this;
    }

    public TicketingSystemBuilder setDisplay(Display display) {
        this.display = display;
        return this;
    }

    public TicketingSystemBuilder setCards(Cards cards) {
        this.cards = cards;
        return this;
    }

    public TicketingSystemBuilder setInternetConnection(InternetConnection internetConnection) {
        this.internetConnection = internetConnection;
        return this;
    }

    public TicketingSystemBuilder setStorage(Storage storage) {
        this.storage = storage;
        return this;
    }

    public TicketingSystemBuilder setController(Controller controller) {
        this.controller = controller;
        return this;
    }

    public TicketingSystemBuilder setWebServer(WebServer webServer) {
        this.webServer = webServer;
        return this;
    }

    // Method to build the final TicketingSystem
    public TicketingSystem build() {
        return new TicketingSystem(microprocessor, display, cards, internetConnection, storage, controller, webServer);
    }
}

public class task2 {
    public static void main(String[] args) {
        // Example for Basic Package
        ComponentFactory basicFactory = new BasicPackageFactory();
        TicketingSystem basicSystem = new TicketingSystemBuilder()
                .setMicroprocessor(basicFactory.createMicroProcessor())
                .setDisplay(basicFactory.createDisplay())
                .setCards(basicFactory.createCards())
                .setInternetConnection(basicFactory.createInternetConnection())
                .setStorage(basicFactory.createStorage())
                .setController(basicFactory.createController())
                .setWebServer(basicFactory.createWebServer())
                .build();
        System.out.println("Basic Package:");
        basicSystem.operate();
        System.out.println();

        // Example for Standard Package
        ComponentFactory standardFactory = new StandardPackageFactory();
        TicketingSystem standardSystem = new TicketingSystemBuilder()
                .setMicroprocessor(standardFactory.createMicroProcessor())
                .setDisplay(standardFactory.createDisplay())
                .setCards(standardFactory.createCards())
                .setInternetConnection(standardFactory.createInternetConnection())
                .setStorage(standardFactory.createStorage())
                .setController(standardFactory.createController())
                .setWebServer(standardFactory.createWebServer())
                .build();
        System.out.println("Standard Package:");
        standardSystem.operate();
        System.out.println();

        //Example for Advanced Packages
        ComponentFactory AdvancdFactory = new AdvancedPackageFactory();
        TicketingSystem advancedSystem = new TicketingSystemBuilder()
                .setMicroprocessor(AdvancdFactory.createMicroProcessor())
                .setDisplay(AdvancdFactory.createDisplay())
                .setCards(AdvancdFactory.createCards())
                .setInternetConnection(AdvancdFactory.createInternetConnection())
                .setStorage(AdvancdFactory.createStorage())
                .setController(AdvancdFactory.createController())
                .setWebServer(AdvancdFactory.createWebServer())
                .build();
        System.out.println("Advanced Package:");
        standardSystem.operate();
        System.out.println();


        // Example for Premium Package
        ComponentFactory premiumFactory = new PremiumPackageFactory();
        TicketingSystem premiumSystem = new TicketingSystemBuilder()
                .setMicroprocessor(premiumFactory.createMicroProcessor())
                .setDisplay(premiumFactory.createDisplay())
                .setCards(premiumFactory.createCards())
                .setInternetConnection(premiumFactory.createInternetConnection())
                .setStorage(premiumFactory.createStorage())
                .setController(premiumFactory.createController())
                .setWebServer(premiumFactory.createWebServer())
                .build();
        System.out.println("Premium Package:");
        premiumSystem.operate();
    }
}
