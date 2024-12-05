import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.PriorityQueue;

public class Day1 {
    public static void main(String[] args) {
        PriorityQueue<Integer> list1 = new PriorityQueue<>();
        PriorityQueue<Integer> list2 = new PriorityQueue<>();
        HashMap<Integer, Integer> hashMap = new HashMap<>();
        ArrayList<Integer> list3 = new ArrayList<>();
        ArrayList<Integer> list4 = new ArrayList<>();
        int totalDistance = 0;
        try{
            BufferedReader br = new BufferedReader(new FileReader("Day_1_input.txt"));
            String line="";
            while((line=br.readLine())!= null) // if line not null store as String
            {
                String[] arr = line.trim().split(" ");
                list1.add(Integer.parseInt(arr[0].trim()));
                list2.add(Integer.parseInt(arr[arr.length - 1]));

                list3.add(Integer.parseInt(arr[0].trim()));
                list4.add(Integer.parseInt(arr[arr.length - 1]));

            }
        }
        catch (IOException io){
            System.err.println("File Error: "+io);
        }
        int size = list1.size();
        for(int i = 0; i < size; i++) {
//            System.out.println(list1.peek() + " " + list2.peek() + " = " + Math.abs(list1.poll() - list2.poll()));
            totalDistance += Math.abs(list1.poll() - list2.poll());
        }

        System.out.println("totalDistance: " + totalDistance); // for first one


        // part 2
        int sum = 0;
        for(int i : list3){
            int count = 0;
            for(int j : list4)
                if(i == j)
                    count++;
            sum += (i * count);
        }

        System.out.println("Similarity Score: " + sum); // for second one
    }
}