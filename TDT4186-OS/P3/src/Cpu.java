
public class Cpu implements Constants {
	
	private Queue queue;
	private Gui gui;
	private EventQueue events;
	private long maxCpuTime,timeLeft;
	private Process p, currentProcess;
	private Statistics statistics;
	
	
	
	
	public Cpu(Queue queue, Gui gui, EventQueue events,long maxCpuTime, Statistics statistics){
		this.queue = queue;
		this.gui = gui;
		this.events = events;
		this.maxCpuTime = maxCpuTime;
		this.statistics = statistics;
		
		
		
		
	}
	
	public void addCpuQueue(Process p, long clock){
		
		queue.insert(p);
		if (currentProcess == null && queue.getQueueLength() == 1) {
			events.insertEvent(new Event(SWITCH_PROCESS, clock));
		}
	}
	

	

	
	public void roundRobin(long clock){
		if (currentProcess != null) {
			
			long timeNeeded = currentProcess.getCpuNeeded();
			long nextIO = currentProcess.getCPUTimeToNextIO();
			if (timeNeeded > maxCpuTime) {
				currentProcess.giveCpuTime(maxCpuTime);
				events.insertEvent(new Event(SWITCH_PROCESS, clock + maxCpuTime));
				statistics.cpuTimeSpent += maxCpuTime;
				statistics.processShifts++;
			} else if (timeNeeded > nextIO && nextIO <= maxCpuTime) { // we must check if process need IO before it is finsihed
				System.out.println("JAJAJAJAJJAAJAJ1");
			
				currentProcess.giveCpuTime(nextIO);
				events.insertEvent(new Event(IO_REQUEST, clock + nextIO));
				events.insertEvent(new Event(SWITCH_PROCESS, clock + nextIO + 1));
				statistics.cpuTimeSpent += nextIO;
			} else if (timeNeeded <= maxCpuTime) {
				currentProcess.giveCpuTime(timeNeeded);
				System.out.println("NEEEEEEEEEEEEEEEEEEEEEi");
				events.insertEvent(new Event(END_PROCESS, clock + timeNeeded));
				events.insertEvent(new Event(SWITCH_PROCESS, clock + timeNeeded + 1));
				statistics.cpuTimeSpent += timeNeeded;
			} else {
				System.out.println("Test");
			}
		}
		
		
		
		
		
		
	}
	public void switchProcess() {
		if (queue.getQueueLength() > 0) {
			if (currentProcess != null) {
				queue.insert(currentProcess);
			}
			currentProcess = (Process) queue.removeNext();
			gui.setCpuActive(currentProcess);
		}
	}
	public Process fetchCurrentProcess() {
		Process fetched = currentProcess;
		currentProcess = null;
		gui.setCpuActive(null);
		return fetched;
	}
	
	public void insertProcess(Process p, long clock) {
		queue.insert(p);
		p.addedToReadyQueue();
		statistics.insertsCPUQueue++;
		if (currentProcess == null && queue.getQueueLength() == 1) {
			events.insertEvent(new Event(Simulator.SWITCH_PROCESS, clock));
		}
	}
	

	
	
	
	
	

}
