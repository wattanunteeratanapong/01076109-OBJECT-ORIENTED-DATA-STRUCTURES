# Chapter : 1 - item : 3 - Election

# โรงเรียนดังประจำจังหวัดแห่งหนึ่ง จะมีการจัดการเลือกตั้งหาประธานนักเรียนคนใหม่ขึ้นในทุกๆปี โดยในปีนี้มีผู้เข้าแข่งขันสูงถึง 20 คน โดยกฤษฎาได้รับมอบหมายให้เป็นผู้นับคะแนนเลือกตั้งในปีนี้ แต่กฤษฎารู้สึกขี้เกียจนับคะแนนขึ้นมา จึงได้ไหว้วานให้คุณช่วยเขียนโปรแกรม ในการหาว่าผู้เข้าแข่งขันคนใดได้รับคะแนนสูงที่สุด
# ข้อควรระวัง หากมีการเลือกเลขที่ไม่ตรงกับผู้เข้าแข่งขัน (1-20) จะนับว่าเป็นบัตรเสีย และถ้าหากทุกใบเป็นบัตรเสียจะถือว่าไม่มีผู้ชนะ

print("*** Election ***")
num_voter = int(input("Enter a number of voter(s) : "))
votes = list(map(int, input("").split()))

votes = [vote for vote in votes if 0 <= vote <= 20]

if not votes:
    print("*** No Candidate Wins ***")
else:
    votes_count = {}
    for vote in votes:
        if vote in votes_count:
            votes_count[vote] += 1
        else:
            votes_count[vote] = 1

    max_val = max(votes_count.values())

    winners = [candidate for candidate, count in votes_count.items() if count == max_val]

    print(' '.join(map(str, sorted(winners))))
