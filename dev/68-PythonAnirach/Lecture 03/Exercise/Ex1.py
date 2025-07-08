def CheckPromation(score1,score2,score3):
    ressum = score1 + score2 + score3
    avg = ressum / 3 

    print(avg)

    if avg > 95:
        print('"Congratulations!"')
        print("That's is great avarage!")
    else:
        print('กระจอก')
        
score1 = int(input('Enter the score for test 1: '))
score2 = int(input('Enter the score for test 2: '))
score3 = int(input('Enter the score for test 3: '))

CheckPromation(score1,score2,score3)
