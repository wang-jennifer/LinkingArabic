import java.util.*;
import java.io.*;

public class ShellScript {
	public static void main(String[] args) throws FileNotFoundException {
		File arabicFile = new File("Diary_50_Arabic_EditsStandardized_20150917 (1).html");
		Scanner arabicScanner = new Scanner(arabicFile);
		File diaryFile = new File("Diary_50_20160719_links.html");
		Scanner diaryScanner = new Scanner(diaryFile);

		findIdCell(diaryScanner);
	}
	// scan through file to find ID-cell
	// copies ID (looks like [A50_...])
	// forms new string that looks like:
	// <a href= "Diary_50_Arabic_EditsStandardized_20150917 (1).html#A50_009_09:001">Link to arabic</a>
	public static void findIdCell(Scanner input) {
		while (input.hasNextLine()) {
			String line = input.nextLine();
            String result = "<a href= \"Diary_50_Arabic_EditsStandardized_20150917 (1).html#";
			if line.contains("[A50_")) {
                String id = line.substring(line.indexOf("[") + 1, line.indexOf("]")); // from [A50_...] to A50_...
                result += id + "\">Link to arabic</a>"; // change link name?
			}
		}
	}
	// method to replace (Scanner file, String replaceWith)
	// find and replace
	// insert before the string <a id = "string"> </a>
	// keep a list of all the ids that we created
	public static void replace(Scanner input, String replaceWith) {

	}
}
