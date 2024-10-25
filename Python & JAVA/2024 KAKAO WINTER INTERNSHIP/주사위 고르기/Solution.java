/*

- Brute Force

1. n/2 개의 주사위 선택 : nC(n/2) : n! / (n/2)!
2. A가 선택한 주사위에서 나올 경우의 수 : 6^(n/2)
3. B가 선택한 주사위에서 나올 경우의 수 : 6^(n/2)
4. A와 B의 주사위 결과 비교 : 2 * 3 ==> 6^n ==> O(6^10)

- SegmentTree : 구간합 (X)
- Imos : 누적합 (X)
- DP : 단계별로 memoization (X)

* Backtracking + Binary Search

0) A가 선택할 것 : Backtracking

1) A : n/2개 선택해서 모든 주사위의 모든 조합 구하기 & Sort
2) B : n/2개 선택해서 모든 주사위의 모든 조합 구하기 & Sort
3) A의 원소를 하나씩 선택
    ==> binary search로 A의 원소가 작은 부분의 index 찾기 : index개만큼 A가 더 큼

*/

import java.util.*;

class Solution {
    
    static boolean[] select;
    static int n;
    static int max = -1;
    static ArrayList<Integer> result = new ArrayList<>();
    static ArrayList<Integer> aList = new ArrayList<>();
    static ArrayList<Integer> bList = new ArrayList<>();
    
    public int[] solution(int[][] dice) {
        int[] answer;
        
        n = dice.length;
        select = new boolean[n];
        
        backtracking(0, 0, dice); // 0) backtracking
        
        Collections.sort(result);
        answer = new int[result.size()];
        for(int i = 0; i < result.size(); i++) {
            answer[i] = result.get(i);
        }
        
        return answer;
    }
    
    static void backtracking(int index, int count, int[][] dice) {
        if(count == n/2) { // 0) A가 선택할 것 choice 완료
            // solve
            getResult(dice);
            return;
        }
        
        for(int t = index ; t < n; t++) {
            if(select[t]) continue;
            
            select[t] = true;
            backtracking(t + 1, count+1, dice);
            select[t] = false;
        }
    }
    
    static void getResult(int[][] dice) {
        ArrayList<Integer> As = new ArrayList<Integer>();
        ArrayList<Integer> Bs = new ArrayList<Integer>();
        
        for(int t = 0; t < n; t++) {
            if(select[t]) As.add(t);
            else Bs.add(t);
        }
        
        getSums(As, 0, 0, dice, true); // 1)
        getSums(Bs, 0, 0, dice, false); // 2)
        
        Collections.sort(aList); // 1)
        Collections.sort(bList); // 2)
        
        int cnt = 0;
        
        for(int aSum : aList) { // 3)
            int left = 0, right = bList.size() - 1;
            
            while(left <= right) {
                int mid = (left + right) / 2;
                if(aSum > bList.get(mid)) {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            }
            
            cnt += right;
        }
        
        if(cnt > max) { // 승리 횟수가 갱신 될 때마다 결과 수정
            max = cnt;
            result = new ArrayList<Integer>();
            for(int t = 0; t < n; t++) {
                if(select[t]) result.add(t+1);
            }
        }
        
        
        aList = new ArrayList<>();
        bList = new ArrayList<>();
    }
    
    // A에 의해 선택된 주사위에서 하나씩 선택해 각각의 합을 구하여 list에 저장
    static void getSums(ArrayList<Integer> selected, int sum, int index, int[][] dice, boolean a) {
        if(index >= n/2 && a) {
            aList.add(sum);
            return;
        } else if(index >= n/2 && !a) {
            bList.add(sum);
            return;
        }
        
        for(int t = 0; t < 6; t++) {
            getSums(selected, sum + dice[selected.get(index)][t], index+1, dice, a);
        }
    }
}