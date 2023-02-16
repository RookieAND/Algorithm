// '(' 열린 괄호를 만나면 stack 에 이를 추가하고, 닫힌 괄호를 만나면 stack에서 제거한다.
function solution(s){
    let openBracket = 0

    for (const char of s) {
        // 열린 괄호를 만났다면 수량을 1개 추가하고 다음 반복을 진행.
        if (char == '(') {
            openBracket += 1;
            continue
        }
        // 만약 열린 괄호가 없는데 닫힌 괄호가 들어왔다면 false.
        if (!openBracket) {
            return false
        }
        openBracket -= 1;
    }
    // 괄호가 완전히 열리고 닫혀 stack 내부가 비었다면 true, 아니라면 false
    return openBracket === 0;
}