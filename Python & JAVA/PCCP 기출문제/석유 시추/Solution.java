/*

Breadth First Search
- 각 Column마다 row를 지나가며 BFS를 진행하고
- 이 때 뽑을 수 있는 최댓값을 찾아냄.
- 이미 확인한 석유 개수는 found에 저장하고, checked 에서 false라면, 그 수를 미리 더함.
- found에서 확인한 값은 Column을 이동할 때까지 확인하지 않음

*/

import java.util.*;

class Solution {
    
    public int solution(int[][] land) {
        int answer = 0;
        
        int n = land.length;
        int m = land[0].length;
        
        ArrayList<Integer> found = new ArrayList<>();
        ArrayList<Boolean> checked = new ArrayList<>();
        
        int[] dx = {1, -1, 0, 0};
        int[] dy = {0, 0, 1, -1};
        
        int numFuel = 0;
        int fuelIndex = 0; // abs(fuelIndex)
        
        for(int col = 0; col < m; col++) {
            
            int max = 0;
            for(int i = 0; i < checked.size(); i++) {
                checked.set(i, false);
            }
            
            for(int row = 0; row < n; row++) {
                
                if(land[row][col] < 0) { // 석유 개수 추가 됐는지 확인 후, 추가 안 됐다면 추가
                    int index = Math.abs(land[row][col]) - 1;
                    int fuels = found.get(index);
                    
                    // 이미 check가 true이면 더하지 않음
                    if(!checked.get(index)) {
                        max += fuels;
                    }
                    
                    checked.set(index, true);
                    continue;
                }
                
                if(land[row][col] == 0) continue; // 석유 없는 땅
                
                Queue<point> queue = new LinkedList<>();
                queue.offer(new point(row, col));
                
                fuelIndex--;
                
                while(!queue.isEmpty()) {
                    
                    point current = queue.poll();
                    
                    if(land[current.x][current.y] < 0) continue;
                    
                    land[current.x][current.y] = fuelIndex;
                    numFuel++;
                    max++;
                    
                    for(int step = 0; step < 4; step++) {
                        int nX = current.x + dx[step];
                        int nY = current.y + dy[step];
                        
                        if(nX < 0 || nX >= n || nY < 0 || nY >= m) continue;
                        if(land[nX][nY] <= 0) continue;
                        
                        queue.offer(new point(nX, nY));
                    }
                    
                }
                
                found.add(numFuel);
                checked.add(true);
                numFuel = 0;
                
            }
            answer = Math.max(max, answer);
        }
        
        return answer;
    }
}

class point {
    int x;
    int y;
    
    point(int x, int y) {
        this.x = x;
        this.y = y;
    }
}