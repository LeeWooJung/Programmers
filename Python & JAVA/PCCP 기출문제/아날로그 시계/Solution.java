class Solution {
    public int solution(int h1, int m1, int s1, int h2, int m2, int s2) {
        
        int answer = 0;
        
        
        int start = h1 * 3600 + m1 * 60 + s1;
        int end = h2 * 3600 + m2 * 60 + s2;
        
        answer = numAlarm(end) - numAlarm(start);
        answer += curAlarm(start) ? 1 : 0;
        
           
        return answer;
    }
    
    static int numAlarm(int time) {
        
        int ms = time * 59 / 3600;
        int hs = time * 719 / 43200;
        int oClock12 = 43200 <= time ? 2 : 1;
        
        return ms + hs - oClock12;
        
    }
    
    static boolean curAlarm(int time) {
        return time * 59 % 3600 == 0 || time * 719 % 43200 == 0;
    }
}