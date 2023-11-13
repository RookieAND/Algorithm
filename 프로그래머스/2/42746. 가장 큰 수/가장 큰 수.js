// 문자열 변환 후 두 수를 이어 붙였을 때 더 큰 값으로 정렬해야 함.
// ex : [3, 310] 이라면 3310 이 3103 보다 훨씬 큼 (값이 같으면 자릿수가 작을수록 유리)
function solution(numbers) {
    const answer = numbers.map((num) => String(num)).sort((a, b) => (b + a) - (a + b)).join("");
    return answer[0] === '0' ? '0' : answer;
}
