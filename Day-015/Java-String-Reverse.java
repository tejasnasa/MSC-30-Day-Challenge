import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        String A = sc.next();
        String R = "";
        
        for (int i = A.length() - 1; i >= 0; i--) {
            R = R + A.charAt(i);
        }
            
        if (A.compareTo(R) == 0) {
            System.out.println("Yes");
        }
        else {
            System.out.println("No");
        }
        
        sc.close()
    
        
    }
}
