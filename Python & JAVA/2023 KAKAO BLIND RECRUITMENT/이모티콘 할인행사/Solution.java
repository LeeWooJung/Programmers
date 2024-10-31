import java.util.*;

class Solution {
    
    static ArrayList<eachDiscount> discountComb = new ArrayList<>();
    static ArrayList<int[]> results = new ArrayList<>();
    
    public int[] solution(int[][] users, int[] emoticons) {
        
        int[] answer = new int[2];
        int[] discounts = {10, 20, 30, 40};
        
        
        //results.add(new int[]{1 ,2}); people, cost
        
        // emoticon 별로 할인율 적용한 조합을 만들어야함 : O(4^7)
        backtracking(0, discounts, emoticons, users);
        
        Collections.sort(results, (a, b) -> {
            if(a[0] == b[0]) {
                return b[1] - a[1];
            } else {
                return b[0] - a[0];
            }
        });
        
        answer = results.get(0);
        
        return answer;
    }
    
    static void res(int[][] users) {
        
        int n = users.length;
        
        int nPeople = 0;
        int totCost = 0;
        
        
        for(int index = 0; index < n; index++) {
            int base_discount = users[index][0];
            int base_cost = users[index][1];
            
            int buyCost = 0;
            
            for(eachDiscount comb: discountComb) {
                if(comb.discount >= base_discount) {
                    // 구매
                    buyCost += (int)(comb.cost * (double)(100 - comb.discount)/100);
                }
                if(buyCost >= base_cost) {
                    buyCost = 0;
                    nPeople++;
                    break;
                }
            }
            
            totCost += buyCost;
        }
        
        results.add(new int[]{nPeople, totCost});
    }
    
    static void backtracking(int eindex, int[] discounts, int[] emoticons, int[][] users) {
        
        if(discountComb.size() == emoticons.length) {
            res(users);
            return;
        }
        
        for(int i = 0; i < discounts.length; i++) {
            for(int j = eindex; j < emoticons.length; j++) {
                discountComb.add(new eachDiscount(discounts[i], emoticons[j]));
                backtracking(j+1, discounts, emoticons, users);
                discountComb.remove(discountComb.size() - 1);
            }
        }
    }
}

class eachDiscount {
    int discount;
    int cost;
    
    eachDiscount(int discount, int cost) {
        this.discount = discount;
        this.cost = cost;
    }
}