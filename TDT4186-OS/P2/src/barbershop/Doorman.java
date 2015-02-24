package barbershop;
import java.util.Random;

/**
 * This class implements the doorman's part of the
 * Barbershop thread synchronization example.
 */
public class Doorman extends Thread {
	/**
	 * Creates a new doorman.
	 * @param queue		The customer queue.
	 * @param gui		A reference to the GUI interface.
	 */
	private Gui gui;
	private CustomerQueue customerQueue;
	private int customerOfToday;
	
	
	public Doorman(CustomerQueue queue, Gui gui) { 
		this.gui = gui;
		customerQueue = queue;
		customerOfToday = Globals.customerOfBarber;
	}

	/**
	 * Starts the doorman running as a separate thread.
	 */
	public void run(){
		Random r = new Random();
		int sec = 4 - r.nextInt(4);
		while(customerOfToday > 0){
			synchronized (this) {
				try {
					wait(sec*Globals.doormanSleep/4);
					Customer c = new Customer();
					customerQueue.setCustomerInSaloon(c);
					customerOfToday--;
					
					
				} catch (InterruptedException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}notifyAll();
				
				
				
			}
		}
		
		
		
		
		
		
		
		
	}

	// Add more methods as needed
}
