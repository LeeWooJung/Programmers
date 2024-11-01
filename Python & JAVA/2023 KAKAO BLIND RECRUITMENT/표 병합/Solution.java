import java.util.*;

class Solution {
    static String[][] req = new String[51][51];
    static Pair[][] merge = new Pair[51][51];
    static boolean[][] check;
    static int answerLength = 0;

    public String[] solution(String[] commands) {
        // merge 초기화
        for(int i=1;i<=50;i++){
            for(int j=1;j<=50;j++){
                // 자기 자신을 가리키도록 초기화
                merge[i][j] = new Pair(i,j);
            }
        }
        // queue 초기화
        Queue<String> res = new LinkedList<>();

        for(int i=0;i<commands.length;i++){
            String command = commands[i];
            StringTokenizer st = new StringTokenizer(command);

            // 커맨드 타입
            String type = st.nextToken();

            // update
            if(Objects.equals(type, "UPDATE")){
                // 위치 좌표를 입력받을 때
                if(st.countTokens() == 3){
                    int r = Integer.parseInt(st.nextToken());
                    int c = Integer.parseInt(st.nextToken());
                    String str = st.nextToken();
                    
                    // 입력받은 좌표의 merge 배열이 가리키는 좌표의 값을 변경
                    req[merge[r][c].r][merge[r][c].c] = str;
                }

                // 값을 입력받을 때
                if(st.countTokens() == 2){
                    String str1 = st.nextToken();
                    String str2 = st.nextToken();

                    // 표 전체에서 str1 문자열 찾은 후 str2로 치환
                    for(int r=1;r<=50;r++){
                        for(int c=1;c<=50;c++){
                            if(Objects.equals(req[r][c], str1)) req[r][c] = str2;
                        }
                    }
                }
            }

            // merge
            else if(Objects.equals(type, "MERGE")){
                int r1 = Integer.parseInt(st.nextToken());
                int c1 = Integer.parseInt(st.nextToken());
                int r2 = Integer.parseInt(st.nextToken());
                int c2 = Integer.parseInt(st.nextToken());

                // 입력받은 좌표의 merge 배열이 가리키는 좌표
                int newR1 = merge[r1][c1].r;
                int newC1 = merge[r1][c1].c;
                int newR2 = merge[r2][c2].r;
                int newC2 = merge[r2][c2].c;
                
                // merge 배열에서 newR2,newC2 값을 가지는 부분을 전부 newR1, newC1로 변경
                for(int j=1;j<=50;j++){
                    for(int k=1;k<=50;k++){
                        if(merge[j][k].r == newR2 && merge[j][k].c == newC2)
                            merge[j][k] = new Pair(newR1,newC1);
                    }
                }
                
                // 두 위치의 셀이 같은 셀일 경우 무시
                if(newR1 != newR2 || newC1 != newC2){
                    // 두 셀 중 한 셀이 값을 가지고 있을 경우 병합된 셀은 그 값을 가짐
                    if(!Objects.equals(req[newR1][newC1], null) && Objects.equals(req[newR2][newC2], null)){
                        req[newR2][newC2] = req[newR1][newC1];
                    }
                    else if(Objects.equals(req[newR1][newC1], null) && !Objects.equals(req[newR2][newC2], null)){
                        req[newR1][newC1] = req[newR2][newC2];
                    }

                    // 두 셀 모두 값을 가지고 있을 경우 병합된 셀은 r1,c1 위치의 셀 값 가짐
                    else if(!Objects.equals(req[newR1][newC1], null) && !Objects.equals(req[newR2][newC2], null)){
                        req[newR2][newC2] = req[newR1][newC1];
                    }
                }
            }

            // unmerge
            else if(Objects.equals(type, "UNMERGE")){
                int r = Integer.parseInt(st.nextToken());
                int c = Integer.parseInt(st.nextToken());

                // 입력받은 좌표의 merge 배열이 가리키는 좌표
                int newR = merge[r][c].r;
                int newC = merge[r][c].c;
                String str = req[newR][newC];

                // merge값이 newR, newC인 부분을 자기 자신으로 치환 후 req값도 null로 비우기
                for(int j=1;j<=50;j++){
                    for(int k=1;k<=50;k++){
                        if(merge[j][k].r == newR && merge[j][k].c == newC){
                            merge[j][k] = new Pair(j,k);
                            req[j][k] = null;
                        }
                    }
                }
                
                // 값 변경
                req[r][c] = str;
            }

            // print
            else if(Objects.equals(type, "PRINT")){
                int r = Integer.parseInt(st.nextToken());
                int c = Integer.parseInt(st.nextToken());
                answerLength++;

                // 입력받은 좌표의 merge 배열이 가리키는 좌표
                int newR = merge[r][c].r;
                int newC = merge[r][c].c;
                String str = req[newR][newC];

                // 선택한 셀이 비어있을 경우 EMPTY 출력
                if(Objects.equals(str, null)) res.add("EMPTY");
                else res.add(str);
            }
        }

        String[] answer = new String[answerLength];
        int idx = 0;    
        while(!res.isEmpty()){
            answer[idx] = res.poll();
            idx++;
        }
        return answer;
    }
}

class Pair{
    int r;
    int c;

    Pair(int r, int c){
        this.r = r;
        this.c = c;
    }
}