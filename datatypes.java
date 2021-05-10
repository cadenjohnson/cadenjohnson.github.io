import examples;

// This is a single line comment

/* This is a 
 * multi-line comment
 */

public class datatypes {
	public static void main(String[] args) {
		// Print statement
		System.out.println("This is Caden's first test\n");
		
		// String Example
		String testword = "Normal Sentence";
		System.out.println(testword);
		System.out.println(testword.toUpperCase());
		System.out.println(testword.toLowerCase());
		System.out.println("location of \'S\' = " + testword.indexOf("S"));
		System.out.println(testword.concat(" added string") + "\n");
		
		
		// Different variable types
		String word = "test";
		int integer = 10;
		char letter = 'A';
		boolean bool = true;
		float buoy = 3.141596f;
		// double buoy = 3.141596
		// float buoy = (float) 3.141596
		final int permanent = 75;
		System.out.println("String = " + word);
		System.out.println("int = " + integer);
		System.out.println("char = " + letter);
		System.out.println("boolean = " + bool);
		System.out.println("float = " + buoy);
		System.out.println("final int = " + permanent + "\n");
		
		// Data Types
		System.out.println("Primative Data Types:");
		System.out.println("byte = numbers between -128 to 127");
		System.out.println("short = numbers between -32,768 to 32,767");
		System.out.println("int, long, double = 15 decimals");
		System.out.println("float = 6-7 decimals, boolean, char\n");
		
		System.out.println("Non-Primative Data Types:");
		System.out.println("String, Arrays, Classes\n");
		
		System.out.println("Sizes (small to large)");
		System.out.println("byte - short - char - int - long - float - double\n");
		
		// Access other class
		datatypes myClass = new datatypes();
		myClass.examples();
	}
	

	void examples() {
		// Creating Array
		int[] myarray = {1,2,3,4,5,6,7,8,9,10};
		System.out.println(myarray);

		// For Loop
		for(int i=0; i<10; i++) {
			System.out.println(myarray[i]);
		}		
	}
	
}