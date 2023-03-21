function solution(cap, n, deliveries, pickups) {
    deliveries.reverse()
    pickups.reverse()
    let answer = 0

    let have_to_deli = 0
    let have_to_pick = 0

    for (let i = 0; i <= n; i++) {
        have_to_deli += deliveries[i]
        have_to_pick += pickups[i]

        while (have_to_deli > 0 || have_to_pick > 0) {
            have_to_deli -= cap
            have_to_pick -= cap
            answer += (n - i) * 2   
        }   
    }

    return answer
}