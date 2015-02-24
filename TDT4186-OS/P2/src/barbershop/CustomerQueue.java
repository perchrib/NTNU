package barbershop;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Random;

/**
 * This class implements a queue of customers as a circular buffer.
 */
public class CustomerQueue {
	/**
	 * Creates a new customer queue.
	 * 
	 * @param queueLength
	 *            The maximum length of the queue.
	 * @param gui
	 *            A reference to the GUI interface.
	 */
	private Queue<Customer> queue;
	private Gui gui;
	private int limit;
	private int seat;
	private ArrayList<Integer> seats;
	private Queue<Customer> appointments;
	private Queue<Integer> occupiedSeats;

	public CustomerQueue(int queueLength, Gui gui) {
		queue = new LinkedList<Customer>();
		appointments = new LinkedList<Customer>();
		limit = queueLength;
		this.gui = gui;
		occupiedSeats = new LinkedList<Integer>();
		seats = new ArrayList<Integer>();
		generateSeats();

	}

	private void generateSeats() {
		for (int i = 0; i < limit; i++) {

			seats.add(i);

		}
	}

	public synchronized Queue<Customer> getQueue() {
		return queue;
	}
	
	

	public synchronized Customer removeCustomerFromSaloon() {
		Customer c;
		if (!appointments.isEmpty()) {
			c = queue.poll();
			seat = occupiedSeats.poll();
			gui.emptyLoungeChair(seat);
			seats.add(seat);
			Customer c1 = appointments.poll();
			addCustomers(c1);

		} else {
			c = queue.poll();
			if (!occupiedSeats.isEmpty()) {
				seat = occupiedSeats.poll();
				gui.emptyLoungeChair(seat);
				seats.add(seat);

			}

		}
		return c;
	}

	private void addCustomers(Customer c) {
		if (queue.size() >= limit) {
			gui.println("The saloon is Full, Setting up Appointments");
			appointments.add(c);

		} else {
			Random rand = new Random();
			int r = rand.nextInt(seats.size());
			seat = seats.get(r);
			occupiedSeats.add(seat);
			seats.remove((Integer) seat);
			queue.add(c);
			gui.fillLoungeChair(seat, c);
		}

	}


	public synchronized void setCustomerInSaloon(Customer c) {
		addCustomers(c);

	}
	// Add more methods as needed

}
