// 출저: https://school.programmers.co.kr/learn/courses/30/lessons/181920
// 유형: 배열 
// 날짜: 6/30

class Solution { // Solution 클래스 정의
  
    public int[] solution(int start, int end) { // solution 메서드 정의, int 배열을 반환
        int[] answer = new int[end - start + 1]; // end - start + 1 크기의 int 배열 생성

        for(int i = 0; i <= end - start; i++) { // 0부터 end - start까지 반복
            answer[i] = start + i; // 배열의 각 요소에 start에서 시작하는 연속된 숫자 저장
        }

        return answer; // 생성된 배열 반환
    }
}
