function solution(s){
    let openBracket = 0

    for (const char of s) {
        // 열린 괄호인지, 닫힌 괄호인지에 따라 열린 괄호의 수량을 더하거나 빼줌.
        openBracket += char == '(' ? 1 : -1
        // 만약 열린 괄호의 수량이 0 혹은 그 이하로 떨어진다면 false
        if (openBracket < 0) return false
    }
    // 괄호가 완전히 열리고 닫혀 수량이 0개라면 true, 아니라면 false
    return openBracket === 0;
}