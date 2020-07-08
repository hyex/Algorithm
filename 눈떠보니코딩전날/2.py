# rock = [1, 2, 1, 4]
rock = [5, 3, 4, 1, 3, 8, 3]
person = [{
    "이름" : "루비독",
    "나이" : "95년생",
    "점프력" : "3",
    "몸무게" : "4",
    }, {
    "이름" : "피치독",
    "나이" : "95년생",
    "점프력" : "3",
    "몸무게" : "3",
    }, {
    "이름" : "씨-독",
    "나이" : "72년생",
    "점프력" : "2",
    "몸무게" : "1",
    }, {
    "이름" : "코볼독",
    "나이" : "59년생",
    "점프력" : "1",
    "몸무게" : "1",
    },
]


def solution(rock, person):
    answer = [ i["이름"] for i in person]
    for i in person:
        x = 0
        while x < len(rock)-1:
            x += int(i["점프력"])
            rock[x-1] -= int(i["몸무게"])
            if rock[x-1] < 0:
                del answer[answer.index(i["이름"])]
                break
    return answer


print(solution(rock.copy(), person.copy()))
