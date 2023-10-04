import java.util.Scanner;

public class Solution {

    
    
    static boolean isAnagram(String a, String b) {
        char[] A = new char[a.length()];
        char[] B = new char[b.length()];
 
        for (int i = 0; i < a.length(); i++) {
            A[i] = a.charAt(i);
        }
        
        for (int i = 0; i < b.length(); i++) {
            B[i] = b.charAt(i);
        }
        
        char temp1;
 
        for (int i = 0; i < a.length(); i++) {
            for (int j = 0; j < a.length(); j++) {
                if (A[j] < A[i]) {
                    temp1 = A[i];
                    A[i] = A[j];
                    A[j] = temp1;
                }
            }
        }
        
        char temp2;
 
        for (int i = 0; i < b.length(); i++) {
            for (int j = 0; j < b.length(); j++) {
                if (B[j] < B[i]) {
                    temp2 = B[i];
                    B[i] = B[j];
                    B[j] = temp2;
                }
            }
        }
        
        String a1 = String.valueOf(A);
        String a2 = a1.toLowerCase();
        String b1 = String.valueOf(B);
        String b2 = b1.toLowerCase();
        
        if (a2.compareTo(b2) == 0) {
            return true;
        }
        
        return false;
        
    }


    public static void main(String[] args) {
    
        Scanner scan = new Scanner(System.in);
        String a = scan.next();
        String b = scan.next();
        scan.close();
        boolean ret = isAnagram(a, b);
        System.out.println( (ret) ? "Anagrams" : "Not Anagrams" );
    }
}
