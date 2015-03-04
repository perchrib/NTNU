package barbershop;
import java.util.Random;

//import com.sun.org.apache.bcel.internal.classfile.Constant;

/**
 * This class implements the barber's part of the
 * Barbershop thread synchronization example.
 */
public class Barber extends Thread {
	/**
	 * Creates a new barber.
	 * @param queue		The customer queue.
	 * @param gui		The GUI.
	 * @param pos		The position of this barber's chair
	 */
	private Gui gui;
	private int barberID;
	private CustomerQueue custumerQueue;
	private boolean [] yesOrNO = new boolean[5];
	private boolean isSleeping, isReady;
	
	
	
	public Barber(CustomerQueue queue, Gui gui, int pos) { 
		this.custumerQueue = queue;
		this.gui = gui;
		this.barberID = pos;
		yesOrNO[0] = true;
		isReady = true;
		
		
		
		
	}
	public void run(){
		
		
		while(Globals.customerOfBarber > 0 ){
			Random rand = new Random();
			int sec = 4 - rand.nextInt(4);
			int r = rand.nextInt(5);
			isSleeping = yesOrNO[r];
			if (isReady && !isSleeping) {
				synchronized (this) {
					try {
						wait(700);
						Customer c = custumerQueue.removeCustomerFromSaloon();
						if(c == null)
							continue;
						else{
							gui.fillBarberChair(barberID, c);
							gui.println("Barber#" + barberID + " has customer#" + c.getCustomerID());
							wait(sec*Globals.barberWork/2);
							isReady = false;
							gui.emptyBarberChair(barberID);
							Globals.customerOfBarber--;
							gui.println("Customer left: " + Globals.customerOfBarber);
							
						}
					} catch (InterruptedException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
					isReady = true;
					notifyAll();
					
				}
				
			}
			else if(isReady && isSleeping){
				synchronized (this) {
					
					try {
						gui.barberIsSleeping(barberID);
						wait(sec*Globals.barberSleep/3);
						gui.barberIsAwake(barberID);
						isSleeping = false;
					} catch (InterruptedException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
					notifyAll();
					
				}
			}
			
			
			
		}
		gui.println("Barber#"+ barberID + " is finished for today");
	}

	/**
	 * Starts the barber running as a separate thread.
	 */
	
	

	// Add more methods as needed
}

