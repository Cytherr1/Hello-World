package arrays;

import java.util.Random;
import java.util.Scanner;

public class RandomPassword {

	public static void main(String[] args) {
		
		//numbers [0,1,2,3,4,5,6,7,8,9]
		//letters A-Z a-z
		//symbols + % & - #
		
		
		Scanner sc = new Scanner(System.in);
		
		System.out.println("Lenght: ");
		int lenght = sc.nextInt();
		System.out.println(generatePassword(lenght));
		sc.close();
	}
	
	public static String generatePassword(int lenght) {
		
		char[] symbols = {'+', '-', '%', '&', '#'};
		char[] lower = new char[26];
		char[] upper = new char[26];
		
		for (int i = 0; i < lower.length; i++) {
			lower[i] = (char)('a' + i);
			upper[i] = (char)('A' + i);
		}
		
		Random r = new Random();
		String generatedPassword = "";
		
		for (int i = 0; i < lenght; i++) {
			
			
			int key = r.nextInt(3)+1;
			
			switch (key) {
			case 1:
				//symbol
				int rndm = r.nextInt(5);
				generatedPassword += symbols[rndm];
				
				break;
			case 2:
				//lower
				int rndm1 = r.nextInt(26);
				generatedPassword += lower[rndm1];
				
				
				break;
			case 3:
				//upper
				int rndm2 = r.nextInt(26);
				generatedPassword += upper[rndm2];
				
				break;
			case 4:
				//number
				Integer rndm3 = r.nextInt(10);
				generatedPassword += rndm3;
				
				break;
			default:
				break;
			}
		
		}
		return generatedPassword;
	}
}
