package questions;
import java.util.Scanner;


public class CivilEngineer {

	int[] inputs;
	String[] mixDesignTypes[];
	String[] structElement[];

	CivilEngineer(){
		mixDesignTypes[0] = {"M5", "1", "5", "10"};
		mixDesignTypes[1] = {"M7.5", "1", "4", "8"};
		mixDesignTypes[2] = {"M10", "1", "3", "6"};
		mixDesignTypes[3] = {"M15", "1", "2", "4"};
		mixDesignTypes[4] = {"M20", "1", "1.5", "3"};
		mixDesignTypes[5] = {"M25", "1", "1", "2"};
		mixDesignTypes[6] = {"M30", "1", "1", "1.5"};

		structElement[0] = {"screed", "M10:3", "M7.5:2", "M5:1"};
		structElement[1] = {"beam", "M20:3", "M15:2", "M10:1"};
		structElement[2] = {"slab", "M25:3", "M20:2", "M15:1"};
		structElement[3] = {"column", "M30:3", "M25:2", "M20:1"};
	}

	public void getInputs() {
		Scanner userIn = new Scanner(System.in);
		String stringInputs = userIn.readLine();
		inputs = stringInputs.split(" ");
	}

	



	public static void main(String[] args) {
		

	}

}
