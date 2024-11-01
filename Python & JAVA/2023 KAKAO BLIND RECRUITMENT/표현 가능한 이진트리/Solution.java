/*

1. h = 1 : 2^h - 1 = 1 노드 1개. 0~1까지 표현
2. h = 2 : 2^h - 1 = 3 노드 3개. 111 ~ 010 2 ~ 7까지 표현 (이 중 표현 못하는 것이 있음.)
                                --> 루트 노드가 0이 되면 안 되고, 서브 트리의 루트 노드가 0이면 다음 것도 0이어야함.
3. h = 3 : 2^h - 1 = 7 노드 7개. 1111111 ~ 0001000 : 255 ~ 8까지 표현
                                --> 루트 노드가 0이 되면 안 되고, 서브 트리의 루트 노드가 0이면 다음 것도 0이어야함.
수가 주어졌을 때
ex)
1. 5 : 101
2. 7 : 111
3. 42 : 101010 ==> (0(1)0)1(0(1)0)
--> 0 ~ 7 mid : 3
--> 0 ~ 3, 4 ~ 7
--> 0 ~ 1, 2 ~ 3, 4 ~ 5, 6 ~ 7
--> 0~0, 1~1, 2~2, 3~3, 4~4, 5~5, 6~6, 7~7

            1
    1               1
0       0       0       0

풀이 과정

1. 주어진 수를 표현할 수 있는 height를 확인
- h를 1씩 증가시키면서 2^h -1 개의 이진수 (11....11) 즉 2^(2^h -1) - 1 보다 작거나 같은지 확인.
- 그 때 h가 height

2. 2^h -1 개로 길이를 늘려줘야 하므로, 모자란 것만큼 앞에 0을 채워줌.

3. start = 0, end = 2^h-1 , end는 길이의 끝이라 확인하지 않음
  --> index = (start + end) / 2 가 root node.
  --> (start, index) : left sub tree, (index+1, end) : right sub tree
  
4. sub tree로 이동하면서 이전의 root node 중에 0이 있었는데, 현재 root node가 1이면 불가능.
4-1. 문제 없다면 만들 수 있다는 것을 뜻함.

*/

class Solution {
    public int[] solution(long[] numbers) {
        int[] answer = new int[numbers.length];
    
        for(int index = 0; index < numbers.length; index++) {
            
            long number = numbers[index];
            StringBuilder sb = new StringBuilder();
            
            String tempbinary = getBinary(number);

            int length = getLength(number);
            int diff = length - tempbinary.length();
            
            while(diff-- > 0) {
                sb.append("0");
            }
            
            String binary = sb.toString() + tempbinary;
            
            if(canRepresent(binary)) answer[index] = 1;
            else answer[index] = 0;
        }
        
        return answer;
    }
    
    static boolean dfs(String binary, int start, int end, int root) {
        
        if(start == end) return true;

        int mid = (start + end) / 2;
        if(mid == binary.length()) return true;
        
        int subRoot = binary.charAt(mid) - '0';
        if(root == 0 && subRoot == 1) return false;
        
        
        boolean left = dfs(binary, start, mid, root * subRoot);
        boolean right = dfs(binary, mid+1, end, root * subRoot);
        
        return left && right;
    }
    
    static boolean canRepresent(String binary) {
        
        int start = 0;
        int end = binary.length();
        
        int mid = (start + end) / 2;
        int root = binary.charAt(mid) - '0';
        
        return dfs(binary, start, end, root);
    }
    
    static int getLength(long number) {
        long h = 1;
        
        while(true) {
            long value = (long)Math.pow(2, (long)Math.pow(2, h) - 1) - 1;
            if(number <= value) break;
            h += 1;
        }
        
        return (int)Math.pow(2, h) - 1;
    }
    
    static String getBinary(long number) {
        String result = "";
        while(number > 0) {
            int temp = (int)(number % 2);
            number /= 2;
            result = temp + result;
        }
        return result;
    }
}