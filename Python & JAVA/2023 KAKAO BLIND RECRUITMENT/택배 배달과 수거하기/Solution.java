class Solution {
    public long solution(int cap, int n, int[] deliveries, int[] pickups) {
        long answer = 0;
        
        int dAmount = 0;
        int pAmount = 0;
        
        for(int d = n-1; d >= 0; d--) {
            
            dAmount += deliveries[d];
            pAmount += pickups[d];
        
            int dtimes = dAmount <= 0 ? 0 : (dAmount % cap != 0 ? dAmount/cap + 1 : dAmount / cap);
            int ptimes = pAmount <= 0 ? 0 : (pAmount % cap != 0 ? pAmount/cap + 1 : pAmount / cap);
            
            int times = Math.max(dtimes, ptimes);
            
            answer += (d+1) * 2 * times;
            
            dAmount -= cap * times;
            pAmount -= cap * times;
        }
        
        if(dAmount > 0 || pAmount > 0) answer += 2;
        
        
        return answer;
    }
}