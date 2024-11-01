class Solution {

    static String[] dirsStr = {"d" , "l", "r", "u"};
    static int[][] dirs = {{1, 0}, {0, -1}, {0, 1}, {-1, 0}};
    static StringBuilder answer;
    static String result;
    static int endRow, endCol, mapRow, mapCol;

    public static String solution(int n, int m, int x, int y, int r, int c, int k) {

        result = null;
        answer = new StringBuilder();
        mapRow = n;
        mapCol = m;
        endRow = r;
        endCol = c;
        // x, y : start
        // r, c : end

        int distance = distance(x, y, endRow, endCol);
        if (distance > k || (k - distance) % 2 == 1) return "impossible";
        dfs(x, y, 0, k);

        return result != null ? result : "impossible";
    }

    static int distance(int x, int y, int r, int c) {
        return Math.abs(x - r) + Math.abs(y - c);
    }

    static void dfs(int row, int col, int depth, int limit) {
        if (result != null) return;
        if (depth + distance(row, col, endRow, endCol) > limit) return;

        if (limit == depth) {
            if (row == endRow && col == endCol) result = answer.toString();
            return;
        }
        
        for (int i = 0; i < dirs.length; i++) {
            int nRow = row + dirs[i][0];
            int nCol = col + dirs[i][1];
            if (nRow > 0 && nCol > 0 && nRow <= mapRow && nCol <= mapCol) {
                answer.append(dirsStr[i]);
                dfs(nRow, nCol, depth + 1, limit);
                answer.delete(depth, depth + 1);
            }
        }
    }
}