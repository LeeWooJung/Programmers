import java.util.*;

class Solution {
    
    static int base_year, base_month, base_day;
    
    public int[] solution(String today, String[] terms, String[] privacies) {

        ArrayList<Integer> ans = new ArrayList<>();
        
        String[] ymd = today.split("\\.");
        
        int year = Integer.parseInt(ymd[0]);
        int month = Integer.parseInt(ymd[1]);
        int day = Integer.parseInt(ymd[2]);
        
        //ABCDEFGHIJKLMNOPQRSTUVWXYZ
        int[] periods = new int[26];
        
        for(String t : terms) {
            String[] temp = t.split(" ");
            
            char alpha = temp[0].charAt(0);
            int period = Integer.parseInt(temp[1]);
            
            periods[alpha - 'A'] = period;
        }
        
        for(int index = 0; index < privacies.length; index++) {
            String privacy = privacies[index];
            
            String[] info = privacy.split(" ");
            String[] ymd2 = info[0].split("\\.");
            
            int cur_year = Integer.parseInt(ymd2[0]);
            int cur_month = Integer.parseInt(ymd2[1]);
            int cur_day = Integer.parseInt(ymd2[2]);
            
            int period = periods[info[1].charAt(0) - 'A'];
            
            getLast(cur_year, cur_month, cur_day - 1, period);
            
            if(year > base_year || year == base_year && month > base_month || year == base_year && month == base_month && day > base_day) {
                ans.add(index+1);
            } 
        }


        int[] answer = new int[ans.size()];
        for(int index = 0; index < ans.size(); index++) {
            answer[index] = ans.get(index);
        }
        
        return answer;
    }
    
    static void getLast(int year, int month, int day, int period) {
        
        if(day == 0) {
            month -= 1;
            day = 28;
        }
        
        if(month == 0) {
            year -= 1;
            month = 12;
        }
        
        month += period;
        
        while(month > 12) {
            year += 1;
            month -= 12;
        }
        
        base_year = year;
        base_month = month;
        base_day = day;
        
        
        StringBuilder sb = new StringBuilder();
        sb.append("Period : ").append(period).append(" ").append(year).append(".").append(month).append(".").append(day).append("\n");
        System.out.print(sb.toString());
        
    }
}









