/*

1. 막대 그래프
- 출발 노드 ~ 도착 노드로 움직이고. 거기서 끝남.
==> 마지막 노드는 나가는 간선의 개수가 0개.
==> 임의의 노드에 의해 선택 되더라도 이 값은 변하지 않음.

2. 8자모양 그래프
- 출발 노드 ~ 도착 노드로 움직이고. 간선을 따라 이동하면 <출발 노드>로 돌아옴.
==> 임의의 노드에 의해 선택되더라도 나가는 간선 2개 이상, 들어오는 간선은 2개 이상 존재.

3. 임의의 노드
==> 그래프의 개수만큼 나가는 간선이 존재.
==> 들어오는 간선이 없음.
==> 그래프의 개수가 최소 2개 이상이므로, 나가는 간선의 개수는 2이상.

4. 도넛 그래프
==> 임의의 노드의 나가는 간선 개수 - 막대 그래프 개수 - 8자모양 그래프 개수


*/

class Solution {
    
    public int[] solution(int[][] edges) {
        int[] answer = new int[4];
        
        int n = -1;
        // getMax nodes
        for(int[] edge: edges) {
            n = Math.max(n, edge[0]);
            n = Math.max(n, edge[1]);
        }
        
        int[][] numEdges = new int[n+1][2]; // [][0] : out edge, [][1] : in edge
        
        for(int[] edge: edges) {
            int from = edge[0];
            int to = edge[1];
            
            numEdges[from][0]++;
            numEdges[to][1]++;
        }
        
        int addedNode = getAddedNode(numEdges);
        answer[0] = addedNode;

        
        answer[2] = getStickCount(numEdges);
        answer[3] = get8count(numEdges);
        answer[1] = numEdges[addedNode][0] - answer[2] - answer[3];
        
        return answer;
    }
    
    static int getStickCount(int[][] numEdges) {
        int cnt = 0;
        for(int index = 1; index < numEdges.length; index++) {
            if(numEdges[index][0] == 0 && numEdges[index][1] > 0) {
                cnt++;
            }
        }
        return cnt;
    }
    
    static int get8count(int[][] numEdges) {
        int cnt = 0;
        for(int index = 1; index < numEdges.length; index++) {
            if(numEdges[index][0] >= 2 && numEdges[index][1] >= 2) {
                cnt++;
            }
        }
        return cnt;
    }
    
    static int getAddedNode(int[][] numEdges) {
        int result = -1;
        for(int index = 1; index < numEdges.length; index++) {
            if(numEdges[index][1] == 0 && numEdges[index][0] >= 2) {
                result = index;
                break;
            }
        }
        return result;
    }
}








