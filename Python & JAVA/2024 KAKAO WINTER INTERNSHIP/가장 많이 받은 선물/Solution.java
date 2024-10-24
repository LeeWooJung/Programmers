import java.util.*;

class Solution {
    public int solution(String[] friends, String[] gifts) {
        int answer = 0;
        int nPeople = friends.length;
        int[] giftIndex = new int[nPeople];
        
        HashMap<String, Integer> personToIndex = new HashMap<>();
        
        for(int idx = 0; idx < nPeople; idx++) {
            personToIndex.put(friends[idx], idx);
        }
        
        int[][] giveReceive = new int[nPeople][nPeople];
        
        StringTokenizer st;
        
        for(String give: gifts) {
            st = new StringTokenizer(give);
            String name1 = st.nextToken();
            String name2 = st.nextToken();
            
            giveReceive[personToIndex.get(name1)][personToIndex.get(name2)]++;
            giftIndex[personToIndex.get(name1)]++;
            giftIndex[personToIndex.get(name2)]--;
        }
        
        for(int p1 = 0; p1 < nPeople; p1++) {
            int willReceive = 0;
            for(int p2 = 0; p2 < nPeople; p2++) {
                if(p1 == p2) continue;
                
                int p1p2 = giveReceive[p1][p2];
                int p2p1 = giveReceive[p2][p1];
                
                if(p1p2 > p2p1) willReceive++;
                if(p1p2 == p2p1) {
                    if(giftIndex[p1] > giftIndex[p2]) willReceive++;
                }
            }
            
            answer = Math.max(willReceive, answer);
        }
        
        
        return answer;
    }
}